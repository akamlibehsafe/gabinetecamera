Perfect. Below is the **FULLY REGENERATED, CONSOLIDATED MVP SPEC**, rewritten **from zero**, with **everything frozen and consistent**, incorporating **all updated decisions**, including:

* DaierTek Fuse Box (frozen)
* PSU specs
* Fuse specs
* Wire gauges
* MOSFET
* Fans
* 1-TEC / 2-TEC modes
* Controllers
* Project plan
* Shopping list

This document is meant to be **the single source of truth** for the MVP.

You can safely:

* archive it
* paste into a new chat
* use it as a build manual
* evolve it later into the final product spec

---

# 📌 **MVP SPEC — TEC-BASED DEHUMIDIFIER (PROOF OF CONCEPT)**

> **Status:** MVP — CONSOLIDATED & FROZEN
> **Purpose:** Validate TEC-based dehumidification before committing to custom copper plates, silent cooling, and final furniture
> **Scope:** Electrical, thermal, control, mechanical MVP
> **Non-Goals:** Silence optimization, aesthetics, long-term durability

---

## 1️⃣ MVP OBJECTIVE

Demonstrate that a **thermoelectric (TEC) cold plate**, when properly powered, controlled, and protected, can:

1. Condense water from air
2. Reduce RH in sealed enclosures
3. Operate without uncontrolled icing
4. Scale from **~20 L → ~100 L → ~200 L** chambers

This MVP exists to answer:

> *“Does TEC-based dehumidification work reliably for my cabinet volumes, and at what power level?”*

---

## 2️⃣ TARGET TEST VOLUMES

| Stage   | Volume                   | Purpose                     |
| ------- | ------------------------ | --------------------------- |
| Stage 1 | ~20 L sealed plastic box | First proof of condensation |
| Stage 2 | ~100 L sealed enclosure  | Cycling & stability         |
| Stage 3 | ~200 L sealed enclosure  | Upper practical bound       |

All test chambers **must be airtight** (tape/seal as needed).

---

## 3️⃣ COOLING HARDWARE (MVP ENGINE)

### 3.1 TEC Cooling Kit (Primary MVP Platform)

**Model:** XD-6038
**Type:** Dual-TEC thermoelectric cooling kit

**Configuration:**

* **2 × TEC1-12710**
* Flat aluminum cold plate
* Dual heatpipe tower heatsinks
* **3 × DC cooling fans**

**Electrical Class:**

* Voltage: **12 V DC**
* Max current: **~20–25 A**
* Max electrical input: **~200–240 W**

**Hot Side:**

* Fully exposed to ambient air
* No enclosure during MVP

**Cold Side:**

* Cold plate protrudes into sealed chamber
* Perimeter sealed with closed-cell foam

---

## 4️⃣ CONTROL ARCHITECTURE (NO MCU)

### 4.1 Humidity Control

**Module:** XH-M452
**Function:**

* Measures RH and chamber temperature
* Relay closes when RH exceeds setpoint

**Sensor placement:**

* Mid-air inside chamber
* Away from cold plate and walls

---

### 4.2 Cold Plate Temperature Safety

**Module:** W1209
**Function:**

* Measures cold plate temperature
* Prevents icing via adjustable cutoff

**Sensor placement:**

* Directly attached to cold plate
* Thermal paste + tape/clamp

---

### 4.3 Power Switching

**Module:** DC MOSFET Power Module
**Rating:** **≥30 A**, **5–36 V DC**

**Function:**

* Switches TEC + fans ON/OFF
* Controlled by relay logic
* MOSFET switches **positive (+)** only

---

## 5️⃣ POWER DISTRIBUTION (FROZEN)

### 5.1 PSU (Main Power Source)

**Type:** Regulated DC Power Supply
**Output:** **12 V DC**
**Current rating:** **≥30 A** (recommended ≥40 A margin)

---

### 5.2 Fuse & Distribution (FROZEN)

**Component:** **DaierTek Fuse Box**
**Status:** 🔒 FROZEN

**Specs:**

* Voltage: **12–36 V DC**
* Total current: **100 A continuous**
* Per circuit: **30 A max**
* Fuse type: **ATO / ATC**
* Circuits: **6**
* Integrated **+ and − distribution**
* LED per circuit
* Marine-grade enclosure

---

## 6️⃣ FUSE ASSIGNMENT (LOCKED)

| Slot | Circuit                       | Fuse      |
| ---- | ----------------------------- | --------- |
| F1   | TEC + Fans (via MOSFET)       | **30 A**  |
| F2   | Controllers (XH-M452 + W1209) | **3–5 A** |
| F3   | Spare                         | 5–10 A    |
| F4   | Spare                         | 5–10 A    |
| F5   | Spare                         | 5–10 A    |
| F6   | Spare                         | 5–10 A    |

---

## 7️⃣ WIRE GAUGE SPECIFICATION

### PSU → DaierTek Fuse Box

* **4.0 mm²** (≈ AWG12) for **+**
* **4.0 mm²** (≈ AWG12) for **−**

### TEC + Fans Branch

* **2.5–4.0 mm²** (AWG14–12)

### Fan sub-branches

* **1.0–1.5 mm²** (AWG18–16)

### Control & logic wiring

* **0.5–0.75 mm²** (AWG20–18)

---

## 8️⃣ ELECTRICAL LOGIC (LOCKED)

```
TEC + FANS ENABLED =
   (RH > setpoint)
AND
   (Cold plate temperature > cutoff)
```

* XH-M452 provides **RH demand**
* W1209 provides **anti-ice safety**
* MOSFET enforces high-current switching

Fans are powered **in parallel with TEC** and always run when TEC is ON.

---

## 9️⃣ OPERATING MODES

### 9.1 1-TEC Mode (Recommended First)

* One TEC disconnected (both + and − insulated)
* Lower power
* Easier tuning
* Best for 20 L and early 100 L tests

### 9.2 2-TEC Mode

* Both TECs connected
* Higher power
* Faster dehumidification
* Higher icing risk if cutoff too low

---

## 🔟 INITIAL CONTROLLER SETTINGS

### W1209 (Cold Plate)

* Mode: Cooling
* Setpoint: **8 °C**
* Hysteresis: **3 °C**
* Raise to 10–12 °C if icing occurs

### XH-M452 (RH)

* Target RH: **55%**
* Hysteresis: ~5%

---

## 1️⃣1️⃣ MECHANICAL MVP SETUP

* Cold plate protrudes into chamber
* Perimeter sealed with closed-cell foam
* Hot side fully open to air
* Simple drip tray or gutter under cold plate
* Hose to external container optional

---

## 1️⃣2️⃣ TEST PLAN

### Test 0 — Dry Electronics Test

* No TEC connected
* Verify relays, MOSFET, fans

### Test 1 — 20 L Chamber

* Observe condensation
* Confirm RH drop

### Test 2 — Anti-Ice Tuning

* Adjust W1209 cutoff

### Test 3 — 100 L Chamber

* Observe cycling & stability

### Test 4 — 200 L Chamber

* Evaluate upper limits

---

## 1️⃣3️⃣ DATA TO RECORD

* Starting RH
* Lowest RH achieved
* Time to plateau
* Condensation type (drip vs ice)
* Hot-side thermal behavior
* Duty cycle

---

## 1️⃣4️⃣ SHOPPING LIST (MVP)

### Core

* XD-6038 TEC cooling kit
* 12 V ≥30 A DC PSU
* **DaierTek Fuse Box (6-way, 100 A / 30 A per circuit)**

### Control

* XH-M452 humidity controller
* W1209 temperature controller
* DC MOSFET power module ≥30 A

### Protection

* ATO/ATC blade fuses:

  * 30 A (TEC)
  * 3–5 A (controllers)
  * 5–10 A (spares)

### Wiring & Hardware

* AWG12 / AWG14 / AWG18 wire
* Ring/fork terminals
* Heatshrink
* Thermal paste
* Closed-cell foam

---

## 1️⃣5️⃣ MVP SUCCESS CRITERIA

✔ RH reliably drops below setpoint
✔ Water physically removed
✔ No uncontrolled icing
✔ Stable multi-hour operation
✔ Scaling behavior understood

---

## 1️⃣6️⃣ STATUS

* 🔒 Electrical architecture **FROZEN**
* 🔒 DaierTek Fuse Box **FROZEN**
* 🔒 MVP spec **LOCKED**
* 🔁 Ready for build and testing

---

### Suggested reuse line

> *“This document defines the frozen MVP specification for a TEC-based dehumidifier used to validate condensation, RH control, and scaling behavior prior to final cabinet design.”*

---

If you want next, I can:

* regenerate **final wiring SVG using DaierTek**
* create a **one-page build checklist**
* or convert this into a **final product sizing guide** once MVP data comes in
