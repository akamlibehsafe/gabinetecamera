# 📙 CAMERA CABINET DEHUMIDIFIER

## MASTER THERMAL SPECIFICATION — OPTIONS **1–5**

**Status:** **FROZEN (options + key dimensions + interfaces)**
**Depends on:** *MASTER GEOMETRY & AIRFLOW SPECIFICATION (FROZEN)* incl. **Appendix E — Dehumidifying Module (Interface Standard / DMI)**

---

## 1) Design Basis Used for Thermal Calculations

* **Location:** Campinas–SP (Viracopos region)
* **Worst typical hot/humid season:** **Jan–Mar**
* **Room:** no A/C; sheltered from direct sun; dry/sound walls; no infiltrations
* **Cabinet free air volume:** **~0.4–0.45 m³**
* **Target internal environment:** **40–45% RH**, nominal **~25 °C**
* **Door opening worst case:** **1× per day**
* **Moisture load used for feasibility checks (order-of-magnitude):** **~3–5 g/day typical**, **≤10 g/day conservative**
* **Control intent:** dehumidify only when RH rises above target; rely on sealing to hold

---

## 2) Geometry Interface Dependency (DMI)

All Options **1–5** must mount into the **same Dehumidifying Module Interface (DMI)** defined in Geometry Appendix E, without furniture rebuild.

### 2.1 DMI fixed elements (from Geometry Appendix E)

* **Module holder:** 15 mm MR MDF, PU gloss; **213 mm (depth) × 370 mm (height)**
* **Internal cutout:** **217 mm (depth) × 374 mm (height)** through internal wall thickness
* **External cutout:** **137 mm (depth) × 314 mm (height)** through external wall thickness
* **Seal:** closed-cell silicone foam gasket **3–4 mm** (consumable)
* **Mounting for sealing only:** **4× M4** flat-head screws + nuts + coil springs
* **Heatsink weight:** carried by separate support structure (not by sealing screws)
* **Electrical intent:** one standardized connector per module (type/pinout deferred)

### 2.2 DMI anchor point (airflow-locked)

* The DMI is centered at the frozen anchor:

  * **Vertical center:** **288 mm above cabinet bottom**
  * **Depth center:** **140 mm from back wall**

### 2.3 Moisture handling rule (option-aware)

* **Options 1–3 (TEC / condensation):** module must include **gutter + drain** to external container
* **Options 4–5 (membrane):** **no internal condensation**, drain not required (may be capped/unused)

### 2.4 Fan ownership

* Mixing fan and wash fan are **part of cabinet geometry**, not part of the module.

---

## 3) Common Sensing & Control (interface-level)

* **RH sensing:** 3× RH+T sensors (left / middle / right); control uses **max(RH)**
* **Options 1–3:**

  * **Cold-side (plate) temperature sensor:** DS18B20 (or equivalent)
  * **Hot-side temperature sensor:** DS18B20 (or equivalent) — mandatory limiter
  * **TEC drive:** PWM via ESP + MOSFET (details deferred to Electrical spec)
* **Options 4–5:**

  * Prefer **long ON periods** (avoid rapid cycling); no cold-plate loop

---

# 4) THERMAL OPTIONS (FROZEN)

## **Option 1 — 1× TEC + Liquid Cooling (Hot Side)**

**Purpose:** quiet high hot-side rejection headroom via radiator loop.

### 4.1.1 Stack & key dimensions (FROZEN)

**All dimensions expressed as (Depth × Height × Thickness)** to match DMI cutout axes.

* **Copper cold plate:** **100 × 140 × 8 mm**
* **Aluminum hot spreader:** **120 × 160 × 10 mm**
* **TEC:** 1× (single TEC, centered on spreader/plate; exact model deferred)
* **Condensate handling:** gutter + drain integrated in module

### 4.1.2 Liquid loop spec (FROZEN baseline)

* **Hot-side dissipation target:** **~150 W continuous headroom** (quiet operation goal)
* **Radiator:** **240 mm minimum** (2×120), **~27 mm thick** slim
* **Fans:** PWM; controlled by ESP32 (quiet baseline + ramp with hot-side temperature)
* **Pump:** 12 V PWM pump; ESP32 PWM with **minimum safe duty**; **tach feedback recommended**
* **Water block:** compact PC-style block (copper base preferred)

  * Mounting via **blind drilled + tapped holes** in aluminum spreader (independent from TEC clamp)
* **Tubing/fittings:** ~10 mm ID class; G1/4 fittings; short runs, gentle bends
* **Coolant:** distilled water + inhibitor or premix; provide fill/bleed point (reservoir preferred)
* **Safety (FROZEN policy):**

  * hot-side high → fans/pump 100%
  * pump failure or overtemp → **TEC OFF**

### 4.1.3 Fixed BOM (vendor: PowerUpInfo + Noctua) — FROZEN

*(BOM item names in Portuguese as per vendor; Noctua fan model intentionally not fixed.)*

| Item                    | Qtde | Produto / descrição                                          | SKU                                |
| ----------------------- | ---: | ------------------------------------------------------------ | ---------------------------------- |
| Bomba                   |   01 | Freezemod PU-GTD5 1.100L/H RGB 5V 1/4                        | Bomda-D5-RGB                       |
| Radiador                |   01 | Radiador 240mm de Cobre Freezemod 27mm                       | 240mm-Cobre-Preto                  |
| Ventilador (radiador)   |   02 | Noctua 120mm PWM (modelo não especificado)                   | —                                  |
| Reservatório            |   01 | Reservatório 66mm Freezemod OD60mm com Kit Montagem          | Reservatorio_66mm_Freezemod_OD60mm |
| CPU Block               |   01 | Water Cooler CPU Block Freezemod Intel LGA 1700–1851         | CPUBlock-Freezemod-Reto-Intel      |
| Fitting 90°             |   01 | Fitting G1/4 Curva 90 Giratório PUWC                         | Fitting-90Graus                    |
| Fitting tampa           |   02 | Fitting G1/4 Tampa PUWC                                      | Fitting-Tampa                      |
| Fitting compression 3/8 |   06 | Fitting G1/4 para Mangueira 3/8 – Compression                | Fitting-Compression-38             |
| Mangueira               |   02 | Mangueira Transparente Siliconada 3/8 (1m/un)                | Mangueira-Transparente38           |
| Fluido                  |   01 | Fluido Liquid Water Cooler Power Up Hexa Pro Transparente 1L | Fluido-Transparente                |

---

## **Option 2 — 1× TEC + 1× NH-C14S (Air Hot Side)**

**Purpose:** simplest air-cooled TEC implementation using NH-C14S externally.

### 4.2.1 Stack & key dimensions (FROZEN)

* **Copper cold plate:** **100 × 140 × 8 mm**
* **Aluminum hot spreader:** **120 × 160 × 10 mm**
* **TEC:** 1× (single TEC; exact model deferred)
* **Hot-side cooler:** **1× Noctua NH-C14S**, outside cabinet
* **Condensate handling:** gutter + drain integrated in module

### 4.2.2 Hot-side acoustic policy (FROZEN)

* NH-C14S fan at **minimum RPM by default**
* Allow **brief boosts** or “as long as needed” to reach RH setpoint, but always bounded by hot-side temperature limiter

---

## **Option 3 — 2× TEC + 2× NH-C14S (Upgrade Path)**

**Purpose:** increase steady-state dehumidification capacity if Option 2 cannot hold RH on humid days.

### 4.3.1 Stack & key dimensions (FROZEN)

* **Copper cold plate:** **140 × 260 × 8 mm**
* **Aluminum hot spreader (overall envelope):** **160 × 280 × 10 mm**
* **Hot spreader split (FROZEN):** split the **280 mm height** into **two halves of 140 mm each**, yielding:

  * **Upper spreader half:** **160 × 140 × 10 mm**
  * **Lower spreader half:** **160 × 140 × 10 mm**
* **TECs (layout FROZEN):**

  * **2× TEC total**
  * **Each TEC centered** on its corresponding **160×140** spreader half (top half, bottom half)
* **Hot-side coolers:** **2× NH-C14S**, outside cabinet (default for Option 3)
* **Condensate handling:** gutter + drain integrated in module

*(Exact TEC-to-heatsink mechanical coupling and cartridge internals are deferred to the Cartridge/Clamping specification.)*

---

## **Option 4 — Rosahl M-5J1R (Membrane Dehumidifier)**

**Purpose:** near-silent humidity control without condensation, drains, or cold surfaces.

* **Mechanism:** electrolytic membrane moisture transport (active pump of vapor)
* **No cold plate / no TEC / no internal condensate / no drain**
* **Mounting requirement:** airtight mounting through DMI; discharge side must be well ventilated to external plenum
* **Control intent:** prefer **long ON periods** (avoid rapid cycling)
* **Chemical compatibility constraint (mandatory):** avoid silicone/siloxane/VCI/oil/amine vapor exposure near membrane (document as user warning)

---

## **Option 5 — Rosahl M-5J1R (Alternate Integration)**

Same device as Option 4; differs only in **mechanical/venting implementation inside the same DMI envelope** (to be defined later). Must preserve:

* airtight sealing at DMI
* ventilated discharge side
* chemical constraints
* no internal condensation / no drain

---

## 5) Deferred Items (Not part of this frozen thermal option spec)

* Exact TEC part numbers and electrical ratings
* Absolute hot-side overtemp threshold value
* TEC control tuning (duty limits, boost rules, hysteresis)
* Detailed Dehumidifying Module cartridge implementation (bolt pattern details, gasket type, service procedure)
* Detailed clamping/pressure system (handled in dedicated clamping work)
* Full electrical wiring diagram, PSU selection, and safety circuits (handled in Electrical spec)

---

**END — MASTER THERMAL SPEC (Options 1–5, frozen)**
