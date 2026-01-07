Below is the **fully regenerated, export-ready MASTER GEOMETRY DOCUMENT**, now **including the Dehumidifying Module as a FROZEN interface standard**.

This is a **single authoritative document**.
You can save, export, and reuse it without having to re-explain anything later.

---

# 📘 CAMERA CABINET DEHUMIDIFIER

## MASTER GEOMETRY & AIRFLOW SPECIFICATION

**Status:** **FROZEN**

*(Thermal sizing, mechanical detailing, and electrical design will reference this document but must not redefine its geometry or interfaces.)*

---

## 1. Objective

Design a **silent, robust, serviceable dehumidified display cabinet** for photographic cameras, with:

* Uniform humidity and temperature (mixing-first)
* Effective dehumidification at a cold surface or membrane (local wash)
* No reliance on fragile airflow loops
* Modular, replaceable dehumidification technology
* Long-term serviceability without cabinet rebuild

---

## 2. Cabinet Internal Geometry (Fixed)

### Internal dimensions

* **Width:** 1974 mm (left → right)
* **Depth:** 317 mm (back wall → glass door)
* **Height:** 514 mm (bottom → top)

### Internal boundaries

* Left wall
* **Right wall** (hosts dehumidifying module interface)
* Back wall
* Front wall (glass door)
* Top
* Bottom

The cabinet is **sealed** (no intentional air exchange with room air).

---

## 3. Shelves & Camera Layout (Fixed)

### Camera rows

* **Three rows**

  1. Bottom row (cabinet floor)
  2. Lower glass shelf
  3. Upper glass shelf

### Glass shelves

* Quantity: **2**
* Thickness: **6 mm**

**Lower shelf**

* Bottom: **211 mm**
* Top: **217 mm**

**Upper shelf**

* Bottom: **359 mm**
* Top: **365 mm**

### Shelf plan dimensions

* **Width:** 1774 mm (100 mm gap each side)
* **Depth:** 267 mm (fixed to back wall, **50 mm gap to door**)

### Camera placement constraints

* ~30–35 cameras total
* No enclosed boxes
* Maintain clearance:

  * ~100 mm from right wall (drip / module zone)
  * gap behind cameras to back wall
* Cameras kept out of drip zone below dehumidifying surface

---

## 4. Plenum Decision (Fixed)

* **NO PLENUM**
* Dehumidifying surface exposed directly to chamber air

---

## 5. Airflow Strategy (Fixed)

* **Mixing-first + local wash**
* Robust against uncertainty
* No guaranteed circulation loop assumed

---

## 6. Fans (Fixed)

### Fan type

* **120 mm Noctua**, low RPM, PWM

### Fan count

* **Two fans**

**Fan 1 — Mixing**

* Location: bottom-left
* Direction: **UP**
* Role: bulk mixing

**Fan 2 — Local wash**

* Drives air **parallel to dehumidifying surface**

Primary:

* Bottom-right, **below surface**, **UP**

Alternative:

* Top-right, **above surface**, **DOWN**
* Requires drip shielding

---

## 7. Return Path Requirements (Fixed)

Must preserve:

* 50 mm front gap to door
* 100 mm side gaps at shelves
* gaps behind cameras
* clearance under shelves and bottom-row cameras

---

## 8. Dehumidifying Surface Placement (Provisional, Airflow-Locked)

* **Wall:** right wall
* **Vertical center:** 288 mm above bottom
* **Depth center:** 140 mm from back wall
* Size and technology: **defined per module option**

---

## 9. Condensation Handling (Geometry Only)

* Free drips possible
* Drain system mandatory
* Drain belongs to the **dehumidifying module**
* External container used

---

## 10. Explicit Non-Assumptions

This design does **not** assume:

* symmetric flow
* single circulation loop
* CFD-level predictability

---

## 11. Geometry Status

* Cabinet geometry: **FROZEN**
* Airflow concept: **FROZEN**
* Fan placement: **FROZEN**
* Dehumidifying interface: **FROZEN**
* Thermal sizing: **DEFERRED**
* Mechanical detailing: **DEFERRED**
* Electrical detailing: **DEFERRED**

---

# 📎 Appendix A — System Context

### Thermal concepts (options, not sized here)

* TEC-based cold plate systems
* Membrane-based systems (Rosahl)

### Hot-side heat rejection

* External to cabinet
* Air or liquid cooled, depending on option

### Control

* ESP32-based
* Sensors + PWM control

---

# 📎 Appendix B — Splash / Visual Shield (Optional)

* Flat rigid plastic plane, **1–2 mm**
* Positioned **50 mm** from right wall
* Fully open on all sides
* Extends **40 mm** beyond dehumidifying surface
* Wash airflow must pass through this gap

---

# 📎 Appendix C — Cabinet Construction & Materials

### Internal shell

* Moisture Resistant MDF (Ultra MDF / green)
* Thickness:

  * Left, Right, Top, Bottom: **18 mm**
  * Back wall: **15 mm**
* Finish: **off-white PU automotive gloss**

### External cladding

* **25 mm melamine MDF**
* Wood-pattern finish
* Edge trimmed
* Glued + screwed to internal shell
* Forms **monolithic structure**
* No airflow paths between layers

---

# 📎 Appendix D — Door, Seal & Latching (Generic Guidance)

### Door

* 8 mm tempered glass
* 30 mm black anodized aluminum frame
* Top-hinged
* Opens upward ~110°, closes downward

### Seal

* Face seal
* EPDM closed-cell foam **or** magnetic gasket
* Bonded to painted MDF front border
* Continuous loop
* Target compression: 25–40%

### Bottom retention

* Required for seal compression
* No visible clamps
* Allowed solutions:

  * concealed cam latches
  * push-to-lock compression latches
  * hidden museum-style latches
  * magnetic gasket + discreet assist
* Final choice with cabinet maker

---

# 📎 Appendix E — Dehumidifying Module (FROZEN INTERFACE STANDARD)

## E1. Purpose

Allow **multiple dehumidification technologies** to be installed, tested, and replaced **without cabinet rebuild**.

---

## E2. Thermal Options (Referenced Later)

* **Option 1:**
  1× copper cold plate + 1× 40×40 TEC + hot spreader, **liquid cooled**

* **Option 2:**
  1× copper cold plate + 1× 40×40 TEC + hot spreader, **1× NH-C14S air cooled**

* **Option 3:**
  1× larger copper plate + 2× 40×40 TEC + hot spreader, **2× NH-C14S air cooled**

* **Option 4:**
  Rosahl **M-5J1R** membrane dehumidifier

* **Option 5:**
  Rosahl **M-5J1R** membrane dehumidifier (alternate integration)

---

## E3. Module Holder (Fixed)

* Material: 15 mm moisture-resistant MDF
* Finish: off-white PU automotive gloss
* Size: **213 mm (depth) × 370 mm (height)**
* Hosts and supports the dehumidifying unit
* Has a **cutout exposing the active element directly to chamber air**
* Active element protrudes **~2 mm or more** into chamber (exact value later)

---

## E4. Internal Cutout (Fixed)

* Location: internal right wall
* Size: **217 mm (depth) × 374 mm (height)**
* Through full wall thickness
* Centered horizontally and vertically
* Holder fits with **2 mm clearance on each edge**

---

## E5. External Cutout (Fixed)

* Location: external right wall (25 mm MDF)
* Size: **137 mm (depth) × 314 mm (height)**
* Through full thickness
* Centered in both axes
* Used for:

  * airflow (Options 4 & 5)
  * heatsink clearance (Options 2 & 3)
  * liquid cooling routing (Option 1)

---

## E6. Sealing Interface (Fixed)

* Closed-cell silicone foam gasket, **3–4 mm**
* Located between holder and external wall
* Defines **air and thermal boundary**
* **Consumable** (replaced on each module swap)

---

## E7. Mounting Method (Fixed)

* 4× M4 flat-head screws
* Pass through:

  * holder
  * gasket
  * external wall
* Secured with nuts + coil springs
* Function: **sealing pressure only**
* Heatsink weight handled by **separate support structure**

---

## E8. Drain Interface (Fixed at Concept Level)

* Gutter is **integrated into the module**
* Drain passes through holder to external side
* Hose leads to container
* Detailed design deferred

---

## E9. Electrical Interface (Intent Fixed)

* **Single standardized connector** per module
* Power + signals
* Connector type and pinout deferred to Electrical Design

---

## E10. Alignment & Serviceability

* Alignment: **screw-based centering only**
* Module replacement:

  * door open
  * shelves may be removed
* Module swaps are **infrequent**, convenience not optimized

---

## E11. Standardization Rule

* **One single holder + cutout standard** for all options
* What varies:

  * how each dehumidifying unit attaches to the holder
* Everything is **centered** relative to internal right wall

---

## NEXT STEP

Proceed to **Thermal Design**, using this document as the **non-negotiable geometric baseline**.

Suggested opening line:

> *“We have a fully frozen Master Geometry & Airflow specification including the Dehumidifying Module standard. Let us now dimension the thermal system.”*

---

If you want, I can:

* convert this into **PDF-ready Markdown**
* generate **dimensioned sketches**
* extract a **one-page interface spec** for suppliers
