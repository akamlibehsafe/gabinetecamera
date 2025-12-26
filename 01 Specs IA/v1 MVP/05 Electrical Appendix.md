# ✅ FINAL ELECTRICAL APPENDIX — MVP (TEC Dehumidifier)

> **Status:** FINAL — ELECTRICAL (MVP)
> **Scope:** Power distribution, protection, wiring gauges, control logic, modes, and terminal-level wiring
> **Frozen components:** **DaierTek Fuse Box** (as defined below)

---

## 1) System Purpose (Electrical)

Provide safe, expandable 12 V DC power distribution and simple control for a TEC-based dehumidifier MVP, ensuring:

* **Branch circuit protection** (fusing per circuit)
* **Safe high-current switching** (MOSFET)
* **Automatic control** by RH + cold-plate temperature (anti-ice)
* **Fans always ON when TEC is ON**
* Expandability for future circuits

---

## 2) Frozen Power Distribution Component

### 2.1 DaierTek Fuse Box (FROZEN)

**Name (canonical):** *DaierTek Fuse Box*
**Type:** Marine/automotive fuse distribution panel with integrated +/− buses and LED indicators
**Fuse type:** ATO/ATC (blade)
**Voltage:** 12–36 V DC
**Total rating:** 100 A continuous
**Per-way rating:** 30 A max per circuit
**Ways:** 6
**Features:** Transparent cover, label stickers, screw terminals, LED per circuit

---

## 3) Bill of Materials (Electrical)

### 3.1 Power

* **PSU:** Regulated **12 V DC**, **≥30 A** (recommended **≥40 A**)

  * Terminals: **V+**, **V−**
* **DaierTek Fuse Box:** as above

### 3.2 Control Modules

* **XH-M452** humidity controller (RH setpoint + relay)

  * Power: **VCC / +12V**, **GND**
  * Relay: **COM**, **NO**, **NC** (use **COM/NO** only)
* **W1209** thermostat controller (cold plate temperature cutoff)

  * Power: **VCC / +12V**, **GND**
  * Relay: **COM**, **NO**, **NC** (use **COM/NO** only)

### 3.3 Switching

* **MOSFET Power Module**: **5–36 V DC**, **≥30 A**

  * Power: **VIN+**, **VIN−**, **VOUT+**, **VOUT−**
  * Signal: **SIG+**, **SIG−** (may be labeled IN+/IN− or PWM+/PWM−)

### 3.4 Load

* **XD-6038 TEC kit** (or equivalent) with:

  * TEC(s) leads: **TEC+ (red)**, **TEC− (black)**
  * Fans: **FAN+ (red)**, **FAN− (black)** (3× fans typical)

---

## 4) Protection & Fuse Plan (Frozen)

### 4.1 Fuse Assignment

| DaierTek Slot | Circuit                       | Fuse              |
| ------------- | ----------------------------- | ----------------- |
| **F1**        | TEC + Fans (via MOSFET)       | **30 A ATO/ATC**  |
| **F2**        | Controllers (XH-M452 + W1209) | **3–5 A ATO/ATC** |
| F3–F6         | Future circuits               | as needed         |

**Note:** Listing-provided fuse assortments often do **not** include 30 A; you must buy **30 A blade fuse** separately.

---

## 5) Wiring Gauge Specification (Frozen)

| Segment                                                     | Recommended Wire              |
| ----------------------------------------------------------- | ----------------------------- |
| **PSU → DaierTek (+ and − inputs)**                         | **4.0 mm² (≈ AWG12)**         |
| **DaierTek F1 → MOSFET VIN / MOSFET VOUT → TEC**            | **2.5–4.0 mm² (≈ AWG14–12)**  |
| **MOSFET VOUT → fan branches**                              | **1.0–1.5 mm² (≈ AWG18–16)**  |
| **DaierTek F2 → controllers + relay logic + MOSFET signal** | **0.5–0.75 mm² (≈ AWG20–18)** |

---

## 6) Electrical Logic (Frozen)

### 6.1 Control Condition

**TEC + Fans ON** only when both are true:

1. **RH above setpoint** (XH-M452 relay closed)
2. **Cold plate above cutoff temperature** (W1209 relay closed)

If either opens → MOSFET turns OFF → TEC and fans OFF.

### 6.2 Fan Rule (Frozen)

**Fans must be powered from MOSFET VOUT in parallel with TEC**, so they run whenever TEC runs.

---

## 7) Wiring Schematic (MD Reference)

### 7.1 Main Feed (PSU → DaierTek)

* **PSU V+ → DaierTek + INPUT**
* **PSU V− → DaierTek − INPUT**

Only **two wires** between PSU and DaierTek: **+** and **−**.

### 7.2 High-Current Branch (DaierTek F1 → MOSFET → TEC + Fans)

* **DaierTek F1 + → MOSFET VIN+**
* **DaierTek F1 − → MOSFET VIN−**
* **MOSFET VOUT+ → TEC+ AND all FAN+ (parallel)**
* **MOSFET VOUT− → TEC− AND all FAN− (parallel)**

### 7.3 Controller Power (DaierTek F2 → controllers)

* **DaierTek F2 + → XH-M452 VCC**
* **DaierTek F2 − → XH-M452 GND**
* **DaierTek F2 + → W1209 VCC**
* **DaierTek F2 − → W1209 GND**

### 7.4 Relay Chain (Series logic → MOSFET SIG)

* **DaierTek F2 + → XH-M452 relay COM**
* **XH-M452 relay NO → W1209 relay COM**
* **W1209 relay NO → MOSFET SIG+**
* **MOSFET SIG− → DaierTek F2 −**

Use **COM/NO only**. Ignore NC.

---

## 8) Literal Wiring Recipe (Terminal-Level)

**Power OFF, PSU unplugged from AC.**

### 8.1 PSU → DaierTek

1. Connect **PSU V+ → DaierTek + INPUT** (AWG12)
2. Connect **PSU V− → DaierTek − INPUT** (AWG12)

### 8.2 Install Fuses

3. Insert **30A** blade fuse in **F1**
4. Insert **3–5A** blade fuse in **F2**

### 8.3 DaierTek F1 → MOSFET VIN (high current)

5. **DaierTek F1 + → MOSFET VIN+** (AWG14–12)
6. **DaierTek F1 − → MOSFET VIN−** (AWG14–12)

### 8.4 MOSFET VOUT → TEC + Fans (high current)

7. **MOSFET VOUT+ → TEC+ (red)** (AWG14–12)
8. **MOSFET VOUT− → TEC− (black)** (AWG14–12)
9. **MOSFET VOUT+ → FAN1+ / FAN2+ / FAN3+ (parallel)** (AWG18–16)
10. **MOSFET VOUT− → FAN1− / FAN2− / FAN3− (parallel)** (AWG18–16)

### 8.5 DaierTek F2 → Controller power (low current)

11. **DaierTek F2 + → XH-M452 VCC** (AWG20–18)
12. **DaierTek F2 − → XH-M452 GND** (AWG20–18)
13. **DaierTek F2 + → W1209 VCC** (AWG20–18)
14. **DaierTek F2 − → W1209 GND** (AWG20–18)

### 8.6 Relay logic chain → MOSFET signal (low current)

15. **DaierTek F2 + → XH-M452 relay COM**
16. **XH-M452 relay NO → W1209 relay COM**
17. **W1209 relay NO → MOSFET SIG+**
18. **MOSFET SIG− → DaierTek F2 −**

### 8.7 Sensors

19. Place **XH-M452 RH sensor** mid-air inside chamber
20. Attach **W1209 probe** to cold plate with thermal paste + tape/clamp

---

## 9) Operating Modes (Frozen)

### 9.1 1-TEC Mode (recommended first test)

* Disconnect TEC2 **both + and −**, insulate ends
* Keep fans connected normally
* Lower power, easier tuning

### 9.2 2-TEC Mode

* Reconnect TEC2 leads
* Higher power, higher icing risk

No wiring diagram changes required—only which TEC leads are connected.

---

## 10) Initial Controller Settings (Baseline)

### W1209 (cold plate protection)

* Mode: **Cooling**
* Setpoint: **8 °C**
* Hysteresis: **3 °C**
* If icing occurs: raise to **10–12 °C**

### XH-M452 (humidity demand)

* Setpoint: **55% RH**
* Hysteresis: ~5%

---

## 11) Commissioning Checklist (Electrical)

* Verify all screws tight (PSU, DaierTek, MOSFET)
* Verify fuses: **F1=30A**, **F2=3–5A**
* Confirm TEC and fans connected to **MOSFET VOUT**, not VIN
* Confirm relay chain uses **COM/NO**
* Confirm polarity (red = +, black = −)
* First power-on:

  * Fans should only run when MOSFET is enabled
  * If fans run continuously, they are not on VOUT

---

## 12) Terminology Clarification (Important)

In this document:

* “Ground” means **PSU negative (0 V)**.
* PSU to DaierTek uses only **two wires: + and −**.
* AC earth (wall ground) is not part of the DC wiring scheme.

---

## 13) Appendix Status

✅ This document is the **FINAL ELECTRICAL APPENDIX** for the MVP.
All future MVP wiring diagrams and build steps must remain consistent with this appendix unless explicitly “unfrozen.”
