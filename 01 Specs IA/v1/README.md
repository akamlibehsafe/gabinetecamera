Below is the **Frozen Design Spec – v1.0** in **English**, formatted as a clean **Markdown document** you can save and reuse. This freezes all major choices we agreed on and clearly marks the remaining open items.

---

# Custom Dry Cabinet – Frozen Design Spec (v1.0)

**Project goal:**
Permanent-display dry cabinet for a camera collection, furniture-grade appearance, ultra-quiet operation, controlled RH (~45%), and high reliability.

---

## 1. Cabinet Overview

* **External form:** Horizontal furniture piece
* **Internal free height (camera chamber):** **500 mm**
* **Depth:** ~300 mm
* **Door:** Single glass door with aluminum frame and perimeter gasket
* **Internal finish:** Ultra MDF painted with automotive PU
* **External finish:** Wood veneer / solid wood panels
* **Panel thickness:**

  * Internal panels: **25 mm**
  * External panels: **25 mm**

---

## 2. Compartment Layout

### Camera Chamber

* **Shelving:**

  * **2 glass shelves** (3 display levels total)
* **Clearances for airflow:**

  * **Left side gap:** 100 mm (chimney)
  * **Right side gap (Wall A side):** 100 mm (chimney)
  * **Front gap (shelf → glass door):** 50 mm
* **Purpose:** uniform air circulation, display, RH sensing

### Right Tech Box (Hot Chamber)

* **Clear internal width:** **130 mm**
* **Height:** same as cabinet (≈480–500 mm clear)
* **Depth:** cabinet depth
* **Front access:** removable sealed service panel
* **Purpose:** TEC hot-side cooling, pump/reservoir, wiring, control electronics

---

## 3. Walls & Internal Architecture

### Wall B (Structural Partition)

* **Material:** MDF
* **Thickness:** **15 mm**
* Separates camera chamber from hot chamber
* Cold plate is mounted through Wall B opening

### Wall A (Cosmetic Airflow Screen)

* **Material:** Ultra MDF, PU painted
* **Role:**

  * hides cold plate edges, foam, condensation details
  * shapes airflow
  * blocks line-of-sight
* **Spacing:**

  * **Clear gap between Wall A and Wall B:** **40 mm nominal** (35–45 mm acceptable)
* **Slot:**

  * single vertical slot
  * width: **15–20 mm**
  * height: **300–380 mm**
* **Baffle (shadow reveal):**

  * MDF strip behind slot
  * thickness: 10–15 mm
  * offset from Wall A: 10–15 mm

---

## 4. Airflow Strategy

### Camera Chamber Airflow

* **Primary circulation fan:**

  * 120 mm Noctua
  * Mounted on **bottom panel**, inside **left-side 100 mm chimney**
  * Blowing **upward**
  * Slightly back-biased (≈80–100 mm from rear wall)
* **Operation:**

  * Runs **continuously** at very low RPM (≈300–500 RPM)
* **Flow pattern:**

  * Air rises on left
  * crosses shelves
  * descends on right (Wall A side)
  * exchanges through Wall A slot with cold-plate cavity
  * returns via front gap and shelf gaps

### Cold-Plate Cavity

* **Passive** (no fan)
* Air enters/exits through Wall A slot
* Slow airflow for efficient condensation

### Hot Chamber Airflow

* Radiator exhausts **directly to room**
* Intake separated vertically from exhaust

---

## 5. Cold Plate / TEC Assembly

### Cold Plate (Camera Side)

* **Material:** Copper C110
* **Dimensions:** **100 × 140 × 8 mm**
* Smooth, flat faces
* No holes

### TEC

* **Size:** 40 × 40 mm
* Thickness: ~4 mm
* Controlled ON/OFF by RH logic

### Hot-Side Spreader

* **Material:** Aluminum (6061 or similar)
* **Dimensions:** **120 × 160 × 10 mm**
* 4 through-holes outside TEC footprint for clamp rods

### Thermal Bypass Isolation

* **Material:** Closed-cell silicone foam
* **Thickness:** **4 mm**
* **Shape:** picture-frame gasket

  * inner opening: **42 × 42 mm**
  * outer size: **≈80 × 80 mm**
* Positioned around TEC between plates
* Compression target: ~10–20%

### Mechanical Clamping

* All clamp force carried by **metal rods + springs**
* No load carried by MDF or plastic
* 3D-printed parts allowed **only** as:

  * alignment frame
  * insulation
  * cosmetic cover
    (not load-bearing)

---

## 6. Cold Plate Positioning

* **Horizontal:** centered on Wall B
* **Vertical (500 mm free height):**

  * Cold plate centerline: **250 mm from bottom**
  * Bottom edge: **180 mm**
  * Top edge: **320 mm**

---

## 7. Hot Chamber Cooling (FINAL)

* **Cooling type:** Custom water-cooling loop
* **Radiator:** **240 mm**

  * Embedded into 25 + 25 mm side panel thickness
* **Fans:**

  * 2 × 120 mm Noctua
  * PWM controlled, low RPM
* **Pump/Reservoir:**

  * Compact combo unit
  * Mounted inside hot chamber
  * Vibration-isolated
* **Water block:**

  * Standard CPU block pressed against aluminum spreader

---

## 8. Electrical Architecture

### Power

* **Voltage:** 12 V DC system
* **PSU:** External AC → DC supply (brick or industrial PSU)
* **PSU location:** outside cabinet
* **DC inlet:** XT60 or GX16 connector into hot chamber

### Distribution

* **DC hub:** fused distribution block (automotive blade fuses)
* **Star topology** for all branches

### Typical Wire Gauges

* Main feed / TEC branch: **2.5 mm²** (4.0 mm² if TEC >12–15 A)
* Pump: **0.75–1.0 mm²**
* Fans: **0.5 mm²**
* Sensors/signals: **0.22–0.5 mm²**

---

## 9. Sensors & Control Logic

### Sensors

* **Primary RH sensor:** inside camera chamber

  * mid-height, mid-depth
  * away from cold plate and door
* **Temperature sensor:** bonded to aluminum spreader (hot side)

### Control Logic

* **Primary control:** RH-based

  * Target: **45% RH**
  * Hysteresis: **≈5%**
* **Safety cutoff:**

  * TEC OFF if spreader temperature ≥ **70–75 °C**
* **Fans & pump:**

  * Always ON when TEC is ON
  * Camera chamber fan runs continuously

### Switching

* TEC switched via **DC MOSFET module** (silent)
* Optional hardware thermal cutoff in series

### Tuya Integration

* **Role:** monitoring + manual override only
* Local wired control remains authoritative

---

## 10. Operating Targets

* **Camera chamber RH:** ~45%
* **Cold plate temperature:** typically 8–20 °C
* **TEC hot side (spreader):**

  * normal: 40–60 °C
  * cutoff: 70–75 °C
* **Noise goal:** inaudible in living room

---

## 11. Open Items (to be finalized later)

* Exact **TEC model & current**
* Exact **PSU amperage**
* Specific **controller / RH sensor models**
* Exact **pump/reservoir model**
* Final **fuse values**

---

**Status:**
This document defines the **frozen baseline** for geometry, airflow, thermal design, electrical architecture, and control philosophy. Future changes should be tracked as revisions.

---

If you want, next I can:

* export this as **README.md** and **CHANGELOG.md**
* create a **SketchUp dimension checklist**
* or start **Spec v1.1** once you lock the TEC and PSU models
