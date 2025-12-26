## 1️⃣ Purchase List for MVP

### AIO TEC + Cooling Solution 240W

https://aliexpress.com/item/1005008570707899.html
A51I 240W 2x12710 Electronic Semiconductor Refrigeration 12V Diy Refrigerator Cooler Cooling System Kit Diy Refrigerator Cooler

Several similar models, this one has clearer stated 2x12710 (2x the model of TEC included). After checking with AI, this seems to be a trully 240W unit with 2x Tower Heatsink and 2X100mm fans


### PSU (regulated 12V 30A)

https://aliexpress.com/item/1005004655805485.html
Key Source 12v 30A 360W P/ Cftv Led Tape Automotive Sound

12V 30A no fan and slim


### Fuse and Distribution Box

https://aliexpress.com/item/1005009223175783.htm
DaierTek 6 12 Way Fuse Block 12 Volt Blade Fuse Block with LED Indicator Circuit Fuse Box 12V ATO/ATC Marine Fuse Panel For Car

12V 100A Max Total 30A per channel. Does not include 30A fuse must buy 


### MOSFET Power Switch Module



### Humidity Sensor and Controller


* **XH-M452** humidity controller (RH setpoint + relay)






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
