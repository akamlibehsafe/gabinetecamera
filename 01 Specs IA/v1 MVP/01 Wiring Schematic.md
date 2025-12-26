Perfect. Below is the **REGENERATED WIRING SCHEMATIC**, written **entirely in Markdown**, designed to be:

* ✅ readable as text
* ✅ printable
* ✅ unambiguous
* ✅ consistent with the **frozen MVP spec**
* ✅ using the **DaierTek Fuse Box** as the central hub

This is a **schematic + wiring reference**, not a literal step list (you already have that).
Think of it as the **“map”**, while the recipe is the **“instructions”**.

---

# 🔌 **WIRING SCHEMATIC — TEC DEHUMIDIFIER MVP (MD)**

> **Power:** 12 V DC
> **Distribution:** DaierTek Fuse Box (100 A total, 30 A per circuit)
> **Loads:** TEC(s) + Fans, Controllers
> **Control:** XH-M452 (RH) + W1209 (Temp) + MOSFET

---

## 1️⃣ SYSTEM OVERVIEW (BLOCK LEVEL)

```
        AC MAINS
            │
            ▼
      ┌──────────┐
      │ 12V PSU  │
      │ ≥30–40A  │
      └────┬─────┘
           │
           ▼
 ┌───────────────────┐
 │ DaierTek Fuse Box │  ← Central + / − distribution
 │ 100A / 30A per ch│
 └───┬─────────┬────┘
     │         │
     │         │
     ▼         ▼
 TEC + FANS   CONTROLLERS
 (via MOSFET) (XH-M452 + W1209)
```

---

## 2️⃣ POWER DISTRIBUTION — DAIERTEK FUSE BOX

### Inputs (from PSU)

```
PSU V+  ───────────►  DaierTek + INPUT
PSU V−  ───────────►  DaierTek − INPUT
```

> Only **two wires** between PSU and fuse box: **+ and −**

---

### Fuse Assignments (Frozen)

```
DaierTek Fuse Slots:

F1  ── 30A ── TEC + Fans (via MOSFET)
F2  ── 3–5A ─ Controllers (XH-M452 + W1209)
F3  ── spare
F4  ── spare
F5  ── spare
F6  ── spare
```

---

## 3️⃣ HIGH-CURRENT PATH — TEC + FANS

```
DaierTek F1 (+) ──► MOSFET VIN+
DaierTek F1 (−) ──► MOSFET VIN−
```

### MOSFET Output (Switched Power)

```
MOSFET VOUT+ ──► TEC+ (red)
               ├─► FAN1+
               ├─► FAN2+
               └─► FAN3+

MOSFET VOUT− ──► TEC− (black)
               ├─► FAN1−
               ├─► FAN2−
               └─► FAN3−
```

✅ **TEC and fans are in parallel**
✅ **Fans are ON whenever TEC is ON**
✅ **MOSFET switches only the + side**

---

## 4️⃣ LOW-CURRENT POWER — CONTROLLERS

```
DaierTek F2 (+) ──► XH-M452 VCC
                 └─► W1209 VCC

DaierTek F2 (−) ──► XH-M452 GND
                 └─► W1209 GND
```

---

## 5️⃣ CONTROL LOGIC — RELAY CHAIN

### Logical rule (frozen)

```
TEC ENABLE =
   (RH above setpoint)
AND
   (Cold plate temperature above cutoff)
```

---

### Wiring (Series Relay Logic)

```
DaierTek F2 (+)
      │
      ▼
XH-M452 Relay COM
      │
      └──► XH-M452 Relay NO
                    │
                    ▼
             W1209 Relay COM
                    │
                    └──► W1209 Relay NO
                                  │
                                  ▼
                           MOSFET SIG+

MOSFET SIG− ───────────────► DaierTek F2 (−)
```

✔ Both relays must close
✔ Any fault opens the chain
✔ MOSFET shuts off safely

---

## 6️⃣ SENSOR PLACEMENT (REFERENCE)

```
[ SEALED CHAMBER ]

   (Air)
     │
     │  XH-M452 RH SENSOR
     │  (mid-air, shaded)
     │
 ┌───▼──────────────────┐
 │     COLD PLATE       │◄── W1209 probe
 │ (condensation zone)  │    (thermal paste)
 └──────────────────────┘
```

---

## 7️⃣ 1-TEC vs 2-TEC MODE (SCHEMATIC VIEW)

### 1-TEC MODE

```
MOSFET VOUT → TEC1 + fans
TEC2 disconnected (both + and − insulated)
```

### 2-TEC MODE

```
MOSFET VOUT → TEC1 + TEC2 + fans (parallel)
```

No schematic changes required — only which TEC leads are connected.

---

## 8️⃣ CURRENT DOMAINS (IMPORTANT CONCEPT)

```
HIGH CURRENT:
 PSU → DaierTek → MOSFET → TEC + fans

LOW CURRENT:
 DaierTek → Controllers → Relays → MOSFET signal
```

These domains **must never mix** directly.

---

## 9️⃣ GROUND / NEGATIVE CLARIFICATION

* “Ground” = **PSU negative (0 V)**
* No earth ground involved
* All − returns go to **DaierTek − bus**
* One − wire returns to PSU

---

## 🔟 SCHEMATIC SUMMARY (ONE-LINE)

```
PSU → DaierTek Fuse Box
   → F1 → MOSFET → TEC + Fans
   → F2 → Controllers → Relays → MOSFET signal
All returns → DaierTek − → PSU −
```

---

## ✅ STATUS

* ✔ Matches frozen MVP spec
* ✔ Includes DaierTek Fuse Box
* ✔ Fans fully integrated
* ✔ Safe, readable, printable
* ✔ Ready for build

---

If you want next, I can:

* regenerate the **literal wiring recipe** referencing DaierTek terminal names,
* produce a **fault-diagnosis schematic** (“if X happens, check Y”),
* or lock this into a **final electrical appendix** for your project documentation.
