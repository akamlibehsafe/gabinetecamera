Understood. Below is a **clean, complete, freeze-ready Mechanical & Clamping Specification**, written so you can **save it as a standalone MD** and load it together with Geometry and Thermal in the next chat.

I have **not invented anything new** — this strictly consolidates and formalizes what is already agreed.

---

# 📘 MECHANICAL & CLAMPING SPECIFICATION

## Dehumidifying Module — v3.3.1 (FROZEN)

---

## 1. Scope and Status

This document defines the **Mechanical and Clamping specification** of the **Dehumidifying Module**, as installed in the cabinet right wall.

* Geometry & Airflow: **FROZEN (external reference)**
* Thermal Design: **FROZEN (external reference)**
* Electrical & Control: **OUT OF SCOPE**
* This document is **freeze-ready** and intended for archival and reuse.

---

## 2. Terminology (Authoritative)

The following terminology is **mandatory and exclusive**.

### 2.1 Dehumidifying Module

The **complete removable assembly** that mounts into the cabinet, composed of:

* Dehumidifying Module Holder
* Dehumidifying Module Gasket
* Dehumidifying Module Mounting Screws
* Dehumidifying Unit (functional device)

The Dehumidifying Module is designed to be **fully removable and replaceable** without cabinet reconstruction.

---

### 2.2 Dehumidifying Module Holder

A structural plate that:

* Mounts into the internal wall cutout
* Carries the Dehumidifying Unit
* Provides the vent opening (if applicable)
* Transmits sealing force to the gasket

**Material & Finish**

* 15 mm humidity-resistant MDF
* Painted with PU automotive paint, off-white glossy
* Same finish as internal cabinet panels

**Dimensions**

* 213 mm — depth (back → front)
* 370 mm — height (bottom → top)

---

### 2.3 Dehumidifying Module Internal Cutout

Cutout on the **internal right wall** (18 mm MR MDF).

**Dimensions**

* 217 mm — depth
* 374 mm — height

**Properties**

* Passes through entire wall thickness
* Centered in both directions
* Provides **2 mm clearance per side** to the Holder

---

### 2.4 Dehumidifying Module External Cutout

Cutout on the **external right wall** (25 mm MDF).

**Dimensions**

* 137 mm — depth
* 314 mm — height

**Properties**

* Passes through entire wall thickness
* Centered in both directions
* Creates the overlap region required for sealing

---

### 2.5 Dehumidifying Module Gasket

A closed-cell compressible gasket placed in the overlap region between:

* Dehumidifying Module Holder
* External cabinet wall

**Function**

* Airtight sealing
* Long-term compression stability

**Thickness**

* Nominal: **3–4 mm**

**Material (by Thermal Option)**

* **Options 1–3 (TEC-based):** closed-cell silicone foam
* **Options 4–5 (Rosahl-based):** closed-cell **EPDM foam** (non-silicone)

---

### 2.6 Dehumidifying Module Mounting Screws

Fasteners whose **sole function is sealing compression**.

**Specification**

* Quantity: 4
* Type: M4
* Head: flat / countersunk (internal face)
* Pass through:

  * Holder
  * Gasket
  * External wall
* Secured with:

  * Nuts
  * Coil springs

**Design Rule**

* Screws are **not structural**
* They do **not** carry:

  * heatsink weight
  * dehumidifying unit mass
* They only provide controlled gasket compression

---

### 2.7 Dehumidifying Unit

The **functional moisture-removal device** mounted to the Holder.

Examples:

* TEC-based stack (Options 1–3)
* Rosahl M-5J1R (Option 4)
* Rosahl M-7J1R (Option 5)

The Dehumidifying Unit:

* Is fixed to the Holder
* Can be replaced independently
* Uses manufacturer-specified mounting hardware

---

## 3. Mechanical Architecture (General)

### 3.1 Removability

* The entire Dehumidifying Module can be removed by:

  1. Releasing the 4 mounting screws
  2. Pulling the Holder inward
* No cabinet panels require modification
* No wiring or sensors are mechanically integrated into the Module

---

### 3.2 Load Paths

* **Sealing loads:** carried by the 4 M4 screws and springs
* **Device weight loads:** carried by:

  * Holder structure
  * Separate mechanical supports (if required by thermal option)
* No load stacking is permitted on the sealing screws

---

## 4. Thermal Option Applicability

### 4.1 Options 1 & 2 (TEC — Single Module)

* Use identical mechanical and clamping architecture
* Differences are thermal only
* Cold-side and hot-side stacks mount to the Holder
* Gasket material: **silicone foam**

---

### 4.2 Option 3 (TEC — Dual Module)

* Same clamping architecture as Option 2
* Larger plates and envelopes (per Thermal Spec)
* Two TEC zones
* Gasket material: **silicone foam**
* Mechanical scalability is guaranteed by Holder envelope

---

### 4.3 Option 4 (Rosahl M-5J1R)

* Dehumidifying Unit mounts directly to Holder
* Vent opening:

  * **55 × 55 mm**
  * Centered on Holder
* Gasket material: **EPDM closed-cell foam**
* No condensate handling required

---

### 4.4 Option 5 (Rosahl M-7J1R)

* Same mechanical concept as Option 4
* Vent opening:

  * **75 × 75 mm**
  * Centered on Holder
* Separate Holder variant allowed
* Gasket material: **EPDM closed-cell foam**

---

## 5. Chemical Compatibility Constraints (Options 4–5)

For Rosahl-based options, the following are **strictly prohibited** in contact with airflow paths:

* Silicone sealants or foams
* Siloxanes
* Oils or oil mist
* VCIs (vapor corrosion inhibitors)
* Amines
* Chlorinated solvents

Approved:

* EPDM gasket
* PU automotive paint
* MDF substrates

---

## 6. Intentional Exclusions

This specification does **not** define:

* Electrical wiring
* Control logic
* Sensor count or placement
* Screw torque values
* CAD-level hole patterns

These are addressed in other phases.

---

## 7. Freeze Declaration

This Mechanical & Clamping specification is:

* Internally consistent
* Aligned with Geometry & Thermal specs
* Ready for archival
* Intended as immutable input for subsequent phases

**Status: FROZEN**

---

If you want, next I can:

* generate a **single consolidated ZIP-ready MD** (Geometry + Thermal + Mechanical), or
* proceed directly to **Electrical & Control** with this as locked context.
