# Laminar Flow Hood v1: OpenSCAD Build Spec

**For:** the Claude project with OpenSCAD MCP access (Windows)
**Printer:** Elegoo Centauri Carbon 2 (256 × 256 × 256 mm build volume, 0.4 mm nozzle)
**Material:** PLA (PLA+ fine) for everything except one TPU 95A gasket ring
**Status: FINAL, built from measured parts (31 Oct 2026).** Verified in the reference model (`lfh_v1_reference.scad`) at these exact dimensions: bed fit, zero interference, slide-together assembly path, wrong-assembly blocking, the bayonet twist path, and the visor fit and pull-off path all pass.

---

## 0. Instructions to the build project

1. Build **one parametric OpenSCAD file**. Every dimension comes from section 2, with nothing hard-coded. Derived values must be computed, not typed in.
2. Model every part **in the shared assembly frame** (section 1), then export each part through its **print-pose transform** (section 7) as its own STL.
3. Deliverables:
   - one STL per part, named as in section 6
   - one assembly preview, PNG or `.scad` assembly mode
   - an `echo()` line listing all derived values
4. Run the **acceptance checks** in section 9 and report the results.
5. `lfh_v1_reference.scad` is a working reference implementation of this spec, and you can adopt or rewrite it. **Where it and this document disagree, this document wins.**
6. Units are mm and degrees. OpenSCAD 2021.01+ (the reference uses `rotate_extrude(angle=)` and `offset()`).

---

## 1. Coordinate frame and naming

| Axis | Direction |
|---|---|
| **X** | Right, as viewed by the operator standing in front of the filter |
| **Y** | Depth. **Y = 0 is the gasket face** (front face of the box flange), and +Y runs towards the back |
| **Z** | Up |
| Origin | Centre of the filter opening on the gasket face |

**Quarter numbering** (always as viewed **from the front**, clockwise):
`1 = top-left, 2 = top-right, 3 = bottom-right, 4 = bottom-left`

The same numbering applies to the box (**Q**), back (**B**) and clamp frame (**C**). B1 sits directly behind Q1, so viewed from behind B1 is on the top-right. That's expected.

**Seams** (split planes):

| Seam | Plane | Between |
|---|---|---|
| Top | x = 0, z > 0 | piece 1 ↔ 2 |
| Right | z = 0, x > 0 | piece 2 ↔ 3 |
| Bottom | x = 0, z < 0 | piece 3 ↔ 4 |
| Left | z = 0, x < 0 | piece 4 ↔ 1 |

---

## 2. Parameters

### 2.1 Measured values (Joe's parts, 31 Oct 2026)

| Name | Value | What it is |
|---|---|---|
| `FILTER_W` × `FILTER_H` | **339 × 291** | HEPA cardboard frame face, landscape (W horizontal) |
| `FILTER_FOAM` | **2** | Soft foam wrapped round the frame's **edges** (not on a face), each side. Over the foam: **343 × 295** |
| `FILTER_T` | **22** | Design thickness. The cardboard frame measures 22–25, so the design uses the thin end: a leak would start at the thin spots |
| `FILTER_T_MAX` | 25 | Thickest measured point. The gasket must still seal there (assert) |
| `FILTER_BORDER` | **10.8** | Flat frame border on the fibrous face, narrowest side |
| `FAN_OD` = `FAN_END_OD` | **148.1** | Fan body diameter, the same end to end (465 mm circumference, confirmed with calipers) |
| `FAN_LEN` | **150** | |
| `GLAND_FROM_INTAKE` | **52** | 98 from the outlet end |
| `GLAND_D` | **11.5** | Including the rubber boot |

The fan mounts **intake up** and blows down into the box. The gland sits 52 mm below the intake end, clear of both the socket (bottom 34 mm) and the bell sleeve (top 30 mm), so **neither part gets a gland notch**.

### 2.2 Fixed design parameters

| Name | Value | Meaning |
|---|---|---|
| `DEPTH` | 230 | Overall box depth (gasket face to back outer face) |
| `WALL` | 3 | Box wall thickness |
| `BACK_T` | 3 | Back plate thickness |
| `FLANGE_T` | 6 | Front flange thickness |
| `FLANGE_EXT` | 15 | Flange (and clamp) outer edge beyond the filter's **over-foam** edge |
| `FILTER_TOL` | 0.5 | Clearance between the **edge foam** and the clamp wall, per side. The walls just kiss the foam, which centres the filter on the gasket |
| `CLAMP_PLATE` | 4 | Clamp front plate thickness |
| `GASKET_W` / `GASKET_T` | **10 / 8** | Self-adhesive EPDM strip, width / uncompressed thickness |
| `GASKET_C` | **6.5** | Strip height at `FILTER_T` (19% squeeze). At `FILTER_T_MAX` it's 3.5 (56%) |
| `CH_D` / `CH_W` / `CH_R` | 1.0 / `GASKET_W + 0.5` / 8 | Gasket channel depth / width / centreline corner radius |
| `RIB_D` / `RIB_HW` / `RIB_STOP` | 7 / 6 / 10 | Internal seam rib depth / half-width / distance it stops short of the rear end |
| `BOSS_D` / `BOSS_H` | 12 / 6 | Bolt boss diameter / height on the flange rear |
| `BOLT_HOLE` | 4.4 | M4 clearance hole |
| `NUT_AF` / `NUT_DEPTH` | 7.3 / 3.7 | M4 nut pocket across flats / depth |
| `CB_D` / `CB_DEPTH` | 7.6 / 3 | Bolt-head counterbore in the clamp front |
| `CLR` | 0.15 | Sliding dovetail clearance **per face** |
| `JIG_CLR` | 0.2 | Back-plate jigsaw clearance per face |
| `RIDGE_T` / `RIDGE_H` / `RIDGE_CLR` | 2.5 / 6 / 0.2 | Back-plate U-channel ridge thickness / height / clearance to the wall |
| `SOCK_CLEAR` | 0.5 | Socket bore diametral clearance over `FAN_OD` |
| `SOCK_WALL` / `SOCK_H` | 3 / 40 | Socket wall / total height |
| `SOCK_FL_D` / `SOCK_FL_T` | 210 / 4 | Socket base flange diameter / thickness |
| `LEDGE_W` | 4 | Fan ledge width (radial, inside the socket) |
| `RING_T` | 2 | TPU ring thickness |
| `FOOT_W` / `FOOT_L` / `FOOT_INSET` | 30 / 40 / 20 | Rear foot width / contact length / inset from the side |
| `BELL_MOUTH_ID` | 220 | Intake bell mouth inner diameter |
| `BELL_WALL` | 2.5 | Bell wall thickness |
| `BAND_H` / `CONE_H` / `SLEEVE_L` | 12 / 40 / 30 | Bell rim band / cone / sleeve heights |
| `GRID_PITCH` / `GRID_BAR` / `GRID_T` | 15 / 2 / 2 | Bell mouth support grid |
| `LID_CLR` / `LID_WALL` / `LID_PLATE` | 0.3 / 2.4 / 2.4 | Lid radial clearance / skirt wall / grille plate |
| `PRESS_H` / `DISC_CLAMP` / `SKIRT_DOWN` | **7** / 3 / 8 | Lid pressing-ring height / disc edge clamped thickness / skirt reach below the mouth. `PRESS_H` 7 leaves 10 mm over the grid, so the 10 mm floss keeps its loft |
| `LUG_W` / `LUG_R` / `LUG_H` | 8 / 1.5 / 2.5 | Bayonet lug width / radial depth / height |
| `SLOT_W` / `SLOT_DEPTH` / `ENTRY_H` / `RUN_ANG` | 9 / 1.8 / 6 / 20 | Bayonet entry slot width / radial depth / height, and run angle |
| `VISOR_REACH` | 150 | How far the visor canopy projects in front of the clamp front face |
| `VISOR_T` | 2.4 | Canopy and wing thickness |
| `VISOR_LIP` | 20 | Canopy overlap resting on top of the clamp frame (carries the visor's weight) |
| `WING_END_Z` | 0 | Height where the side wings taper to nothing (0 = half-way down the box) |
| `STRIP_T` | 4.2 | Visor mounting strip thickness |
| `FRONT_RIB_H` | 10 | Stiffening rib under the canopy's front edge |
| `MAG_D` / `MAG_T` | 6 / 3 | Disc magnet diameter / thickness |
| `MAG_POCKET_D` / `MAG_POCKET_DEPTH` | 6.3 / 3.1 | Magnet pocket (magnet sits 0.1 below the face) |
| `HEAD_H` | 4.0 | M4 socket-cap head height (sits 1 mm proud of the clamp face) |
| `HEAD_CLR_D` / `HEAD_CLR_DEPTH` | 8.6 / 1.4 | Bolt-head pockets in the visor strip; they also locate the visor |

### 2.3 Derived (compute; values are for the measured parts)

| Name | Formula | Value |
|---|---|---|
| `FILTER_WO`, `FILTER_HO` | `FILTER_W + 2·FILTER_FOAM`, `FILTER_H + 2·FILTER_FOAM` (over the edge foam) | 343, 295 |
| `W_i`, `H_i` | `FILTER_W − 2·FILTER_BORDER`, `FILTER_H − 2·FILTER_BORDER` (internal opening, flush with the frame's inner edge) | 317.4, 269.4 |
| `W_o`, `H_o` | `W_i + 2·WALL`, `H_i + 2·WALL` | 323.4, 275.4 |
| `FL_W`, `FL_H` | `FILTER_WO + 2·FLANGE_EXT`, `FILTER_HO + 2·FLANGE_EXT` | 373, 325 |
| `TUBE_L` | `DEPTH − BACK_T` | 227 |
| `FILTER_BACK_Y` | `−(GASKET_C − CH_D)` (filter back face position) | −5.5 |
| `CLAMP_DEPTH` | `CLAMP_PLATE + FILTER_T + (GASKET_C − CH_D)` | 31.5 |
| `CLAMP_WALL` | `FLANGE_EXT − FILTER_TOL` | 14.5 |
| `BX`, `BZ` | `FILTER_WO/2 + FILTER_TOL + CLAMP_WALL/2`, `FILTER_HO/2 + FILTER_TOL + CLAMP_WALL/2` | 179.25, 155.25 |
| `GC_X`, `GC_Z` | `FILTER_W/2 − GASKET_W/2`, `FILTER_H/2 − GASKET_W/2` (gasket centreline: strip's outer edge flush with the cardboard edge, 0.8 clear of the pleats) | 164.5, 140.5 |
| `BAND_W` | `WALL + RIB_D` | 10 |
| `Y_F` | `TUBE_L/2` (fan centre, depth) | 113.5 |
| `FAN_HOLE_D` | `FAN_END_OD − 4` | 144.1 |
| `SOCK_ID` | `FAN_OD + SOCK_CLEAR` | 148.6 |
| `LEDGE_ID` | `FAN_END_OD − 2·LEDGE_W` | 140.1 |
| `FOOT_H` | `FL_H/2 − H_o/2` | 24.8 |
| `FOOT_END` | `TUBE_L − RIDGE_H − 1` | 220 |
| `W_b`, `H_b` | `W_o + 2·(RIDGE_CLR + RIDGE_T)`, `H_o + 2·(RIDGE_CLR + RIDGE_T)` | 328.8, 280.8 |
| `SLEEVE_ID` | `FAN_OD + 0.4` | 148.5 |
| `STOP_ID` | `FAN_OD − 4` | 144.1 |
| `BELL_RIM_OD` | `BELL_MOUTH_ID + 6` | 226 |
| `LID_SKIRT_ID` | `BELL_RIM_OD + 2·LID_CLR` | 226.6 |
| `LID_OD` | `LID_SKIRT_ID + 2·LID_WALL` | 231.4 |
| `DISC_D` | `BELL_RIM_OD − 2` (pre-filter disc diameter) | 224 |
| `WIN_W`, `WIN_H` | `FILTER_W − 2·(FILTER_BORDER − 2)`, `FILTER_H − 2·(FILTER_BORDER − 2)` (clamp window; the lip covers 8.8 mm of cardboard border) | 321.4, 273.4 |
| `Y_CF` | `−CLAMP_DEPTH` (clamp front face) | −31.5 |

**Asserts**:
- `GASKET_W ≤ FILTER_BORDER − 0.5`
- `GASKET_C − (FILTER_T_MAX − FILTER_T) ≥ 3` (the strip still seals at the thickest point)
- `GC_X − CH_W/2 > W_i/2` (the channel stays outside the box opening)
- `Y_F − SOCK_FL_D/2 ≥ FLANGE_T + 1`
- `Y_F + SOCK_FL_D/2 ≤ TUBE_L − 2`
- every print-pose bounding box ≤ 250 × 250 × 250

---

## 3. Joint system (read this before modelling)

### 3.1 Ownership and size coding

- Each piece **owns the tongue on its clockwise seam** and **receives on its anticlockwise seam**: piece 1 owns Top, 2 owns Right, 3 owns Bottom, 4 owns Left.
- **Size code:** Top and Right seams = **S**; Bottom and Left seams = **L**.
- Result: pieces 1 and 3 (and 2 and 4) are congruent under a 180° rotation about Y, but any swap forces an L tongue into an S slot and physically clashes. **The box, back and clamp can each only go together one way.** (Verified in the reference: any wrong arrangement needs at least one placement that clashes, by 116–620 mm³.)

### 3.2 Profiles (2D, in the plane perpendicular to the slide axis)

Local 2D frame: `u` = pointing direction (out of the owner, into the receiver), `v` = across the band. The tongue starts at the seam plane (`u = 0`).

**Dovetail** `[neck, head, length]`: polygon `[(0, −neck/2), (length, −head/2), (length, head/2), (0, neck/2)]`

| Use | S | L |
|---|---|---|
| Box wall seams (`DT_WALL`) | 3.0 / 5.0 / 4 | 4.0 / 6.0 / 4 |
| Box flange seams and clamp seams (`DT_FLNG`) | 4.0 / 6.0 / 4 | 5.0 / 7.5 / 4 |

**Jigsaw knob** `[neck_w, head_d, neck_len]` (back plate only): a rectangle `neck_w` wide from `u = 0` to `u = neck_len`, plus a circle of `head_d` centred at `u = neck_len + head_d/2 − 0.5`.

| | S | L |
|---|---|---|
| Back knobs (`KNOB`) | 6 / 9 / 3 | 8 / 12 / 3 |

**Slot** = `offset(delta = CLR)` of the tongue profile (`JIG_CLR` for knobs), subtracted from the receiver only.

### 3.3 Slide axis and the open-slot rule

- Every joint slides along **Y**. With the reference face down on a flat bench, each piece is **lowered from above** and the bench is the end stop.
- **Box wall slots run the full tube length** (`Y = −1 … TUBE_L + 1`), open at both ends. Tongues run only `Y = 0 … TUBE_L − RIB_STOP`. This is required: the last piece (Q4) engages two seams moving in the same direction (verified).
- Flange slots go through the full flange thickness. Clamp slots go through the full clamp depth.

### 3.4 Joint positions

| Seam | Box wall tongue centre | Box flange tongue centre | Clamp tongue centre | Points (u) | Size |
|---|---|---|---|---|---|
| Top (1→2) | (x=0, z=`H_o/2 − BAND_W/2` = 132.7) | (0, `FL_H/2 − 7` = 155.5) | (0, `BZ`) | +X | S |
| Right (2→3) | (`W_o/2 − BAND_W/2` = 156.7, 0) | (`FL_W/2 − 7` = 179.5, 0) | (`BX`, 0) | −Z | S |
| Bottom (3→4) | (0, −132.7) | (0, −155.5) | (0, −`BZ`) | −X | L |
| Left (4→1) | (−156.7, 0) | (−179.5, 0) | (−`BX`, 0) | +Z | L |

**Back knobs:** 2 per seam segment, centred at

| Segment | Knob centres |
|---|---|
| Top segment (x=0) | z = **47, 94** |
| Right segment (z=0) | x = **55, 110** |
| Bottom segment | z = **−47, −94** |
| Left segment | x = **−55, −110** |

Same ownership and size rules as above. If the filter size changes, keep the knobs at roughly ⅓ and ⅔ of each segment and clear of the ridges.

---

## 4. Part geometry

### 4.1 Box quarters Q1–Q4 (P01–P04)

Build the full tube body, split it with quadrant clips, add the owned tongues, then subtract the cuts and the received slots.

**Tube body (assembly frame):**
1. **Walls:** a rectangular ring with outer `W_o × H_o` and inner `W_i × H_i`, extruded `Y = 0 … TUBE_L`.
2. **Front flange:** outer `FL_W × FL_H`, inner `W_i × H_i`, `Y = 0 … FLANGE_T`.
3. **Seam ribs** (inside the box), `Y = 0 … TUBE_L − RIB_STOP`, centred on each seam line:
   - top: x ∈ [−6, 6], z ∈ [`H_i/2 − RIB_D`, `H_i/2`]; the bottom rib mirrors it
   - right: x ∈ [`W_i/2 − RIB_D`, `W_i/2`], z ∈ [−6, 6]; the left rib mirrors it
4. **Bolt bosses:** Ø`BOSS_D` cylinders on the flange rear, `Y = FLANGE_T … FLANGE_T + BOSS_H`, at all 12 bolt positions (section 5).
5. **Rear feet** (Q3 at x = +126.7, Q4 at x = −126.7):
   - x-centre = ±(`W_o/2 − FOOT_INSET − FOOT_W/2`), width `FOOT_W`
   - side profile (Y, z) polygon: (`FOOT_END − FOOT_L − FOOT_H`, −`H_o/2`), (`FOOT_END`, −`H_o/2`), (`FOOT_END`, −`FL_H/2`), (`FOOT_END − FOOT_L`, −`FL_H/2`)
   - the front face of the foot is a 45° chamfer, so it prints without support
   - the feet end at `FOOT_END` so they clear the back-plate ridge

**Cuts (applied to every quarter):**
- **Gasket channel** in the flange front face (`Y = 0 … CH_D`): a rounded-rectangle ring centred on (`GC_X`, `GC_Z`) half-sizes, width `CH_W`, centreline corner radius `CH_R` (outer edge radius `CH_R + CH_W/2`, inner edge radius `CH_R − CH_W/2`).
- **Bolt holes:** Ø`BOLT_HOLE` through the flange and boss along Y.
- **Nut pockets:** hexagon `NUT_AF` across flats, from the boss top (`Y = FLANGE_T + BOSS_H`) down `NUT_DEPTH`. Orient the hex flats so they print cleanly. The pocket opens upward in the print pose.
- **Fan hole:** Ø`FAN_HOLE_D`, axis Z, centred (0, `Y_F`), cut through the top wall **and** the top rib band. Each of Q1 and Q2 gets a half.
- **Socket guide:** an engraved ring on the top outer face, Ø`SOCK_FL_D` to Ø`SOCK_FL_D + 2`, 0.6 deep, centred on the fan hole.
- **Label:** debossed 0.6 mm on the **inner face of the side wall** at Y ≈ `0.55·TUBE_L`, z = ±`H_i/4`. Text `Q1 FRONT` (etc.), DejaVu Sans Bold or similar, 9 mm, running along Y, readable from inside the box. Optionally add a debossed arrow pointing to −Y.

**Joints:** box-wall dovetails (`DT_WALL`) and box-flange dovetails (`DT_FLNG`) per section 3.

### 4.2 Back quarters B1–B4 (P05–P08)

- **Plate:** `W_b × H_b`, `Y = TUBE_L … DEPTH` (3 mm).
- **U-channel** on the inner face (`Y = TUBE_L − RIDGE_H … TUBE_L`), formed by two ridges. It takes the tube's rear edge with `RIDGE_CLR` either side.
  - outer ridge: between the rectangle `W_o + 2·RIDGE_CLR` × `H_o + 2·RIDGE_CLR` and the plate edge
  - inner ridge: a ring between `W_i − 2·RIDGE_CLR` and `W_i − 2·RIDGE_CLR − 2·RIDGE_T` (and the same for H)
- Split into quadrants and add jigsaw knobs (section 3). Knob and slot depth is the plate only (`Y = TUBE_L … DEPTH`). The ridges simply butt at the seams.
- **Label** `B1`… debossed 0.6 mm on the inner face (ridge side), centred in the quarter, 14 mm, reading correctly from the front and from above in the print pose (**not mirrored**).

### 4.3 Clamp quarters C1–C4 (P09–P12): front frame plus compression stop

- **Front plate:** `Y = −CLAMP_DEPTH … −CLAMP_DEPTH + CLAMP_PLATE`. Outer `FL_W × FL_H`; window `WIN_W × WIN_H` = 321.4 × 273.4. The lip covers 8.8 mm of the cardboard border and never the media.
- **Wall block:** `Y = −CLAMP_DEPTH … 0`. Outer `FL_W × FL_H`; inner `(FILTER_WO + 2·FILTER_TOL) × (FILTER_HO + 2·FILTER_TOL)` = 344 × 296, so the walls just kiss the edge foam.
- **The rear face at Y = 0 is the compression stop.** When it touches the flange, the EPDM is at `GASKET_C` (6.5) where the frame is 22 mm thick, and 3.5 where it's 25. The cardboard frame takes up the rest.
- **Bolt holes:** Ø`BOLT_HOLE` at the 12 positions, through. **Counterbore** Ø`CB_D` × `CB_DEPTH` from the front face.
- **Seams:** `DT_FLNG` dovetails per section 3, extruded the full clamp depth.
- **Magnet pockets** (visor mounts): Ø`MAG_POCKET_D` × `MAG_POCKET_DEPTH`, open on the front face, at the 8 magnet positions in section 5.1. They fall in C1 and C2 only. The pockets print as blind holes from the bed.
- **Label** `C1`… debossed 0.6 mm on the outer side face, readable from outside.

### 4.4 Fan socket (P13)

Local frame: base on z = 0, axis Z. In assembly it sits on the top outer face at (0, `Y_F`, `H_o/2`).

- **Base flange:** Ø`SOCK_FL_D` × `SOCK_FL_T`.
- **Barrel:** outside diameter `SOCK_ID + 2·SOCK_WALL`, from z = 0 to `SOCK_H`.
- **Bore:** Ø`SOCK_ID` from z = `SOCK_FL_T` to the top.
- **Through-hole:** Ø`LEDGE_ID` (z = 0 … `SOCK_FL_T`). The annulus between `LEDGE_ID` and `SOCK_ID` is the **fan ledge**.
- **Gland notch:** only if `SOCK_FL_T + RING_T + (FAN_LEN − GLAND_FROM_INTAKE) − GLAND_D/2 < SOCK_H`. It is `GLAND_D + 4` wide, runs from the top down to 2 mm below the gland, and faces **+Y (back)**.

### 4.5 TPU gasket ring (P14)

Ring with outside diameter `SOCK_ID − 0.4`, inside diameter `LEDGE_ID`, `RING_T` thick. It sits on the socket ledge, and the fan's outlet rim sits on it.

### 4.6 Intake bell (P15)

Defined in its **print pose**: mouth on the bed at z = 0, sleeve on top. In use it's flipped, with the stop lip resting on the fan's intake rim.

| z range | Feature |
|---|---|
| 0–12 | **Rim band:** outside Ø`BELL_RIM_OD`, inside Ø`BELL_MOUTH_ID` |
| 0–2 | **Support grid** inside the mouth: square lattice, bars `GRID_BAR` wide at `GRID_PITCH`. It prints first, on the bed, and in use it supports the disc against suction |
| 12–52 | **Cone:** inner radius `BELL_MOUTH_ID/2` → `STOP_ID/2` (110 → 72.05), wall ≈ `BELL_WALL` measured normal to the surface. About 43° from vertical, so no support |
| 52–82 | **Sleeve:** inside Ø`SLEEVE_ID`, wall `BELL_WALL`, with **3 grip ribs** 1.5 wide, 0.3 proud, at 120°, full length. The step from `STOP_ID` to `SLEEVE_ID` at z = 52 is the stop lip that rests on the fan |

- **Bayonet**, 3 positions at 0/120/240°:
  - **entry slot** in the rim band's outer face: `SLOT_W` wide (tangential), `SLOT_DEPTH` radial, z = 0 … `ENTRY_H`
  - **run:** same radial depth, z = `ENTRY_H − 3` … `ENTRY_H`, extending `RUN_ANG` from the entry centre in the **+angle direction (print frame)**; the run's far end is the hard stop
- **Gland notch:** if `GLAND_FROM_INTAKE − GLAND_D/2 < SLEEVE_L`, cut a `GLAND_D + 4` wide notch from z = `BAND_H + CONE_H + GLAND_FROM_INTAKE − GLAND_D/2 − 2` up through the open sleeve end, facing +Y in use.

### 4.7 Intake lid (P16)

Defined in its **print pose**: top (grille) face on the bed.

- **Disc and skirt:** overall diameter `LID_OD`. The skirt has inside diameter `LID_SKIRT_ID` and wall `LID_WALL`, height `LID_PLATE + PRESS_H + DISC_CLAMP + SKIRT_DOWN`.
- **Grille plate:** `LID_PLATE` thick, with 12.6 mm square openings at 15 mm pitch inside Ø(`BELL_MOUTH_ID − 6`).
- **Pressing ring** under the plate: radius 110–113 (over the bell rim), `PRESS_H` tall.
- **Lugs:** 3 at 120°, each `LUG_W` wide, protruding `LUG_R` inward from the skirt. They span lid-print z = `LID_PLATE + PRESS_H + DISC_CLAMP + (ENTRY_H − 3) + 0.25` up by `LUG_H`, with a **45° chamfer on the plate-side (bed-side) face**.
  - Angular position: when locked, each lug sits against the run's end stop, at (entry angle + `RUN_ANG` − 2.5°) in the same angular sense as the bell's print frame.
- **Locking:** push down through the entry slots, then **twist clockwise viewed from above** to the stop. The path was simulated clear, and the stop clashes as intended.

### 4.8 Test coupons (P00) and sleeve gauge (P00b)

- **P00 coupon plate.** All these pieces print inside the ring:
  - **gauge ring G1:** a slice of the socket barrel (inside Ø`SOCK_ID`, wall `SOCK_WALL`, 10 tall)
  - **S wall-dovetail slot block,** 20 × 24 × 20
  - **S wall-dovetail tongue block**
  - **L wall-dovetail tongue block**
  - **S jigsaw tab plate and S jigsaw slot plate,** 3 thick
  - **fastener block,** 28 × 28 × `FLANGE_T + BOSS_H`, containing a bolt hole, a counterbore underneath and a nut pocket on top
- **P00b gauge G2:** a slice of the bell sleeve (inside Ø`SLEEVE_ID` with grip ribs, wall `BELL_WALL`, 10 tall).

### 4.9 Visor V1 (left) and V2 (right), P17–P18, clear PLA

A detachable clear hood over the work zone. It **hangs by its rear lip on top of the clamp frame**, its mounting strip bears against the clamp front face, and 8 magnet pairs stop it being knocked off. The weight sits in front of the clamp's top edge, so it tips the strip **into** the clamp face. The magnets aren't load-bearing.

**Full visor (assembly frame), then split at x = 0:**
1. **Mounting strip:** an inverted U in the XZ plane, `Y = Y_CF − STRIP_T … Y_CF`. It is the rectangle `x ∈ [−FL_W/2, FL_W/2]`, `z ∈ [WING_END_Z, FL_H/2]` minus the window rectangle `x ∈ [−WIN_W/2, WIN_W/2]`, `z < WIN_H/2`. It covers only the clamp rim and never the window.
2. **Canopy:** `x ∈ ±FL_W/2`, `Y = Y_CF − VISOR_REACH … Y_CF + VISOR_LIP`, `z = FL_H/2 … FL_H/2 + VISOR_T`. The part behind `Y_CF` is the lip that rests on the clamp top.
3. **Side wings:** `VISOR_T` thick, outer face flush with `x = ±FL_W/2`. Side profile (Y, z) is a triangle: (`Y_CF`, top), (`Y_CF − VISOR_REACH`, top), (`Y_CF`, `WING_END_Z`), with top = `FL_H/2 + VISOR_T`.
4. **Front rib:** under the canopy's front edge, `VISOR_T` deep in Y, `FRONT_RIB_H` tall, full width.

**Cuts (on the strip's rear face, open towards +Y):**
- **Magnet pockets:** Ø`MAG_POCKET_D` × `MAG_POCKET_DEPTH`, coaxial with the clamp magnets (section 5.1).
- **Bolt-head pockets:** Ø`HEAD_CLR_D` × `HEAD_CLR_DEPTH` at every bolt with z > `WING_END_Z`, i.e. (±59.75, 155.25), (±179.25, 155.25), (±179.25, 51.75). The 1 mm-proud bolt heads key into them and locate the visor.

**Split and joint:**
- Split at x = 0. **V1** (x < 0) owns 3 S jigsaw knobs in the canopy plane (`KNOB[0]`, extruded through `VISOR_T`), pointing +X, at Y = `Y_CF − 30`, `Y_CF − 80`, `Y_CF − 130`.
- **V2** gets the matching slots (`JIG_CLR`), cut fully through the canopy.
- The strip top bar and the front rib simply butt at the seam. V1 and V2 are glued into one visor.

**Print pose:** canopy top face on the bed: `translate([0,0,FL_H/2 + VISOR_T]) rotate([180,0,0])`. The wings and strip rise vertically, and the wing narrows as it rises, so there's no overhang. The pockets are horizontal 6–9 mm holes (a teardrop top is optional).

---

## 5. Bolt pattern (12 × M4, shared by flange, bosses and clamp)

Positions (x, z), with `BX/3` = 59.75 and `BZ/3` = 51.75:

| # | x | z | # | x | z |
|---|---|---|---|---|---|
| 1 | −179.25 | 155.25 | 7 | 179.25 | −155.25 |
| 2 | −59.75 | 155.25 | 8 | 59.75 | −155.25 |
| 3 | 59.75 | 155.25 | 9 | −59.75 | −155.25 |
| 4 | 179.25 | 155.25 | 10 | −179.25 | −155.25 |
| 5 | 179.25 | 51.75 | 11 | −179.25 | −51.75 |
| 6 | 179.25 | −51.75 | 12 | −179.25 | 51.75 |

General form: corners (±`BX`, ±`BZ`); long sides (±`BX/3`, ±`BZ`); short sides (±`BX`, ±`BZ/3`). No bolt may sit on a seam.

**Bolt length:**
- Head seat at Y = −28.5 (after the 3 mm counterbore)
- Nut pocket floor at Y = `FLANGE_T + BOSS_H − NUT_DEPTH` = 8.3, so the nut occupies 8.3–11.5
- **M4 × 40** socket cap ends at Y = 11.5, flush with the nut: full engagement. Heads sit 1 mm proud of the clamp face, which is what locates the visor

---

### 5.1 Magnet positions (8 pairs: clamp front face and visor strip)

| # | x | z | # | x | z |
|---|---|---|---|---|---|
| M1 | −119.5 (`−2·BX/3`) | 155.25 | M5 | −179.25 | 103.5 (`2·BZ/3`) |
| M2 | −29.88 (`−BX/6`) | 155.25 | M6 | −179.25 | 25.88 (`BZ/6`) |
| M3 | 29.88 | 155.25 | M7 | 179.25 | 103.5 |
| M4 | 119.5 | 155.25 | M8 | 179.25 | 25.88 |

These positions clear every bolt counterbore and every seam dovetail (checked). All 8 sit in C1/C2 and in the strip.

---

## 6. Parts list and file names

| ID | File | Part | Qty | Material | Est. mass |
|---|---|---|---|---|---|
| P00 | `P00_coupons.stl` | Coupon plate + gauge G1 | 1 | PLA | 62 g |
| P00b | `P00b_gauge_G2.stl` | Sleeve gauge G2 | 1 | PLA | 15 g |
| P01–P04 | `P01_Q1.stl` … `P04_Q4.stl` | Box quarters | 4 | PLA | 259 / 265 / 341 / 340 g |
| P05–P08 | `P05_B1.stl` … `P08_B4.stl` | Back quarters | 4 | PLA | 63 g each |
| P09–P12 | `P09_C1.stl` … `P12_C4.stl` | Clamp quarters | 4 | PLA | 92 g each |
| P13 | `P13_socket.stl` | Fan socket | 1 | PLA | 135 g |
| P14 | `P14_ring_TPU.stl` | Fan gasket ring | 1 | **TPU 95A** | 4 g |
| P15 | `P15_bell.stl` | Intake bell | 1 | PLA | 189 g |
| P16 | `P16_lid.stl` | Intake lid | 1 | PLA | 96 g |
| P17 | `P17_V1.stl` | Visor, left half (owns knobs) | 1 | **Clear PLA** | 177 g |
| P18 | `P18_V2.stl` | Visor, right half | 1 | **Clear PLA** | 176 g |

**Total ≈ 2.3 kg PLA + ≈ 0.35 kg clear PLA** (estimated from mesh volume and the infill settings; the slicer is the authority).

---

## 7. Print poses (export transforms from the assembly frame)

| Part | Face on the bed | Transform (then centre in XY, min z = 0) | Verified envelope (X × Y × Z) |
|---|---|---|---|
| Q1–Q4 | Flange front face | `rotate([90,0,0])` (assembly +Y becomes print +Z) | 190.5 × 162.5 × 227 (Q2/Q4: 186.5 × 166.5 × 227) |
| B1–B4 | Back outer face (ridges up) | `translate([0,0,DEPTH]) rotate([-90,0,0])` | ≤ 178.9 × 154.9 × 9 |
| C1–C4 | Clamp front face | `translate([0,0,CLAMP_DEPTH]) rotate([90,0,0])` | ≤ 190.5 × 166.5 × 31.5 |
| Socket | Base flange | local frame | 210 × 210 × 40 |
| TPU ring | Flat | local | 148.2 × 148.2 × 2 |
| Bell | Mouth (grid) | local print frame | 227 × 227 × 82 |
| Lid | Grille face | local print frame | 231.4 × 231.4 × 20.4 |
| V1 / V2 | Canopy top face | `translate([0,0,FL_H/2 + VISOR_T]) rotate([180,0,0])` | 198 × 170 × 164.9 / 186.5 × 170 × 164.9 |
| P00 / P00b | Flat | local | 154.6 × 154.6 × 20 / 153.5 × 153.5 × 10 |

**All parts are support-free in these poses.** Overhangs are limited to 45° chamfers (feet, lugs), the bell cone at about 43° from vertical, and short bridges (the bayonet run roofs, about 3 mm).

---

## 8. Print settings: ElegooSlicer / OrcaSlicer, Centauri Carbon 2

### 8.1 Global (all PLA parts)

| Setting | Value | Why |
|---|---|---|
| Base profile | Stock CC2 **0.20 mm Standard** + your PLA filament profile | |
| Nozzle / plate | 0.4 mm / stock textured PEI | |
| Layer height / first layer | 0.20 / 0.20 mm | |
| Supports | **Off** | Every part is designed support-free |
| Elephant foot compensation | **0.15 mm** | Joints and gasket faces start on the first layers |
| Outer wall speed | **≤ 120 mm/s** | Dovetail accuracy |
| Seam position | Aligned, and kept off the dovetail faces (paint it onto an outside corner if the slicer drifts) | |
| Sparse infill | Gyroid 15% | |
| Top / bottom shell layers | 5 / 4 | |
| Chamber / lid | Stock PLA behaviour (PLA wants cooling) | |

### 8.2 Per part

| Part | Wall loops | Infill | Brim | Notes |
|---|---|---|---|---|
| P00 coupons | 3 | 15% | — | **Print first.** Tune `CLR` before committing 30+ hours |
| P00b gauge G2 | 3 | — | — | 10-minute print |
| P01–P04 box quarters | **4** (makes the 3 mm walls fully solid, which helps airtightness) | 15% | 5 mm outer | 227 mm tall, flange gives a big footprint |
| P05–P08 back quarters | 3 | 15% | — | Ridges up |
| P09–P12 clamp quarters | 4 | 15% | 3 mm | The front face on the bed is the show face |
| P13 socket | 3 | 15% | — | |
| P14 TPU ring | — (solid) | 100% | — | TPU 95A, 25–40 mm/s, stock TPU profile. If you run the CANVAS unit, feed TPU direct (filament switchers and soft TPU rarely get on) |
| P15 bell | 3 | 15% | 3 mm | Grid prints first on the bed |
| P16 lid | 3 | 15% | — | |
| P17–P18 visor (clear PLA) | 3 | **100%** aligned rectilinear | — | 6 top / 6 bottom shells, outer wall 60 mm/s, other speeds ≤ 80 mm/s, nozzle +10 °C over the profile, part fan about 50%. A smooth PEI plate gives the glossiest canopy face if you have one; the textured plate frosts it. Expect translucent, not glass |

### 8.3 Calibration loop (P00)

| Test | Pass | If it fails |
|---|---|---|
| S tongue into S slot | Slides home by hand, no slop | Too tight: `CLR` +0.05. Sloppy: −0.05 |
| **L tongue into S slot** | **Must NOT go in** | This is the anti-misassembly coding. If it goes in, reduce `CLR` |
| Jigsaw S tab | Presses in, holds itself flat | Adjust `JIG_CLR` ±0.05 |
| M4 nut | Drops into the pocket and sits flush | Adjust `NUT_AF` ±0.1 |
| M4 bolt | Passes the hole freely, and the head sits in the counterbore | Adjust `BOLT_HOLE` / `CB_D` |
| G1 on the fan body | Slides on with a whisker of clearance | Adjust `SOCK_CLEAR` |
| G2 on the fan's intake end | Pushes on and grips | Adjust the grip-rib height (0.3) |

---

## 9. Acceptance checks for the OpenSCAD build (the reference passed all of these at the measured dimensions)

1. **Bed fit:** every exported STL ≤ 250 × 250 × 250, min z = 0, manifold and watertight.
2. **Static interference:** no two parts in assembly pose intersect (touching faces allowed). This includes the EPDM and filter ghosts against the channel and clamp.
3. **Slide path:** with the flange (or clamp front) as the reference face, translate each newly added piece +Y by 2 → 226 mm against its neighbours; the intersection must be ~0 at every step. Order: Q2 → Q1 → Q3 → Q4 (Q4 engages two seams at once), and the same for C.
4. **Wrong-assembly blocking:** rotate Q3 180° about Y into Q1's place and it must clash with its neighbours (> 100 mm³; the reference gives 621 for Q, 295 for B, 118 for C). Same for Q4 into Q2, B3 into B1, B4 into B2, C3 into C1, C4 into C2.
5. **Compression stop:** the clamp rear face is at Y = 0 while the clamp lip is at Y = `FILTER_BACK_Y − FILTER_T`.
6. **Bayonet:** with the lid locked, rotating it towards the entry is clear the whole way, lifting it out at the entry is clear, and rotating it past the stop clashes.
7. **Echo** all derived values (section 2.3) and confirm the asserts.
8. **Visor:**
   - V1 and V2 don't intersect, and V2 lowers onto V1's knobs freely.
   - The fitted visor clears the clamp, bolt heads and magnets.
   - Pulling it straight forward (−Y) is clear from the first millimetre.
   - The magnet pockets in the clamp and the strip are coaxial.

---

## 10. Non-printed bill of materials

| Item | Spec | Qty |
|---|---|---|
| Fan | 150 mm inline duct fan, 500 m³/h or greater (measured body Ø148.1) | 1 |
| HEPA | True HEPA replacement set for Levoit LV-PUR131 / LV-PUR131S (HEPA panel used; carbon panel not used on the front) | 1 set |
| EPDM strip | Self-adhesive EPDM, **10 mm wide × 8 mm thick** | ~1.4 m (perimeter ≈ 1.2 m + spare) |
| Bolts | M4 × 40 socket cap (ISO 4762) | 12 |
| Nuts | M4 hex (ISO 4032) | 12 |
| Magnets | Ø6 × 3 mm disc, N42 or stronger | 16 |
| Glue | Thin (water-thin) cyanoacrylate | 1 bottle |
| Silicone | Neutral-cure, low-odour | 1 small tube |
| Sealant coat | Plasti Dip, brush-on (not spray) | 1 tin, 250 ml |
| Pre-filter | Aquarium floss, 10 mm (a 50 × 50 cm sheet gives 4 discs of Ø`DISC_D` = 224). Optional thin activated-carbon sheet underneath | 1 sheet |
| Filament | PLA ~2.3 kg; clear PLA ~0.35 kg; TPU 95A, a few grams | |
