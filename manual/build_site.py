#!/usr/bin/env python3
"""Generates site/index.html — LFH v1 visual build manual."""
import html

PARTS = [
 # id, img, code, name, qty, mat, bed face, walls, infill, brim, mass, note
 ("P00","print_coupons","coupons","Test coupons + gauge G1",1,"PLA","Flat","3","15%","none","62 g","Print first. Fit checks below."),
 ("P00b","print_GAUGE2","G2","Sleeve gauge G2",1,"PLA","Flat","3","15%","none","15 g","10-minute print."),
 ("P01","print_Q1","Q1","Box quarter, top-left",1,"PLA","Flange","4","15%","5 mm","259 g","Half fan hole. Supports: auto."),
 ("P02","print_Q2","Q2","Box quarter, top-right",1,"PLA","Flange","4","15%","5 mm","265 g","Half fan hole. Supports: auto."),
 ("P03","print_Q3","Q3","Box quarter, bottom-right",1,"PLA","Flange","4","15%","5 mm","341 g","Rear foot."),
 ("P04","print_Q4","Q4","Box quarter, bottom-left",1,"PLA","Flange","4","15%","5 mm","340 g","Rear foot."),
 ("P05","print_B1","B1","Back quarter (behind Q1)",1,"PLA","Outer face","3","15%","none","63 g","Ridges up."),
 ("P06","print_B2","B2","Back quarter (behind Q2)",1,"PLA","Outer face","3","15%","none","63 g","Ridges up."),
 ("P07","print_B3","B3","Back quarter (behind Q3)",1,"PLA","Outer face","3","15%","none","63 g","Ridges up."),
 ("P08","print_B4","B4","Back quarter (behind Q4)",1,"PLA","Outer face","3","15%","none","63 g","Ridges up."),
 ("P09","print_C1","C1","Clamp quarter, top-left",1,"PLA","Front face","4","15%","3 mm","92 g","Show face on the bed."),
 ("P10","print_C2","C2","Clamp quarter, top-right",1,"PLA","Front face","4","15%","3 mm","92 g","Show face on the bed."),
 ("P11","print_C3","C3","Clamp quarter, bottom-right",1,"PLA","Front face","4","15%","3 mm","92 g","Show face on the bed."),
 ("P12","print_C4","C4","Clamp quarter, bottom-left",1,"PLA","Front face","4","15%","3 mm","92 g","Show face on the bed."),
 ("P13","print_SOCKET","SOCKET","Fan socket",1,"PLA","Base flange","3","15%","none","135 g","Ledge carries the fan."),
 ("P14","print_RING","RING","Fan gasket ring",1,"TPU 95A","Flat","solid","100%","none","4 g","25–40 mm/s. Feed direct, not via CANVAS."),
 ("P15","print_BELL","BELL","Intake bell",1,"PLA","Mouth (grid)","3","15%","3 mm","189 g","Grid prints first."),
 ("P16","print_LID","LID","Intake lid",1,"PLA","Grille face","3","15%","none","96 g","Lugs chamfered, no support."),
 ("P17","print_V1","V1","Visor, left half",1,"Clear PLA / PETG","Canopy top","3","100%","none","177 g","Owns the jigsaw knobs. Clear PLA or clear PETG settings (section 4)."),
 ("P18","print_V2","V2","Visor, right half",1,"Clear PLA / PETG","Canopy top","3","100%","none","176 g","Clear PLA or clear PETG settings (section 4)."),
]

STAGES = [
 ("box","Box","Flange-down on a flat surface (glass, worktop, the printer plate). Every piece drops in from above; the surface is the end stop.", [
   ("s_q1","Start with Q1 and Q2",
     ["Stand <b>Q2</b> flange-down on the flat surface.",
      "Lower <b>Q1</b> in from above so its dovetail drops into Q2's slot."],
     "Both flanges sit flat. No rock."),
   ("s_q3","Add Q3",
     ["Lower <b>Q3</b> alongside Q2 the same way, sliding its slot down over Q2's tongue."],
     "The tongue disappears into the slot all the way to the surface."),
   ("s_q4","Q4 goes in last",
     ["Lower <b>Q4</b> into the gap. It engages two seams at once."],
     "All four flanges flat, seams closed. If Q4 refuses, something is in the wrong spot. That is the coding doing its job."),
   ("s_tube","Glue the box",
     ["Run thin superglue along every seam, inside and out, including the four flange seams.",
      "Leave it 10 minutes without moving it."],
     "Rap the walls. Nothing creaks or shifts."),
 ]),
 ("back","Back","Same flat surface. The back goes on rear-edge down into a silicone-filled channel.", [
   ("s_back","Assemble the back plate",
     ["Lay <b>B1–B4</b> ridges-up and press the jigsaw tabs together.",
      "Wick thin superglue along the cross seam."],
     "Plate flat. The U-channel runs unbroken all round."),
   ("s_backjoin","Fit the back",
     ["Run a continuous bead of neutral-cure silicone along the bottom of the U-channel.",
      "Lower the box in, rear edge first, and weight it."],
     "Silicone squeezes out on both sides all round. Leave 24 h."),
 ]),
 ("top","Top and seal","Box upright from here on.", [
   ("s_socket","Fit the fan socket",
     ["Glue the <b>socket</b> flange inside the engraved ring on the top (gland notch, if there is one, to the back).",
      "Run a silicone bead round the flange edge."],
     "Bead fully closed. No gaps at the top seam."),
   ("s_dip","Seal the inside",
     ["Mask the flange front face, where the gasket goes.",
      "Stir the tin, then brush 2–3 thin coats of Plasti Dip inside, through the front opening. Give each coat about 30 minutes."],
     "Torch inside: no bare seam lines. Peel the masking before it fully cures."),
 ]),
 ("front","Clamp, nuts, gasket","The filter seal is the only seal that really matters. Unfiltered air leaking here goes straight onto your work.", [
   ("s_clamp","Build the clamp frame",
     ["Front-face-down on the flat surface, lower <b>C1–C4</b> together like the box.",
      "Wick thin superglue into the four seams."],
     "Frame lies flat with no rock."),
   ("s_nuts","Fit the captive nuts",
     ["Drop an M4 nut into each of the 12 hex pockets on the back of the flange.",
      "Lock each with a drop of superglue (keep it out of the thread)."],
     "A bolt from the front picks up every nut."),
   ("s_epdm","Lay the gasket",
     ["Stick the 10 × 8 mm EPDM strip to the flange face with its <b>outer edge on the guide line</b>, starting and finishing at a bottom corner.",
      "Butt the ends tight and dab silicone on the join."],
     "Strip follows the guide line all round, not stretched at the corners."),
   ("s_filter","Mount the filter",
     ["Seat the filter on the gasket, <b>fibrous pre-filter face towards the box</b>.",
      "Fit the clamp and run the 12 bolts in a criss-cross until the clamp touches the flange all round."],
     "Clamp touches the flange everywhere. That is the designed squeeze: 5.5 mm at the thin spots, 2.5 mm at the thick ones. Stop tightening."),
 ]),
 ("visor","Visor","Detachable clear hood. It hangs by its rear lip on top of the clamp frame; the magnets just stop it getting knocked off.", [
   ("s_vglue","Join the visor halves",
     ["Canopy face down on the flat surface, lower <b>V2</b> onto V1's three jigsaw knobs.",
      "Wick thin superglue along the canopy seam, the strip and the front rib."],
     "Canopy flat across the seam. No step at the front edge."),
   ("s_mags","Clamp magnets",
     ["Glue a 6 × 3 mm magnet into each of the 8 pockets on the clamp front, <b>all the same pole facing out</b>.",
      "Test every one with a loose magnet before the glue goes off."],
     "The loose magnet pulls onto all 8 with the same face."),
   ("s_vfit","Visor magnets, the foolproof way",
     ["Stick one of the remaining 8 magnets onto each clamp magnet (it self-orients), and put a tiny dab of superglue at the bottom of each visor pocket.",
      "Hang the visor on by its lip, press it home for 60 s, then lift it off. The magnets come with it, the right way round."],
     "Visor clicks on, bolt heads land in their pockets, and it pulls off cleanly."),
 ]),
 ("fan","Fan and intake","", [
   ("s_fan","Seat the fan",
     ["Lay the <b>TPU ring</b> on the socket ledge.",
      "Lower the fan in, <b>airflow arrow pointing down</b>, gland towards the back."],
     "Fan sits level on the ring and doesn't rock."),
   ("s_bell","Fit the bell",
     ["Push the <b>bell</b> over the fan's intake end until the stop lip lands on the rim, gland through the notch."],
     "A gentle pull doesn't lift it."),
   ("s_bell","Disc and lid",
     ["Lay the Ø224 mm floss disc on the grid (carbon sheet underneath if you use one).",
      "Fit the <b>lid</b>: push down through the slots, twist clockwise to the stop."],
     "Lid won't lift. Disc edge clamped all round."),
 ]),
]

STAGES = [st for st in STAGES if st[0] != 'visor'] + [st for st in STAGES if st[0] == 'visor']

# Manifest: bought parts with Joe's photos and his listing names (verbatim).
# img, name, spec, qty, used for
BOUGHT = [
 ("m_fan","150mm Inline Duct Fan 500m3/h or greater","Ø150 mm duct. Body measured at 148.1 mm","1","Sits in the top socket, blowing down into the box"),
 ("m_speed","Plug In Variable Fan Speed Controller Dimmer","UK 3-pin plug-in. The fan plugs into it","1","Sets the fan speed for the flame test"),
 ("m_hepa","Replacement Filter set True HEPA For Levoit LV-PUR131 Air Purifier LV-PUR131S UK","HEPA panel 343 × 295 mm over the foam, 22–25 mm thick. The set's carbon panel isn't used on the front","1 set","Front face, under the clamp frame"),
 ("m_floss","1cm thick aquarium floss","50 × 50 cm sheet, 10 mm thick. One sheet gives 4 discs of Ø224 mm","1 sheet","Pre-filter disc in the intake bell"),
 ("m_epdm","Neoprene Self Adhesive Foam Sponge Strip Roll Tape Door Seal EPDM Weather Strips","10 mm wide × 8 mm thick, solid sponge (not hollow D-section)","~1.4 m","Filter gasket, on the flange face along the guide line"),
 ("m_bolts","M4 socket cap bolts","M4 × 40 mm, ISO 4762. 3 mm hex key","12","Clamp frame to the box flange"),
 ("m_nuts","M4 hex nuts","M4, 7 mm across flats, 3.2 mm thick (ISO 4032)","12","Captive pockets behind the flange"),
 ("m_magnets","Magnets, Ø6 × 3 mm disc (N42 or stronger)","Ø6 × 3 mm disc, N42 or stronger","16","8 in the clamp front, 8 in the visor"),
 ("m_plastidip","Plasti Dip","Brush-on, 250 ml tin (not the spray)","1 tin","Sealing coat inside the box"),
]
# No picture: item, spec, qty, used for, search term
NOPIC = [
 ("PLA filament","1.75 mm. PLA+ is fine","≈2.3 kg","Box, back, clamp, socket, bell, lid, test parts","PLA filament 1.75mm"),
 ("Clear PLA or clear PETG filament","1.75 mm. PETG settings in section 4","≈0.35 kg (PETG ≈0.36 kg)","Visor halves V1, V2","clear PETG filament 1.75mm"),
 ("TPU filament","95A, 1.75 mm","~5 g","Fan gasket ring","TPU 95A filament 1.75mm"),
 ("Thin cyanoacrylate (superglue)","Water-thin","1 bottle","Every seam, the nuts, the magnets","thin Cyanoacrylate"),
 ("Silicone sealant","Neutral-cure, low-odour. Not the vinegar-smelling acetoxy type","1 small tube","Back channel, socket flange, gasket join","neutral cure silicone"),
]
# Kit for the bench: tools and odds you'll already have, not bought for the build
BENCH = [
 ("Flat surface","Glass, worktop or the printer plate. It's the end stop for every slide-together joint"),
 ("3 mm hex key","For the M4 socket caps"),
 ("Masking tape","Masks the flange face before the Plasti Dip"),
 ("Small paintbrush","For the brush-on Plasti Dip"),
 ("Sharp knife or scissors","Cuts the floss disc and the EPDM strip"),
 ("Lighter and incense stick","The flame and smoke tests"),
]

def bought_card(b):
    img,name,spec,qty,use = b
    return f'''<article class="mitem">
  <figure class="plate"><img src="img/{img}.png" alt="{esc(name)}"></figure>
  <div class="mbody">
    <div class="mqty mono">× {esc(qty)}</div>
    <h3>{esc(name)}</h3>
    <p class="mspec">{esc(spec)}</p>
    <p class="note">{esc(use)}</p>
  </div>
</article>'''

def nopic_rows():
    return ''.join(f'<tr><td><b>{esc(i)}</b><br><span class="note">{esc(u)}</span></td><td>{esc(s)}</td><td class="num">{esc(q)}</td><td><code class="search">{esc(t)}</code></td></tr>' for i,s,q,u,t in NOPIC)

def bench_rows():
    return ''.join(f'<li><b>{esc(i)}</b> · {esc(u)}</li>' for i,u in BENCH)

def esc(s): return html.escape(s, quote=True)

def part_card(p):
    pid,img,code,name,qty,mat,face,walls,infill,brim,mass,note = p
    tpu = ' tpu' if 'TPU' in mat else ''
    return f'''<article class="part{tpu}">
  <figure class="plate"><img src="img/{img}.png" alt="{esc(name)} in print pose on a 256 mm bed" width="560"></figure>
  <div class="pbody">
    <div class="pid"><span class="mono">{pid}</span><span class="code mono">{esc(code)}</span></div>
    <h3>{esc(name)}</h3>
    <dl class="specs">
      <div><dt>Bed face</dt><dd>{esc(face)}</dd></div>
      <div><dt>Walls</dt><dd>{walls}</dd></div>
      <div><dt>Infill</dt><dd>{infill}</dd></div>
      <div><dt>Brim</dt><dd>{brim}</dd></div>
      <div><dt>Material</dt><dd>{esc(mat)}</dd></div>
      <div><dt>Mass</dt><dd>{mass}</dd></div>
    </dl>
    <p class="note">{esc(note)}</p>
  </div>
</article>'''

def steps_html():
    out=[]; n=0
    for sid,title,intro,steps in STAGES:
        out.append(f'<section class="stage" id="stage-{sid}"><div class="stagehead"><h3>{esc(title)}</h3>' + (f'<p>{intro}</p>' if intro else '') + '</div><ol class="steps">')
        for img,head,acts,check in steps:
            n+=1
            acts_html=''.join(f'<li>{a}</li>' for a in acts)
            out.append(f'''<li class="step" id="step-{n}">
  <figure class="plate"><img src="img/{img}.png" alt="Step {n}: {esc(head)}"></figure>
  <div class="sbody">
    <div class="snum mono">{n:02d}</div>
    <h4>{esc(head)}</h4>
    <ul class="acts">{acts_html}</ul>
    <p class="check"><span>Check</span>{check}</p>
  </div>
</li>''')
        out.append('</ol></section>')
    return '\n'.join(out), n

steps, nsteps = steps_html()
nsteps_total = nsteps + 2  # + test steps

GRID_SVG = '''<svg class="grid9" viewBox="0 0 380 330" role="img" aria-label="Filter face with a 3 by 3 grid of measuring points">
  <rect x="2" y="2" width="376" height="326" rx="4" class="g-clamp"/>
  <rect x="27" y="27" width="326" height="276" class="g-media"/>
  <g class="g-dots">
    <circle cx="81" cy="73" r="9"/><circle cx="190" cy="73" r="9"/><circle cx="299" cy="73" r="9"/>
    <circle cx="81" cy="165" r="9"/><circle cx="190" cy="165" r="9"/><circle cx="299" cy="165" r="9"/>
    <circle cx="81" cy="257" r="9"/><circle cx="190" cy="257" r="9"/><circle cx="299" cy="257" r="9"/>
  </g>
  <text x="190" y="320" text-anchor="middle" class="g-lab">Lighter 5–10 cm out at each point · flame leans ~45° and holds steady</text>
</svg>'''

PAGE = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LFH v1 Build Manual</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root {{
  /* Workshop manual: cool steel neutrals, clamp-orange for sequence and checks, renders on light plates. */
  --bg: #EDF0F3;
  --panel: #FFFFFF;
  --ink: #16202B;
  --muted: #586777;
  --line: #D2D9E1;
  --accent: #B8561F;
  --steel: #46658A;
  --plate: #F8F8F8;
  --ok: #2F7A55;
  --display: "Barlow Condensed", "Arial Narrow", "Roboto Condensed", sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #0F151C; --panel: #17202A; --ink: #E5EBF1; --muted: #98A6B4; --line: #2A3643;
    --accent: #E9814A; --steel: #86A9CD; --plate: #F3F4F5; --ok: #62C493; color-scheme: dark;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #0F151C; --panel: #17202A; --ink: #E5EBF1; --muted: #98A6B4; --line: #2A3643;
  --accent: #E9814A; --steel: #86A9CD; --plate: #F3F4F5; --ok: #62C493; color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font: 400 16px/1.55 var(--body); }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 20px 64px; }}
.mono {{ font-family: var(--mono); font-variant-numeric: tabular-nums; }}
h1, h2, h3, h4 {{ font-family: var(--display); font-weight: 600; line-height: 1.05; margin: 0; text-wrap: balance; letter-spacing: 0.01em; }}
h2 {{ font-size: 2.1rem; text-transform: uppercase; }}
h3 {{ font-size: 1.45rem; }}
h4 {{ font-size: 1.3rem; }}
p {{ margin: 0; max-width: 65ch; }}
a {{ color: var(--steel); }}
a:focus-visible, button:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
img {{ max-width: 100%; height: auto; display: block; }}
.plate {{ margin: 0; background: var(--plate); border-radius: 6px; display: grid; place-items: center; padding: 10px; }}

/* masthead */
header.mast {{ padding: 36px 0 22px; display: grid; gap: 22px; }}
.mast .kicker {{ font: 500 0.8rem/1 var(--mono); color: var(--accent); letter-spacing: 0.08em; text-transform: uppercase; }}
.mast h1 {{ font-size: clamp(2.6rem, 7vw, 4.4rem); text-transform: uppercase; }}
.mast .lede {{ color: var(--muted); font-size: 1.05rem; }}
.facts {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 6px; overflow: hidden; }}
.facts div {{ background: var(--panel); padding: 12px 14px; display: grid; gap: 2px; }}
.facts b {{ font: 600 1.6rem/1 var(--display); font-variant-numeric: tabular-nums; }}
.facts span {{ color: var(--muted); font-size: 0.85rem; }}
.heroes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }}
.heroes figure {{ margin: 0; display: grid; gap: 6px; }}
.heroes .plate {{ height: 100%; }}
.heroes figcaption {{ font-size: 0.85rem; color: var(--muted); }}
nav.toc {{ display: flex; flex-wrap: wrap; gap: 8px; padding: 14px 0 6px; border-top: 1px solid var(--line); }}
nav.toc a {{ font: 500 0.85rem/1 var(--mono); text-decoration: none; color: var(--ink); background: var(--panel); border: 1px solid var(--line); padding: 8px 10px; border-radius: 4px; }}
nav.toc a:hover {{ border-color: var(--accent); }}

section.block {{ padding-top: 44px; display: grid; gap: 18px; }}
.blockhead {{ display: grid; gap: 8px; border-bottom: 2px solid var(--ink); padding-bottom: 10px; }}
.blockhead p {{ color: var(--muted); }}

/* measure */
.measure {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; }}
.mcard {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 16px; display: grid; gap: 10px; align-content: start; }}
.mcard h3 {{ display: flex; gap: 10px; align-items: baseline; }}
.mcard h3 .mono {{ color: var(--accent); font-size: 0.9rem; }}
.mcard ul {{ margin: 0; padding-left: 18px; display: grid; gap: 4px; }}
.mcard code, td code {{ font-family: var(--mono); font-size: 0.85em; background: var(--bg); padding: 1px 4px; border-radius: 3px; }}

/* parts */
.parts {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }}
.part {{ min-width: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; overflow: hidden; display: grid; grid-template-rows: auto 1fr; }}
.part .plate {{ border-radius: 0; aspect-ratio: 4 / 3; display: block; padding: 8px; }}
.part .plate img {{ width: 100%; height: 100%; object-fit: contain; }}
.part.tpu {{ border-color: #B23A48; }}
.pbody {{ padding: 12px 14px 14px; display: grid; gap: 8px; align-content: start; }}
.pid {{ display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--muted); }}
.pid .code {{ color: var(--accent); }}
.specs {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px 10px; margin: 0; }}
.specs div {{ display: grid; }}
.specs dt {{ font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); }}
.specs dd {{ margin: 0; font-weight: 500; font-size: 0.92rem; }}
.note {{ font-size: 0.88rem; color: var(--muted); }}

table.petg {{ table-layout: fixed; }}
table.petg td {{ white-space: normal; overflow-wrap: anywhere; }}
/* manifest */
.subhead {{ font-family: var(--display); font-size: 1.35rem; text-transform: uppercase; color: var(--steel); padding-top: 6px; }}
.mitems {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 12px; }}
.mitem {{ min-width: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; overflow: hidden; display: grid; grid-template-rows: auto 1fr; }}
.mitem .plate {{ border-radius: 0; aspect-ratio: 4 / 3; display: block; padding: 10px; background: #FFFFFF; }}
.mitem .plate img {{ width: 100%; height: 100%; object-fit: contain; }}
.mbody {{ padding: 12px 14px 14px; display: grid; gap: 6px; align-content: start; }}
.mbody h3 {{ font-family: var(--body); font-size: 0.98rem; font-weight: 600; line-height: 1.3; letter-spacing: 0; }}
.mqty {{ color: var(--accent); font-size: 1.05rem; }}
.mspec {{ font-size: 0.9rem; }}
code.search {{ font-family: var(--mono); font-size: 0.85em; background: var(--bg); padding: 2px 6px; border-radius: 3px; border: 1px solid var(--line); white-space: nowrap; }}
ul.bench {{ margin: 0; padding-left: 18px; display: grid; gap: 4px; }}
.callout ul.bench b {{ font-family: var(--body); font-size: inherit; font-weight: 600; letter-spacing: 0; }}

/* tables */
.tablewrap {{ overflow-x: auto; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; }}
table {{ border-collapse: collapse; width: 100%; min-width: 560px; font-size: 0.93rem; }}
th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 600 0.78rem/1.2 var(--body); text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); background: var(--bg); }}
tr:last-child td {{ border-bottom: 0; }}
td.num {{ font-family: var(--mono); font-variant-numeric: tabular-nums; white-space: nowrap; }}
td .must {{ color: var(--accent); font-weight: 600; }}
.two {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; align-items: start; }}

/* steps */
.stage {{ display: grid; gap: 12px; }}
.stagehead {{ display: grid; gap: 4px; padding-top: 12px; }}
.stagehead h3 {{ font-size: 1.6rem; text-transform: uppercase; color: var(--steel); }}
.stagehead p {{ color: var(--muted); }}
ol.steps {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }}
.step {{ min-width: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); overflow: hidden; }}
.step .plate {{ border-radius: 0; min-height: 220px; }}
.step .plate img {{ width: 100%; max-height: 360px; object-fit: contain; }}
.sbody {{ padding: 16px 18px 18px; display: grid; gap: 10px; align-content: start; }}
.snum {{ font-size: 2.2rem; line-height: 1; color: var(--accent); font-family: var(--display); font-weight: 700; }}
ul.acts {{ margin: 0; padding: 0; list-style: none; display: grid; gap: 8px; counter-reset: act; }}
ul.acts li {{ counter-increment: act; position: relative; padding-left: 32px; }}
ul.acts li::before {{ content: counter(act); position: absolute; left: 0; top: 1px; font: 600 0.8rem/1 var(--mono); width: 22px; height: 22px; display: grid; place-items: center; border: 1.5px solid var(--ink); border-radius: 50%; }}
.check {{ border-left: 4px solid var(--ok); background: var(--bg); padding: 8px 12px; border-radius: 0 4px 4px 0; font-size: 0.95rem; }}
.check span {{ display: block; font: 600 0.72rem/1.4 var(--mono); text-transform: uppercase; letter-spacing: 0.08em; color: var(--ok); }}

/* test */
.grid9 {{ width: 100%; max-width: 420px; height: auto; }}
.g-clamp {{ fill: #C2612A; }}
.g-media {{ fill: #E9ECEF; }}
.g-dots circle {{ fill: var(--steel); }}
.g-lab {{ font: 500 11px var(--mono); fill: #ffffff; }}
.testcard {{ background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 16px; display: grid; gap: 12px; }}
.callout {{ background: var(--panel); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 0 6px 6px 0; padding: 14px 16px; display: grid; gap: 6px; }}
.callout b {{ font-family: var(--display); font-size: 1.15rem; font-weight: 600; letter-spacing: 0.02em; }}
footer {{ margin-top: 48px; padding-top: 16px; border-top: 1px solid var(--line); color: var(--muted); font-size: 0.85rem; display: grid; gap: 4px; }}

@media print {{
  nav.toc {{ display: none; }}
  .stage, ol.steps, section.block, .two {{ display: block; }}
  ol.steps > li, .stage > *, section.block > *, .two > * {{ margin-bottom: 12px; }}
  .step {{ display: block; }}
  .step .plate img {{ max-height: 230px; margin: 0 auto; }}
  .step .plate {{ min-height: 0; padding: 6px; }}
  .sbody {{ padding: 10px 14px 12px; gap: 6px; }}
  .blockhead, .step, .part, .mitem, .testcard, .mcard, .callout, tr, .heroes figure {{ break-inside: avoid; page-break-inside: avoid; }}
  .stagehead, .blockhead {{ break-after: avoid; page-break-after: avoid; }}
  section.block {{ padding-top: 20px; }}
  #manifest {{ break-before: page; page-break-before: always; }}
  .subhead {{ break-after: avoid; page-break-after: avoid; }}
  .keep {{ break-inside: avoid; page-break-inside: avoid; }}
  #manifest .mitems {{ display: block; font-size: 0; }}
  #manifest .mitem {{ display: inline-grid; width: calc((100% - 16px) / 3); margin: 0 8px 8px 0; vertical-align: top; font-size: 16px; }}
  #manifest .mitem:nth-child(3n) {{ margin-right: 0; }}
  #manifest .mitem .plate {{ aspect-ratio: 3 / 1; padding: 4px; }}
  .mbody {{ padding: 8px 10px 10px; gap: 4px; }}
  .mbody h3 {{ font-size: 0.85rem; }}
  .mspec, .mbody .note {{ font-size: 0.78rem; }}
}}
@media (max-width: 760px) {{
  table.stack {{ min-width: 0; }}
  table.stack thead {{ display: none; }}
  table.stack tr {{ display: grid; grid-template-columns: 1fr auto; gap: 4px 12px; padding: 12px; border-bottom: 1px solid var(--line); }}
  table.stack tr:last-child {{ border-bottom: 0; }}
  table.stack td {{ border: 0; padding: 0; }}
  table.stack td:nth-child(3) {{ grid-column: 2; grid-row: 1; }}
  table.stack td:nth-child(2), table.stack td:nth-child(4) {{ grid-column: 1 / -1; }}
  .facts {{ grid-template-columns: 1fr 1fr; }}
  .facts div:last-child {{ grid-column: 1 / -1; }}
  .heroes {{ grid-template-columns: 1fr 1fr; }}
  .heroes figure:last-child {{ grid-column: 1 / -1; }}
  .step {{ grid-template-columns: 1fr; }}
  .step .plate {{ min-height: 0; }}
  h2 {{ font-size: 1.8rem; }}
}}
@media (max-width: 420px) {{
  .wrap {{ padding: 0 16px 48px; }}
  .specs {{ grid-template-columns: 1fr 1fr; }}
}}
</style>
</head>
<body>
<div class="wrap">

<header class="mast">
  <div class="kicker">Laminar flow hood · v1 final · measured parts · Centauri Carbon 2</div>
  <h1>LFH v1 Build Manual</h1>
  <p class="lede">A fully printed, Gordotek-style hood: HEPA filter on the front, 150 mm inline fan blowing down into a sealed box, with an intake bell and pre-filter on top, and a detachable clear visor on 6 × 3 mm magnets. Built to the measured parts: a 343 × 295 HEPA and a 148 mm fan. Every check in the reference model passes at these sizes.</p>
  <div class="facts">
    <div><b class="mono">343 × 295</b><span>HEPA over foam, landscape (mm)</span></div>
    <div><b>20</b><span>printed parts, 18 support-free</span></div>
    <div><b>≈2.3 kg</b><span>PLA, + 0.35 kg clear PLA or PETG, a dab of TPU</span></div>
    <div><b>12 × M4×40</b><span>socket caps + captive nuts</span></div>
    <div><b class="mono">45°</b><span>steady flame lean: the pass mark</span></div>
  </div>
  <div class="heroes">
    <figure><div class="plate"><img src="img/hero.png" alt="Finished hood from the front" width="608"></div><figcaption>Front: clear visor over the clamp frame and filter.</figcaption></figure>
    <figure><div class="plate"><img src="img/hero_rear.png" alt="Finished hood from the rear" width="624"></div><figcaption>Rear: jigsaw back, rear feet, visor wing.</figcaption></figure>
    <figure><div class="plate"><img src="img/exploded.png" alt="Exploded view of every part" width="621"></div><figcaption>Exploded: every part in its place.</figcaption></figure>
  </div>
  <nav class="toc" aria-label="Sections">
    <a href="#manifest">1 · Manifest</a><a href="#measure">2 · Measured</a><a href="#parts">3 · Printed parts</a><a href="#settings">4 · Print settings</a><a href="#coupons">5 · Fit test</a><a href="#assembly">6 · Assembly</a><a href="#test">7 · Test</a>
  </nav>
</header>

<section class="block" id="manifest">
  <div class="blockhead"><h2>1 · Manifest</h2><p>Everything you need before the first print, apart from the printer. Photos and names are the actual listings used for this build.</p></div>
  <h3 class="subhead">Bought parts</h3>
  <div class="mitems">
{''.join(bought_card(b) for b in BOUGHT)}
  </div>
  <div class="keep">
  <h3 class="subhead">Filament and consumables</h3>
  <div class="tablewrap"><table class="stack">
    <thead><tr><th>Item</th><th>Spec</th><th>Qty</th><th>Search for</th></tr></thead>
    <tbody>{nopic_rows()}</tbody></table></div>
  </div>
  <div class="callout"><b>Kit for the bench</b><ul class="bench">{bench_rows()}</ul></div>
</section>

<section class="block" id="measure">
  <div class="blockhead"><h2>2 · Measured</h2><p>Taken from the real parts on 31 Oct 2026. Every part in this manual is built from these numbers.</p></div>
  <div class="tablewrap"><table>
    <thead><tr><th>Part</th><th>Measurement</th><th>Value</th><th>Used for</th></tr></thead>
    <tbody>
      <tr><td>HEPA</td><td>Over the edge foam</td><td class="num">343 × 295</td><td>Clamp walls, 0.5 mm clearance so they just kiss the foam</td></tr>
      <tr><td>HEPA</td><td>Cardboard frame</td><td class="num">339 × 291</td><td>Gasket position, box opening</td></tr>
      <tr><td>HEPA</td><td>Frame border, fibrous face</td><td class="num">10.8</td><td>10 mm gasket, outer edge flush with the cardboard edge</td></tr>
      <tr><td>HEPA</td><td>Thickness</td><td class="num">22–25</td><td>Designed at 22. The gasket takes up the rest</td></tr>
      <tr><td>Fan</td><td>Diameter, end to end</td><td class="num">148.1</td><td>Socket bore 148.6, bell sleeve 148.5</td></tr>
      <tr><td>Fan</td><td>Length</td><td class="num">150</td><td></td></tr>
      <tr><td>Fan</td><td>Cable gland</td><td class="num">98 up from the outlet, Ø11.5</td><td>Clear of the socket and the bell, so neither needs a cut-out</td></tr>
    </tbody></table></div>
</section>

<section class="block" id="parts">
  <div class="blockhead"><h2>3 · Printed parts</h2><p>Each card shows the part in its print pose on a 256 mm bed. Codes are debossed on the parts. Quarters are numbered clockwise <b>as seen from the front</b>: 1 top-left, 2 top-right, 3 bottom-right, 4 bottom-left.</p></div>
  <div class="parts">
{''.join(part_card(p) for p in PARTS)}
  </div>
</section>

<section class="block" id="settings">
  <div class="blockhead"><h2>4 · Print settings</h2><p>ElegooSlicer or OrcaSlicer. Start from the stock CC2 <b>0.20 mm Standard</b> profile with your PLA preset, then change only these. Per-part walls, infill and brim are on the part cards.</p></div>
  <div class="tablewrap"><table>
    <thead><tr><th>Setting</th><th>Value</th><th>Why</th></tr></thead>
    <tbody>
      <tr><td>Nozzle / plate</td><td class="num">0.4 mm · textured PEI</td><td>Stock</td></tr>
      <tr><td>Layer / first layer</td><td class="num">0.20 / 0.20 mm</td><td></td></tr>
      <tr><td>Supports</td><td class="num"><span class="must">Off</span>, except <span class="must">P01 + P02: Auto</span></td><td>P01 and P02 need auto supports for the top of the fan hole. Every other part is support-free in its pose</td></tr>
      <tr><td>Elephant foot compensation</td><td class="num"><span class="must">0.15 mm</span></td><td>Joints and the gasket face start on the first layers</td></tr>
      <tr><td>Outer wall speed</td><td class="num">≤ 120 mm/s</td><td>Dovetail accuracy</td></tr>
      <tr><td>Seam</td><td class="num">Aligned</td><td>Keep it off dovetail faces. Paint it onto an outside corner if it wanders</td></tr>
      <tr><td>Sparse infill</td><td class="num">Gyroid 15%</td><td></td></tr>
      <tr><td>Top / bottom shells</td><td class="num">5 / 4</td><td></td></tr>
      <tr><td>Box quarter wall loops</td><td class="num">4</td><td>Makes the 3 mm walls solid, which helps airtightness</td></tr>
      <tr><td>Chamber / grille</td><td class="num">PLA preset</td><td>PLA wants cooling</td></tr>
      <tr><td>Visor (clear PLA)</td><td class="num">100% · 6/6 shells · +10 °C</td><td>Outer wall 60 mm/s, the rest ≤ 80, part fan about 50%. A smooth plate gives a glossier canopy; the textured plate frosts it. Expect translucent, not glass</td></tr>
      <tr><td>TPU ring</td><td class="num">95A · 25–40 mm/s · 100%</td><td>Stock TPU profile. If you run the CANVAS unit, feed TPU direct</td></tr>
    </tbody></table></div>
  <div class="keep">
  <h3 class="subhead">Clear PETG visor (P17, P18), instead of clear PLA</h3>
  <p class="note">Tougher than PLA and takes IPA wipe-downs better. Same STLs, same canopy-down pose, no supports. Start from the stock CC2 0.20 mm Standard process with the stock PETG filament profile, then change only these.</p>
  </div>
  <div class="tablewrap"><table class="petg">
    <colgroup><col style="width:22%"><col style="width:33%"><col style="width:45%"></colgroup>
    <thead><tr><th>Setting</th><th>Value</th><th>Why</th></tr></thead>
    <tbody>
      <tr><td>Filament prep</td><td class="num"><span class="must">Dry 65 °C · 4–6 h</span></td><td>Damp PETG bubbles and hazes, and clear shows every bubble. Print from a dry box</td></tr>
      <tr><td>Nozzle</td><td class="num">250 °C (first layer 245)</td><td>Hotter fuses the lines, and fused lines are what make it clear. Stay inside the spool's range</td></tr>
      <tr><td>Bed</td><td class="num">75 °C (first layer 80)</td><td></td></tr>
      <tr><td>Plate</td><td class="num">Textured PEI</td><td>Smooth PEI <b>only</b> with glue stick: PETG can weld to it and tear the coating. Smooth is glossier, textured frosts</td></tr>
      <tr><td>Walls / infill</td><td class="num">3 · 100% aligned rectilinear</td><td>No air gaps between lines</td></tr>
      <tr><td>Top / bottom shells</td><td class="num">6 / 6</td><td></td></tr>
      <tr><td>Flow ratio</td><td class="num"><span class="must">+3–5%</span></td><td>Squeezes out the gaps. Back off if the top surface ridges</td></tr>
      <tr><td>Speeds</td><td class="num">Outer 40 · inner 60 · infill 80 · first layer 20 mm/s</td><td>Slow lines lie down cleaner</td></tr>
      <tr><td>Part cooling fan</td><td class="num">30% (bridges/overhangs 80%)</td><td>Less fan, better fusion</td></tr>
      <tr><td>Retraction / wipe</td><td class="num">Stock PETG · wipe on</td><td>PETG strings</td></tr>
      <tr><td>Z-hop / ironing</td><td class="num">0.4 mm / off</td><td>No nozzle drag or haze on the clear faces</td></tr>
      <tr><td>Elephant foot / brim</td><td class="num">0.15 mm / none</td><td>As PLA</td></tr>
      <tr><td>Chamber / lid</td><td class="num">Closed is fine</td><td>PETG doesn't need the cooling PLA does</td></tr>
    </tbody></table></div>
  <div class="callout"><b>PETG notes</b><p>Expect frosted-clear rather than glass, usually a touch clearer than clear PLA. The visor clearances were proven in PLA and PETG prints a hair fat, so ease a snug V1/V2 knob joint with a file. Thin superglue grips PETG less reliably: scuff the faces first, or bed the magnets in 2-part epoxy.</p></div>
  <div class="callout"><b>Print order</b><p>P00 + P00b first. Then the box quarters (longest prints, about 227 mm tall), then everything else in any order.</p></div>
</section>

<section class="block" id="coupons">
  <div class="blockhead"><h2>5 · Fit test (P00, P00b)</h2><p>Half an hour of plastic before 30-odd hours of plastic. Any tweak goes back to the OpenSCAD project as a parameter change.</p></div>
  <div class="tablewrap"><table>
    <thead><tr><th>Test</th><th>Pass</th><th>If it fails</th></tr></thead>
    <tbody>
      <tr><td>S tongue into S slot</td><td>Slides home by hand, no slop</td><td>Tight: <code>CLR</code> +0.05. Sloppy: −0.05</td></tr>
      <tr><td>L tongue into S slot</td><td><span class="must">Must not go in</span></td><td>This is the anti-misassembly coding. Reduce <code>CLR</code></td></tr>
      <tr><td>Jigsaw tab</td><td>Presses in and holds flat</td><td><code>JIG_CLR</code> ±0.05</td></tr>
      <tr><td>M4 nut</td><td>Drops in, sits flush</td><td><code>NUT_AF</code> ±0.1</td></tr>
      <tr><td>M4 bolt</td><td>Passes freely, head sits in the counterbore</td><td><code>BOLT_HOLE</code> / <code>CB_D</code></td></tr>
      <tr><td>Gauge G1 on the fan body</td><td>Slides on with a whisker of clearance</td><td><code>SOCK_CLEAR</code></td></tr>
      <tr><td>Gauge G2 on the fan's intake end</td><td>Pushes on and grips</td><td>Grip-rib height (0.3)</td></tr>
    </tbody></table></div>
</section>

<section class="block" id="assembly">
  <div class="blockhead"><h2>6 · Assembly</h2><p>{nsteps} steps, each with no more than two actions and one check. Don't move on until the check passes. Everything you need is in section 1.</p></div>
{steps}
</section>

<section class="block" id="test">
  <div class="blockhead"><h2>7 · Test</h2><p>The plastic is finished. Two quick tests. A lighter and an incense stick, no lab kit.</p></div>
  <div class="two">
    <div class="testcard">
      <div class="snum mono">{nsteps+1:02d}</div>
      <h4>Flame test</h4>
      <ul class="acts"><li>With the visor on, hold a lighter flame 5–10 cm in front of the filter at each of the 9 points.</li><li>Turn the dial on the plug-in speed controller until the flame leans about 45° and settles.</li></ul>
      <p class="check"><span>Check</span>About 45° and dead steady at all 9 points. A flame that dances means turbulence, so adjust the speed until it settles. If it only dances near the edges, check the clamp seal. The usable zone ends roughly 19 cm (7.5 in) out from the filter.</p>
      {GRID_SVG}
    </div>
    <div class="testcard">
      <div class="snum mono">{nsteps+2:02d}</div>
      <h4>Smoke and plates</h4>
      <ul class="acts"><li>Draw an incense stick slowly round the clamp edge, then across the face.</li><li>Run an open-plate test in the airstream.</li></ul>
      <p class="check"><span>Check</span>Smoke runs straight out with no curl-back at the edges, and no smoke escapes round the clamp. Plates stay clean. An aftermarket "H13" label is a claim, and the plates are the test of it.</p>
      <div class="callout"><b>Air spreader inside the box</b><p>Not fitted in v1. If the flame leans much harder on the bottom row than the top, add a deflector under the fan outlet. Otherwise leave it out.</p></div>
    </div>
  </div>
</section>

<footer>
  <p>Renders are from the reference model at the measured dimensions. The OpenSCAD build spec is authoritative for geometry.</p>
  <p>Box, back and clamp can each only go together one way. If a piece won't go, it's in the wrong place.</p>
</footer>

</div>
</body>
</html>
'''
open('site/index.html','w').write(PAGE)
print("steps:", nsteps, "bytes:", len(PAGE))
