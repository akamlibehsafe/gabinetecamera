Perfect. Below is the **FINAL, UPDATED LITERAL WIRING RECIPE**, rewritten **from scratch**, now **explicitly using the DaierTek Fuse Box**, and aligned **100% with the frozen MVP spec**.

This is written for a **non-electrician**, in a **do-this-then-that order**, with **exact terminal names**, **wire gauges**, and **clear intent**.

You can follow this **line by line** without needing to interpret the schematic.

---

# 🧾 **LITERAL WIRING RECIPE — TEC DEHUMIDIFIER MVP**

> **Power:** 12 V DC
> **Distribution:** **DaierTek Fuse Box** (100 A total, 30 A per circuit)
> **Loads:** TEC(s) + Fans, Controllers
> **Control:** XH-M452 (RH) + W1209 (Cold Plate Temp) + MOSFET
> **Fans:** ON whenever TEC is ON

---

## 0️⃣ SAFETY FIRST (READ ONCE)

* ❗ **PSU must be unplugged from AC mains**
* ❗ Never wire or change connections with PSU powered
* ❗ This is low voltage but **high current**
* ❗ Double-check polarity before power-on

---

## 1️⃣ WIRE GAUGE (DO NOT SKIP)

| Path                       | Wire                        |
| -------------------------- | --------------------------- |
| PSU → DaierTek (+ and −)   | **4.0 mm² (AWG12)**         |
| DaierTek F1 → MOSFET → TEC | **2.5–4.0 mm² (AWG14–12)**  |
| Fan branches               | **1.0–1.5 mm² (AWG18–16)**  |
| Controllers + logic        | **0.5–0.75 mm² (AWG20–18)** |

---

## 2️⃣ IDENTIFY TERMINALS (BEFORE CONNECTING)

### Power Supply (PSU)

* **V+**  → +12 V
* **V−**  → 0 V / Negative

---

### DaierTek Fuse Box

* **+ INPUT**  (main positive bus)
* **− INPUT**  (main negative bus)
* **F1 + / F1 −**
* **F2 + / F2 −**
* **F3–F6** (unused for now)

---

### MOSFET Power Module

* **VIN+**
* **VIN−**
* **VOUT+**
* **VOUT−**
* **SIG+** (or IN+ / PWM+)
* **SIG−** (or IN− / PWM−)

---

### Controllers

**XH-M452**

* **VCC / +12V**
* **GND**
* **Relay COM**
* **Relay NO**

**W1209**

* **VCC / +12V**
* **GND**
* **Relay COM**
* **Relay NO**

---

### Loads

* **TEC+** (red)
* **TEC−** (black)
* **FAN+** (red)
* **FAN−** (black)

---

## 3️⃣ MAIN POWER FEED (PSU → DAIERTEK)

### Step 1 — PSU + to DaierTek + INPUT

Connect:

```
PSU V+  →  DaierTek + INPUT
```

* Wire: **4.0 mm² (AWG12)**

---

### Step 2 — PSU − to DaierTek − INPUT

Connect:

```
PSU V−  →  DaierTek − INPUT
```

* Wire: **4.0 mm² (AWG12)**

✅ Now the DaierTek Fuse Box is your **central +/− hub**.

---

## 4️⃣ FUSE INSTALLATION (DO THIS NOW)

Insert fuses into the DaierTek Fuse Box:

| Slot      | Fuse                    |
| --------- | ----------------------- |
| **F1**    | **30 A** (TEC + Fans)   |
| **F2**    | **3–5 A** (Controllers) |
| **F3–F6** | Empty (future use)      |

---

## 5️⃣ HIGH-CURRENT CIRCUIT — TEC + FANS

### Step 3 — DaierTek F1 + to MOSFET VIN+

Connect:

```
DaierTek F1 +  →  MOSFET VIN+
```

* Wire: **2.5–4.0 mm²**

---

### Step 4 — DaierTek F1 − to MOSFET VIN−

Connect:

```
DaierTek F1 −  →  MOSFET VIN−
```

* Wire: **2.5–4.0 mm²**

---

### Step 5 — MOSFET VOUT+ to TEC +

Connect:

```
MOSFET VOUT+  →  TEC+ (red)
```

* Wire: **2.5–4.0 mm²**

---

### Step 6 — MOSFET VOUT− to TEC −

Connect:

```
MOSFET VOUT−  →  TEC− (black)
```

* Wire: **2.5–4.0 mm²**

---

### Step 7 — MOSFET VOUT+ to FAN + (parallel)

Connect:

```
MOSFET VOUT+  →  FAN1+  
               FAN2+  
               FAN3+
```

* Wire: **1.0–1.5 mm²**

---

### Step 8 — MOSFET VOUT− to FAN − (parallel)

Connect:

```
MOSFET VOUT−  →  FAN1−  
               FAN2−  
               FAN3−
```

* Wire: **1.0–1.5 mm²**

✅ **Fans and TEC turn ON and OFF together**

---

## 6️⃣ CONTROLLER POWER (LOW CURRENT)

### Step 9 — DaierTek F2 + to XH-M452 VCC

Connect:

```
DaierTek F2 +  →  XH-M452 VCC
```

---

### Step 10 — DaierTek F2 − to XH-M452 GND

Connect:

```
DaierTek F2 −  →  XH-M452 GND
```

---

### Step 11 — DaierTek F2 + to W1209 VCC

Connect:

```
DaierTek F2 +  →  W1209 VCC
```

---

### Step 12 — DaierTek F2 − to W1209 GND

Connect:

```
DaierTek F2 −  →  W1209 GND
```

---

## 7️⃣ CONTROL LOGIC (RELAY CHAIN)

> Goal: TEC runs **only if RH is high AND plate is not too cold**

---

### Step 13 — DaierTek F2 + to XH-M452 Relay COM

Connect:

```
DaierTek F2 +  →  XH-M452 Relay COM
```

---

### Step 14 — XH-M452 Relay NO to W1209 Relay COM

Connect:

```
XH-M452 Relay NO  →  W1209 Relay COM
```

---

### Step 15 — W1209 Relay NO to MOSFET SIG+

Connect:

```
W1209 Relay NO  →  MOSFET SIG+
```

---

### Step 16 — MOSFET SIG− to DaierTek F2 −

Connect:

```
MOSFET SIG−  →  DaierTek F2 −
```

✅ Both relays must close → MOSFET turns ON

---

## 8️⃣ SENSOR INSTALLATION

### Step 17 — XH-M452 RH Sensor

* Place **mid-air** inside chamber
* Away from cold plate

---

### Step 18 — W1209 Temperature Probe

* Attach to **cold plate**
* Use **thermal paste**
* Tape or clamp firmly

---

## 9️⃣ 1-TEC / 2-TEC MODE

### 1-TEC MODE (recommended first)

* Disconnect **TEC2 + and −**
* Insulate both wires
* Leave fans connected

### 2-TEC MODE

* Both TECs connected normally
* No wiring changes needed

---

## 🔟 FINAL CHECK (DO NOT SKIP)

### Step 19 — Visual inspection

* TEC + fans connected to **MOSFET VOUT**, not VIN
* Relays use **COM + NO**, not NC
* Correct fuse values
* No loose strands

---

### Step 20 — First Power-On

1. Plug PSU into AC
2. Set:

   * **W1209:** Cooling, 8 °C, hysteresis 3 °C
   * **XH-M452:** 55% RH
3. Verify:

   * Fans spin when TEC runs
   * Fans stop when TEC stops

---

## ✅ END STATE

* ✔ DaierTek Fuse Box integrated
* ✔ TEC and fans safely fused
* ✔ Anti-ice protection active
* ✔ Ready for MVP testing

---

If you want, next I can:

* condense this into a **one-page bench checklist**
* add a **fault-diagnosis table**
* or mark this as **FINAL ELECTRICAL APPENDIX** for the project
