# LFH v1 — Handover for Claude Code: build the repo

**Owner:** Joe (UK, maker). **Repo folder:** `E:\LFH-Project\`
**Written:** 20 Nov 2026, at the end of the Claude chat where the whole project was designed.
**Your job:** turn `E:\LFH-Project\` into a clean git repo that loses nothing, then push it.

Read the whole file before touching anything. **Do not change any geometry.** The design is finished, measured and fit-tested. This repo is for safekeeping.

---

## 0. TL;DR for Claude Code

1. **Ask Joe first:**
   - which GitHub account and repo name to use
   - private or public (private suggested)
   - whether g-code goes in (suggested **no**: about 150 MB of machine-specific output)
2. Build the layout in section 9 from the sources in section 8. Joe has already copied most of them into `E:\LFH-Project\Models\`.
3. `E:\LFH-Project\_from_chat\` holds the files that **only existed in the chat's cloud container**: the manual generator, renders, check scripts and Joe's product photos. Move them into place as section 9 says.
4. Add `README.md`, `CLAUDE.md` (seed in section 10), `.gitignore` and `.gitattributes`.
5. Run the verification in section 11, commit in logical chunks, then push.
6. Keep Joe's working style (section 10) in everything you write and say.

---

## 1. What this is

A **cheap, fully 3D-printed laminar flow hood** in the Gordotek style, for sterile work such as mushroom culture and agar.

- A True HEPA panel forms the front face.
- A 150 mm inline duct fan sits on top, **intake up, blowing down** into a sealed box. That pressurises it, so clean air leaves through the HEPA as a laminar sheet.
- An intake bell on top of the fan holds a washable aquarium-floss pre-filter disc under a twist-lock grille lid.
- A detachable clear visor hangs on magnets over the work zone.

**Printer:** Elegoo Centauri Carbon 2. The bed is 256 × 256 mm, so every part had to fit 250 × 250 × 250. The box is therefore split into quarters that **slide together on size-coded dovetails** and are superglued, with one assembly order that works and wrong swaps physically blocked.

**Pass test:**
- Hold a lighter flame 5–10 cm in front of the filter at 9 points. It should lean about **45° and stay steady**. The plug-in speed controller sets the speed.
- Smoke should run straight out with no curl-back and no leak round the clamp.

---

## 2. Bought parts (Joe's actual listings)

| Item | Joe's listing name | Key spec | Qty |
|---|---|---|---|
| Fan | 150mm Inline Duct Fan 500m3/h or greater | Body Ø148.1 (measured), 150 long; cable gland 52 mm below the intake end, Ø11.5 with boot | 1 |
| Speed controller | Plug In Variable Fan Speed Controller Dimmer | UK 3-pin plug-in | 1 |
| HEPA | Replacement Filter set True HEPA For Levoit LV-PUR131 Air Purifier LV-PUR131S UK | Cardboard frame 339 × 291, 343 × 295 over the 2 mm edge foam, 22–25 thick, 10.8 border. The set's carbon panel is **not** used on the front | 1 set |
| Pre-filter | 1cm thick aquarium floss | 50 × 50 cm sheet gives 4 discs of Ø224 | 1 sheet |
| Gasket | Neoprene Self Adhesive Foam Sponge Strip … EPDM Weather Strips | 10 wide × 8 thick, **solid sponge** (not hollow D) | ~1.4 m |
| Bolts | M4 socket cap bolts | M4 × 40, 3 mm hex key | 12 |
| Nuts | M4 hex nuts | 7 mm across flats, 3.2 thick | 12 |
| Magnets | Magnets, Ø6 × 3 mm disc (N42 or stronger) | 8 in the clamp, 8 in the visor | 16 |
| Sealant coat | Plasti Dip | **Brush-on** 250 ml tin, not spray (Joe's choice: cheaper, less mess) | 1 tin |
| Superglue | (no photo) search "thin Cyanoacrylate" | Water-thin | 1 bottle |
| Silicone | (no photo) search "neutral cure silicone" | Neutral-cure, **not** acetoxy (vinegar) | 1 small tube |
| Filament | — | PLA ≈2.3 kg; clear PLA ≈0.35 kg **or** clear PETG ≈0.36 kg; TPU 95A, a few grams | — |

The product photos are in `_from_chat/pipeline/manifest_img/`.

---

## 3. Architecture

**Assembly frame:**
- X is right as seen from the front, Y is depth (Y = 0 is the flange/gasket face, +Y goes back), Z is up.
- Quarters are numbered clockwise from the front: **1 top-left, 2 top-right, 3 bottom-right, 4 bottom-left**.
- Prefixes: **Q** box, **B** back, **C** clamp.

| Assembly | Parts | How it works |
|---|---|---|
| **Box (tube)** | Q1–Q4 (P01–P04) | L-shaped quarters with an **integral front flange**, printed flange-down. Tube 227 deep. Inner opening 317.4 × 269.4 (= the filter's open window), 3 mm walls, flange 373 × 325 × 6 |
| **Seams** | all | **Sliding dovetails** on internal ribs. Every joint slides along Y, so you lower pieces from above onto a flat surface. **Slots are open at both ends**, otherwise the top and bottom pairs can't slide together. Each piece **owns the tongue on its clockwise seam**. **Size coding:** top and right seams are S, bottom and left are L, so a wrong swap clashes physically. Measured clash: Q 621, B 295, C 118 mm³ |
| **Back** | B1–B4 (P05–P08) | Flat plate joined by **jigsaw tabs**. A **U-channel** (two ridges, 6 high) takes the tube's rear edge in a silicone bead. This came from Joe's original "edges into a groove on the back" idea |
| **Front seal** | C1–C4 (P09–P12) | Clamp frame, 31.5 deep, with a 4 mm front plate and a 321.4 × 273.4 window. **Its rear face is the compression stop**, so bolts can't over-squash the gasket. 12 × M4 × 40 run from counterbores in the clamp front into **captive nuts** in pockets on bosses behind the flange |
| **Gasket** | EPDM 10 × 8 | Stuck on the **flat flange face**. A 0.6 × 0.2 mm **guide line** marks the strip's outer edge, flush with the filter's cardboard edge. Squeezed to **5.5 mm with a 22 mm filter and 2.5 mm with 25 mm**. The design uses the 22 mm end on purpose, because leaks start at the thin spots |
| **Fan mount** | SOCKET (P13) + RING (P14, TPU) | Socket bore Ø148.6 is glued and siliconed inside an engraved ring on the box top, over a Ø144.1 hole split across Q1/Q2. The TPU ring seals the fan in the socket |
| **Intake** | BELL (P15) + LID (P16) | Bell sleeve Ø148.5 with 0.3 mm grip ribs pushes onto the fan's intake end, then flares into a mouth. A support grid holds the Ø224 floss disc. The grille lid locks with 3 bayonet lugs: push down through the entry slots and **twist clockwise to a stop**. The gland position needs **no notch** in the socket or the bell |
| **Visor** | V1 (P17, owns knobs) + V2 (P18) | Clear hood. Joe's brief: it runs about 150 mm out from the box top and tapers to about halfway down the sides. It **hangs by its rear lip on the clamp top**, its mounting strip sits against the clamp face, and bolt-head pockets locate it. **8 magnet pairs** only stop knocks and carry no load. Pulls straight forward to remove |

**Assembly order (manual section 6):**
1. **Box:** Q1 + Q2, then Q3, then Q4 last (it engages two seams), then glue.
2. **Back:** jigsaw plate, then silicone into the U-channel, then lower the box in. Leave 24 h.
3. **Top and seal:** socket, then Plasti Dip inside.
4. **Clamp, nuts, gasket:** clamp frame, captive nuts, EPDM on the guide line, filter with the pre-filter face towards the box, bolts criss-cross until the clamp touches the flange.
5. **Fan and intake:** fan, bell, floss disc, lid.
6. **Test:** flame and smoke.
7. **Visor last:** join the halves, fit the clamp magnets, then the visor magnets (stick loose magnets on the clamp ones so the poles self-orient).

The air spreader inside the box is **not fitted in v1**. Add a deflector only if the bottom row leans much harder.

---

## 4. Key numbers (full list in the spec, `LFH-v1_OpenSCAD_build_spec_v5.md`)

**Measured on 31 Oct 2026:**

| Parameter | Value |
|---|---|
| FILTER_W × FILTER_H | 339 × 291 |
| FILTER_FOAM | 2 |
| FILTER_T / FILTER_T_MAX | 22 / 25 |
| FILTER_BORDER | 10.8 |
| FAN_OD | 148.1 |
| FAN_LEN | 150 |
| GLAND_FROM_INTAKE | 52 |
| GLAND_D | 11.5 |

**Derived:**

| Value | mm |
|---|---|
| W_i × H_i | 317.4 × 269.4 |
| W_o × H_o | 323.4 × 275.4 |
| Flange | 373 × 325 |
| TUBE_L | 227 |
| CLAMP_DEPTH | 31.5 |
| BX, BZ (bolt grid) | 179.25, 155.25 |
| Back W_b × H_b | 328.8 × 280.8 |
| FOOT_H | 24.8 |
| LEDGE_ID | 140.1 |
| FILTER_BACK_Y | −5.5 |
| DISC_D | 224 |
| LID_OD | 231.4 |
| SOCK_ID | 148.6 |
| FAN_HOLE_D | 144.1 |
| SLEEVE_ID | 148.5 |
| STOP_ID | 144.1 |
| GC (gasket centreline) | 164.5 / 140.5 |
| Clamp window | 321.4 × 273.4 |
| CLAMP_WALL | 14.5 |
| Y_F (fan centre depth) | 113.5 |

**Gasket and guide line (since 17 Nov):**

| Parameter | Value |
|---|---|
| GASKET_W / GASKET_T | 10 / 8 |
| GASKET_C | 5.5 |
| CH_D | 0 (no groove) |
| CH_R | 8 |
| GUIDE_W / GUIDE_D | 0.6 / 0.2 |

**Fit-tuned values (fit tests passed, so all at default):**

| Parameter | Value |
|---|---|
| CLR (dovetail, per face) | 0.15 |
| JIG_CLR | 0.2 |
| NUT_AF | 7.3 |
| NUT_DEPTH | 3.7 (full M4 × 40 engagement) |
| BOLT_HOLE | 4.4 |
| SOCK_CLEAR | 0.5 |
| Grip-rib height | 0.3 |

---

## 5. Parts (one `.scad` wrapper + one STL each)

| ID | File | Part | Material | Mass | Print notes |
|---|---|---|---|---|---|
| P00 | `Test/P00_coupons` | Coupon plate + socket gauge G1 | PLA | 62 g | **Print first.** Tests dovetail S/L, jigsaw, nut, bolt and counterbore, socket bore |
| P00b | `Test/P00b_gauge_G2` | Bell sleeve gauge G2 | PLA | 15 g | |
| P01–P04 | `P01_Q1` … `P04_Q4` | Box quarters | PLA | 259 / 265 / 341 / 340 g | 4 walls, 5 mm brim, 227 tall. **P01 and P02: supports on Auto**, which only land on the crown of the half fan hole |
| P05–P08 | `P05_B1` … `P08_B4` | Back quarters | PLA | 63 g each | Ridges up |
| P09–P12 | `P09_C1` … `P12_C4` | Clamp quarters | PLA | 92 g each | 4 walls, 3 mm brim, front face on the bed |
| P13 | `P13_socket` | Fan socket | PLA | 135 g | |
| P14 | `P14_ring_TPU` | Fan gasket ring | TPU 95A | 4 g | 25–40 mm/s, 100% |
| P15 | `P15_bell` | Intake bell | PLA | 189 g | Grid on the bed, 3 mm brim |
| P16 | `P16_lid` | Intake lid | PLA | 96 g | |
| P17 | `P17_V1` | Visor left (owns knobs) | Clear PLA or clear PETG | 177 g | Canopy face down, 100% infill. PETG settings in spec 8.4 and manual section 4 |
| P18 | `P18_V2` | Visor right | Clear PLA or clear PETG | 176 g | As P17 |

**Global print settings:**
- Stock CC2 0.20 mm Standard profile, 0.4 nozzle, textured PEI.
- Elephant-foot compensation **0.15**, outer wall ≤ 120 mm/s, aligned seam kept off the dovetail faces.
- Gyroid 15%, shells 5 top / 4 bottom.
- Supports **off except P01 and P02**.

---

## 6. Decision log (why things are the way they are)

1. **Concept:** Joe's brief was all printed, about 4 parts per panel, male/female or jigsaw joints plus superglue, numbered parts and one way to assemble. That became size-coded sliding dovetails plus the ownership rule.
2. **Depth** went from 25 to **23 cm** (Joe), giving a 227 mm tube.
3. **The filter is held by gasket, nuts and bolts** (Joe's preference) rather than glue. That gave the clamp frame, which doubles as the compression stop, plus captive nuts.
4. **The back** uses a U-channel plus silicone, from Joe's "mitred edges into a groove on the back".
5. **Sealing:** Plasti Dip inside (**brush-on tin**, Joe's change from spray), neutral-cure silicone on joins, superglue on seams.
6. **Fan sizing:** 500 m³/h. Joe confirmed against Gordotek's identical-spec fan (flame about 46°). The pass test is a flame at about 45°, and the speed controller was added to the parts list to set it.
7. **Pre-filter:** activated-carbon idea, then G4, then **1 cm aquarium floss**, which is far cheaper. It sits as a disc under a bayonet lid.
8. **Filter set:** Levoit LV-PUR131 HEPA plus carbon panel. HEPA on the front; carbon panel not used there.
9. **Gasket:** EPDM, but the best Joe could get was **10 × 8**, so the design is built round that.
10. **Visor:** a later addition, detachable clear PLA on 6 × 3 mm magnets.
11. **31 Oct:** final dimensions from Joe's calipers (table above).
12. **Outputs:** an all-in-one model is useless for slicing, so **every part is its own wrapper `.scad` plus STL**.
13. **31 Oct manual feedback:**
    - The parts list moved to the **top** of the manual, using Joe's photos and listing names.
    - Magnet size is stated everywhere.
    - No-photo items get a search term.
    - The bench kit sits at the bottom of the list.
14. **17 Nov, fit tests (P00/P00b):** all green, so no parameter changes.
15. **17 Nov, P01/P02 overhang:**
    - The half fan hole is split at the Q1/Q2 seam, so its crown is an **open-ended overhang** with no far side to bridge to.
    - Joe's call: **Auto supports**, which only put support there.
    - Manual v4 records this.
16. **17 Nov, gasket groove removed:**
    - Joe spotted that the old 1 mm groove in the bed-side flange face printed as a **10.5 mm roof standing on a 0.55 mm sliver**. That was effectively midair, after elephant-foot compensation.
    - The fix was a **flat flange plus a hairline guide line**.
    - Only P01–P04 were re-exported.
    - The squeeze went from 6.5/3.5 to 5.5/2.5.
    - The clamp, bolts and visor did not change.
17. **19–20 Nov:** clear PETG added as a visor option, in spec v5 and manual v5.

---

## 7. "Don't undo" list (these look odd but are deliberate)

- **Dovetail slots open at both ends.** Closed ends made the top and bottom pairs impossible to assemble.
- **S/L size coding and clockwise tongue ownership.** These are the anti-misassembly system.
- **Flat flange face (`CH_D = 0`).** Any recess in a bed-side face deeper than a layer becomes an unsupported roof.
- **`convexity=10` on every `linear_extrude` / `rotate_extrude`.** Without it, OpenSCAD's F5 preview draws walls missing.
- **`FILTER_T = 22` as the design point.** Leaks start at the thin spots. The squeeze check at 25 mm is now `>= 2.5`.
- **`NUT_DEPTH = 3.7`.** That's what gives full thread engagement on M4 × 40.
- **Feet end at `FOOT_END = TUBE_L − RIDGE_H − 1`.** That keeps them clear of the back ridge.
- **Lid lugs sit at the bayonet end stop**, and the lid twists **clockwise**.
- **No gland notch** in the socket or the bell at the measured gland position.
- **Wrapper pattern:** `include <lfh_v1_reference.scad>` then `part = "Q1"; pose = "print";`. In OpenSCAD the last assignment wins, so the wrapper overrides the file's defaults. Test wrappers use `include <../lfh_v1_reference.scad>`, so keep `Test/` **inside** the models folder.

---

## 8. Where everything is right now

| Location | Contents | Status |
|---|---|---|
| `E:\LFH-Project\Models\` | `lfh_v1_reference.scad` (**current**, 28,240 bytes, CRLF, MD5 `7ec683b31247e2c9a3a9a5985a203ad2`) plus P01–P18 `.scad` wrappers and STLs | ✅ Current. P01–P04 STLs are the 17 Nov flat-flange versions (binary STL). The rest date from 31 Oct (ASCII STL). All match the reference |
| `E:\LFH-Project\Models\Test\` | P00 coupons and P00b gauge (`.scad` + STL) | ✅ |
| `E:\LFH-Project\Models\Documents\` | Manual PDFs v1–v5 and spec `.md` v1, v2, v3, v5 (there is **no spec v4**) | ✅ **v5 is current** for both |
| `E:\LFH-Project\_from_chat\` | Chat-only files (see below) | Move into the layout |
| `C:\Users\bigjo\Desktop\LFH\3mf\` | `P00_coupons.3mf`, `P01.3mf`, `PARTS.3mf`, `WIPPARTS.3mf` (slicer projects, small) | Copy in. ⚠️ `P01.3mf` was saved **before** the flat-flange change, so it probably holds the old grooved P01. Ask Joe |
| `C:\Users\bigjo\Desktop\LFH\gcodes\` | P00, P00b, P01–P08, P9-P10, P11-P12, 5cmsquare (≈150 MB; the two clamp files are about 25 MB each) | Suggested: **exclude** (`.gitignore`). P01–P04 g-code was sliced about 21:00 on 17 Nov, after the change. Joe decides |
| `C:\Users\bigjo\Desktop\LFH\` | Duplicate PDFs and specs, `first_layer_square_50x50x0.2.stl` (Joe's calibration square) | The duplicates are already in `Models\Documents`. The calibration STL is optional |
| `C:\Users\bigjo\Desktop\LFH\lfh_v1_reference.scad` | **Stale** 31 Oct copy (27,119 bytes, still has the groove) | ❌ Don't use |
| `C:\Users\bigjo\openscad-mcp-workspace\LFH\` | The OpenSCAD MCP working copy; identical to `Models\` | Leave it alone. It's where the OpenSCAD MCP works |
| Junk | `~$H_v1_Build_Manual_v*.pdf` (Office lock files), `LFH - Shortcut.lnk` | Ignore |
| Online manual | https://claude.ai/artifact/4RUymtbCRjRWuiFyjXHBpa (private to Joe) | Stale, about v3 content. The PDF v5 is the truth |

**`_from_chat\pipeline\`** mirrors the cloud container's working folder, so the scripts run unmodified from inside it:

| File | What it is |
|---|---|
| `build_site.py` | Generates the manual: `site/index.html` from the `PARTS`, `STAGES`, `BOUGHT`, `NOPIC` and `BENCH` lists plus HTML/CSS (including the `@media print` rules) |
| `pdf.js` | Playwright: `site/index.html` → `out/LFH_v1_Build_Manual.pdf` (A4, print backgrounds). Paths are relative to the script |
| `site/index.html`, `site/img/*.png` | The built manual (v5 content) and all images: renders (`hero`, `exploded`, `print_*`, `s_*` steps) and processed product photos (`m_*`) |
| `manifest_img/*.png` | Joe's original product photos |
| `scene.scad` | Render scenes for the manual. It imports STLs from `stl_asm/` and `stl_print/`. ⚠️ The camera arguments for each image were never scripted; the PNGs are final art |
| `render.sh` | `render.sh NAME SCENE CAMERA [SIZE] [EXTRA]` → `img/NAME.png` via OpenSCAD |
| `export.sh` | `export.sh PART print\|asm` → `stl_print/` or `stl_asm/PART.stl`. It expects `lfh_ref.scad` in the same folder, a copy of `Models/lfh_v1_reference.scad` |
| `checks.py` | The full acceptance battery (spec section 9): bed fit, static interference, slide paths, wrong-swap clash, bayonet path, visor press-on and pull-off. Uses trimesh with the manifold engine. Writes `checks.json` |
| `checks.json` | Last results (31 Oct, all pass). Geometry above 1 mm hasn't changed since; the 17 Nov change was proven at a maximum deviation of 0.0002 mm |
| `manual_feedback.md` | Joe's 31 Oct manual feedback log (applied) |
| `lfh_ref_pre-measurement.scad` | Archive: the reference before Joe's measurements, with placeholder dimensions |
| `P01_overhang.png` | Diagram of the P01 fan-hole crown overhang (the reason for the auto supports) |

The pipeline was built on Linux. On Windows, run it under Git Bash or WSL; `xvfb-run` is Linux-only, so drop it there.

| Script | Needs |
|---|---|
| `export.sh`, `render.sh` | `openscad` (2021.01+) |
| `checks.py` | Python with `trimesh`, `manifold3d`, `numpy` |
| `pdf.js` | Node with `playwright` |

---

## 9. Suggested repo layout

Keep Joe's `Models/` layout; the wrappers and `Test/` include paths depend on it.

```
LFH-Project/
├─ README.md                  ← new (outline below)
├─ CLAUDE.md                  ← new (seed in section 10)
├─ HANDOVER.md                ← this file; move it to docs/ once the repo is built
├─ .gitignore / .gitattributes
├─ Models/                    ← as is: reference .scad, P01–P18 .scad + .stl
│  ├─ Test/                   ← P00, P00b
│  └─ Documents/              ← manual PDFs and spec .md, all versions (v5 = current)
├─ slicer/3mf/                ← from Desktop\LFH\3mf
├─ manual/                    ← from _from_chat\pipeline (keep the internal layout so the scripts still run)
│  ├─ build_site.py  pdf.js  scene.scad  render.sh  export.sh  checks.py  checks.json
│  ├─ site/index.html  site/img/
│  └─ manifest_img/
└─ docs/
   ├─ manual_feedback_2026-10-31.md
   ├─ P01_overhang.png
   └─ archive/lfh_ref_pre-measurement.scad
```

**`.gitignore` suggestion:**

```
*.gcode
~$*
*.lnk
Thumbs.db
desktop.ini
manual/stl_print/
manual/stl_asm/
manual/out/
manual/logs_*.txt
```

**`.gitattributes` suggestion:**

```
*.stl  binary
*.3mf  binary
*.pdf  binary
*.png  binary
```

Leave `.scad` line endings alone: the copies on Joe's machine are CRLF, and the OpenSCAD MCP is happy with them. The total repo is roughly 35 MB, so no LFS is needed.

**README outline:**
1. One-paragraph description and a hero image (`manual/site/img/hero.png`).
2. Where to start: `Models/Documents/LFH_v1_Build_Manual_v5.pdf` (build) and `LFH-v1_OpenSCAD_build_spec_v5.md` (CAD spec).
3. Parts table, from section 5.
4. Bought-parts table, from section 2.
5. How to regenerate STLs: open a wrapper in OpenSCAD and export, or use the OpenSCAD MCP.
6. How to rebuild the manual: `manual/` pipeline.
7. Status (section 12).
8. Credit: the Gordotek laminar flow box concept (gordotek.org/laminarflowbox).

---

## 10. Seed for the repo's `CLAUDE.md` (working style: keep it)

```markdown
# LFH v1 — notes for Claude

## Project
3D-printed Gordotek-style laminar flow hood for an Elegoo Centauri Carbon 2.
- Geometry source of truth: Models/lfh_v1_reference.scad
- Spec: Models/Documents/LFH-v1_OpenSCAD_build_spec_v5.md (the spec wins over the .scad if they disagree)
- Build manual: Models/Documents/LFH_v1_Build_Manual_v5.pdf, generated by manual/build_site.py + manual/pdf.js
- Design history and "don't undo" list: docs/HANDOVER.md

## Rules for parts
- Every printable part gets its own wrapper .scad (include the reference, then set `part`/`pose`) AND its own STL. Never deliver an all-in-one model for slicing.
- When geometry changes: re-export only the affected parts, then verify (watertight, single body, nothing else moved).
- Before claiming a part needs no supports, check overhangs, including bed-side recesses.

## Docs
- Released docs are versioned `_vN` and never overwritten. The next manual/spec is v6.
- When Joe is collecting feedback ("hold fire, just store"), log the items and amend nothing until he says go. Then do it all in one pass.
- Change only what was asked. List anything else that's now stale in one line, rather than silently "fixing" it.

## Working with Joe
- British English. Brief, dry, direct. Bullets and tables over walls of text.
- Complex tasks: no more than two instructions at a time, and verify each step before moving on.
- Never promise outcomes. Probabilistic framing, own mistakes briefly, then fix them.
- No sign-off questions, no flattery, no "you're right" plus a restatement.
- Default to UK suppliers.
```

---

## 11. Verification before the first push

1. The MD5 of `Models/lfh_v1_reference.scad` is `7ec683b31247e2c9a3a9a5985a203ad2` and it contains `GUIDE_W` (flat-flange version).
2. Every `Pxx_*.scad` wrapper resolves its `include` from its committed location. If `openscad` is on PATH, a quick `openscad -o tmp.stl P01_Q1.scad` proves it.
3. The repo has 20 STLs (P00, P00b, P01–P18), each next to its wrapper.
4. No `.gcode`, lock files or shortcuts are tracked (`git status` is clean after the ignores).
5. Optionally, in `manual/` (Git Bash or WSL):
   - copy `../Models/lfh_v1_reference.scad` to `lfh_ref.scad`
   - export all parts with `export.sh`
   - run `python checks.py`, which should report all six `*_pass True`
   - run `node pdf.js`, which should rebuild the v5 PDF
6. **Suggested commits:**
   1. Models and Test
   2. Documents
   3. Manual pipeline and images
   4. Slicer projects
   5. README, CLAUDE.md, ignores and HANDOVER
7. Push to the remote Joe gives you.
8. Only after Joe confirms the push, ask before deleting `_from_chat\`. Deletion on his machine needs his permission.

---

## 12. Status and open items (20 Nov 2026)

- ✅ **Design:** finished and verified at the measured dimensions. Interference, slide paths, wrong-swap clash, bayonet, visor, bed fit and the overhang scan all pass.
- ✅ **Fit tests:** P00/P00b printed, all green on 17 Nov. No tuning needed.
- 🖨️ **Printing:** g-code exists for P00–P12. Ask Joe how far he's got.
- ⚠️ **`slicer/3mf/P01.3mf`:** may hold the pre-flat-flange P01, so re-import P01–P04 if so.
- ⚠️ **Online manual artifact:** stale. The PDF v5 is the reference.
- ⚠️ **Manual renders:** made from the 31 Oct STLs. The old 1 mm groove isn't visible at that scale; re-render only if it matters.
- ⏳ **Clear PETG visor:** the settings are untested. PETG prints a hair fat, so file a snug knob joint. Superglue grips PETG less well, so scuff first or use epoxy for the magnets.
- ⏳ **Air spreader:** add only if the flame test shows the bottom row leaning harder.
