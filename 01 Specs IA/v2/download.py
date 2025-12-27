import io, os, re, zipfile, math, requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# ---- CONFIG ----
STATION_CODE = "83721"          # CAMPINAS - AEROPORTO (traditional_station_identifier)
YEARS_BACK = 10                 # rolling last 10 years up to now
MONTHS = [1, 2, 3]              # Jan, Feb, Mar
PERCENTILE = 0.90

BASE = "https://portal.inmet.gov.br/uploads/dadoshistoricos"  # annual zips are {year}.zip
OUTDIR = "./inmet_hist"

os.makedirs(OUTDIR, exist_ok=True)

def dew_point_c(Tc, RH):
    """Magnus formula. Tc in °C, RH in %."""
    if pd.isna(Tc) or pd.isna(RH) or RH <= 0:
        return float("nan")
    a, b = 17.62, 243.12
    gamma = (a * Tc) / (b + Tc) + math.log(RH / 100.0)
    return (b * gamma) / (a - gamma)

def find_station_files_in_zip(z: zipfile.ZipFile, station_code: str):
    # INMET zips typically contain multiple CSV/TXT files by station; match code in filename
    pat = re.compile(rf".*{re.escape(station_code)}.*\.(csv|CSV|txt|TXT)$")
    return [n for n in z.namelist() if pat.match(n)]

def read_inmet_file(z: zipfile.ZipFile, name: str):
    raw = z.read(name)
    # Many INMET files are semicolon separated with Portuguese headers, sometimes Latin-1.
    # Try a few encodings.
    for enc in ("utf-8", "latin-1"):
        try:
            text = raw.decode(enc, errors="strict")
            break
        except UnicodeDecodeError:
            text = None
    if text is None:
        text = raw.decode("latin-1", errors="replace")
    # Detect delimiter (usually ;)
    delim = ";" if text.count(";") > text.count(",") else ","
    df = pd.read_csv(io.StringIO(text), sep=delim, engine="python")
    return df

def normalize_columns(df):
    # Map common INMET column variants to normalized names
    cols = {c.strip(): c for c in df.columns}
    def pick(*cands):
        for c in cands:
            if c in cols:
                return cols[c]
        return None

    c_date = pick("DATA (YYYY-MM-DD)", "Data", "DATA", "DT_MEDICAO")
    c_time = pick("HORA (UTC)", "Hora UTC", "HORA", "HR_MEDICAO", "HORA UTC")
    c_t    = pick("TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",
                  "TEMPERATURA DO AR - BULBO SECO, HORARIA (C)",
                  "TEMP. AR (°C)", "TEMPERATURA DO AR (°C)", "TEMPERATURA_DO_AR")
    c_rh   = pick("UMIDADE RELATIVA DO AR, HORARIA (%)",
                  "UMIDADE RELATIVA DO AR (%)", "UMID. REL. (%)", "UMIDADE_RELATIVA_DO_AR")

    if not all([c_date, c_time, c_t, c_rh]):
        missing = [("date",c_date),("time",c_time),("T",c_t),("RH",c_rh)]
        raise ValueError(f"Could not map required columns. Found: {df.columns.tolist()} ; Missing map: {missing}")

    out = df[[c_date, c_time, c_t, c_rh]].copy()
    out.columns = ["date", "time_utc", "T_C", "RH_pct"]

    # Parse datetime in UTC
    out["date"] = out["date"].astype(str).str.strip()
    out["time_utc"] = out["time_utc"].astype(str).str.strip()

    # Try time formats like "0000", "00:00", "0"
    def parse_time(s):
        s = str(s).strip()
        s = s.replace(":", "")
        if len(s) == 1:
            s = s.zfill(2) + "00"
        if len(s) == 2:
            s = s + "00"
        return s.zfill(4)

    out["time_utc"] = out["time_utc"].map(parse_time)
    out["dt_utc"] = pd.to_datetime(out["date"] + " " + out["time_utc"], format="%Y-%m-%d %H%M", errors="coerce", utc=True)

    # Coerce numeric
    out["T_C"] = pd.to_numeric(out["T_C"], errors="coerce")
    out["RH_pct"] = pd.to_numeric(out["RH_pct"], errors="coerce")

    out = out.dropna(subset=["dt_utc"]).sort_values("dt_utc").reset_index(drop=True)
    return out[["dt_utc", "T_C", "RH_pct"]]

def linear_interpolate_hourly(df):
    # Reindex to hourly grid and linearly interpolate
    df = df.set_index("dt_utc").sort_index()
    full = df.reindex(pd.date_range(df.index.min(), df.index.max(), freq="H", tz="UTC"))
    full["T_C"] = full["T_C"].interpolate(method="time")
    full["RH_pct"] = full["RH_pct"].interpolate(method="time")
    full = full.reset_index().rename(columns={"index":"dt_utc"})
    return full

def compute_monthly_p90(df, months, p=0.90):
    df = df.copy()
    df["month"] = df["dt_utc"].dt.month
    df = df[df["month"].isin(months)]
    out = {}
    for m in months:
        sub = df[df["month"] == m]
        out[m] = {
            "T_C_p90": float(sub["T_C"].quantile(p)),
            "DP_C_p90": float(sub["DP_C"].quantile(p)),
        }
    return out

def main():
    now = datetime.now(timezone.utc)
    start_year = (now - timedelta(days=365*YEARS_BACK)).year
    end_year = now.year

    all_rows = []
    for y in range(start_year, end_year + 1):
        url = f"{BASE}/{y}.zip"
        print("Downloading", url)
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        z = zipfile.ZipFile(io.BytesIO(r.content))

        station_files = find_station_files_in_zip(z, STATION_CODE)
        if not station_files:
            print(f"Year {y}: no files matched station code {STATION_CODE}")
            continue

        for name in station_files:
            try:
                df_raw = read_inmet_file(z, name)
                df = normalize_columns(df_raw)
                all_rows.append(df)
                print(f"Year {y}: loaded {name} rows={len(df)}")
            except Exception as e:
                print(f"Year {y}: failed {name}: {e}")

    if not all_rows:
        raise RuntimeError("No data loaded. Check station code / file patterns.")

    data = pd.concat(all_rows, ignore_index=True).drop_duplicates(subset=["dt_utc"]).sort_values("dt_utc")

    # Keep rolling last 10 years up to now
    cutoff = now - timedelta(days=365*YEARS_BACK)
    data = data[data["dt_utc"] >= cutoff].reset_index(drop=True)

    # Interpolate to continuous hourly grid
    data = linear_interpolate_hourly(data)

    # Compute dew point AFTER interpolation (as requested)
    data["DP_C"] = [dew_point_c(t, rh) for t, rh in zip(data["T_C"], data["RH_pct"])]

    p90 = compute_monthly_p90(data, MONTHS, PERCENTILE)

    print("\n=== Monthly 90th-percentile (rolling last 10 years) ===")
    for m in MONTHS:
        print(f"Month {m:02d}:  T_p90 = {p90[m]['T_C_p90']:.2f} °C   DP_p90 = {p90[m]['DP_C_p90']:.2f} °C")

if __name__ == "__main__":
    main()
