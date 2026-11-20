#!/usr/bin/env python3
"""Full acceptance-check battery for LFH v1 (spec section 9). Prints a report and writes checks.json."""
import trimesh, itertools, numpy as np, json, warnings
warnings.filterwarnings("ignore")
R = {}
def load(d, n): return trimesh.load(f'stl_{d}/{n}.stl')
def iv(a, b):
    lo = np.maximum(a.bounds[0], b.bounds[0]); hi = np.minimum(a.bounds[1], b.bounds[1])
    if np.any(lo >= hi): return 0.0
    try:
        r = trimesh.boolean.intersection([a, b], engine='manifold')
        return 0.0 if r.is_empty else round(float(r.volume), 2)
    except Exception:
        return None
def moved(m, T):
    m = m.copy(); m.apply_transform(T); return m
def tr(v): return trimesh.transformations.translation_matrix(v)
def rot(deg, axis, pt): return trimesh.transformations.rotation_matrix(np.radians(deg), axis, pt)

# 1 bed fit
PRINT = "coupons GAUGE2 Q1 Q2 Q3 Q4 B1 B2 B3 B4 C1 C2 C3 C4 SOCKET RING BELL LID V1 V2".split()
bed = {}
for n in PRINT:
    m = load('print', n); e = m.bounds[1] - m.bounds[0]
    bed[n] = dict(env=[round(x, 1) for x in e], vol_cm3=round(m.volume/1000, 1),
                  watertight=bool(m.is_watertight), ok=bool(e.max() <= 250 and m.is_watertight))
R['bed_fit'] = bed
R['bed_fit_pass'] = all(v['ok'] for v in bed.values())

# 2 static interference
ASM = "Q1 Q2 Q3 Q4 B1 B2 B3 B4 C1 C2 C3 C4 SOCKET RING BELL LID FILTER EPDM DISC V1 V2 MAGS".split()
M = {n: load('asm', n) for n in ASM}
over = []
for a, b in itertools.combinations(ASM, 2):
    v = iv(M[a], M[b])
    if v is None or v > 0.5: over.append((a, b, v))
R['interference'] = over; R['interference_pass'] = len(over) == 0

# 3 slide paths (piece lowered onto the bench-side reference face = +Y offset)
slides = {}
for mv, fx in [("Q1","Q2"),("Q3","Q2"),("Q4","Q3"),("Q4","Q1"),("C1","C2"),("C3","C2"),("C4","C3"),("C4","C1")]:
    vals = [iv(moved(M[mv], tr([0, d, 0])), M[fx]) for d in (2, 5, 10, 25, 50, 100, 150, 200, 226)]
    slides[f"{mv}->{fx}"] = max(v if v is not None else 999 for v in vals)
R['slide'] = slides; R['slide_pass'] = all(v < 0.5 for v in slides.values())

# 4 wrong-swap blocking (180 deg about Y)
swaps = {}
for wrong, nb in [("Q3",["Q2","Q4"]),("Q4",["Q1","Q3"]),("B3",["B2","B4"]),("B4",["B1","B3"]),("C3",["C2","C4"]),("C4",["C1","C3"])]:
    r = moved(M[wrong], rot(180, [0,1,0], [0,0,0]))
    swaps[wrong] = max(iv(r, M[n]) or 0 for n in nb)
R['wrong_swap_clash_mm3'] = swaps; R['wrong_swap_pass'] = all(v > 50 for v in swaps.values())

# 6 bayonet
axis = [0, 113.5, 0]
twist_clear = [iv(moved(M['LID'], rot(th, [0,0,1], axis)), M['BELL']) for th in (0, 4, 8, 12, 17.5)]
past_stop = iv(moved(M['LID'], rot(-4, [0,0,1], axis)), M['BELL'])
lift = [iv(moved(moved(M['LID'], rot(17.5, [0,0,1], axis)), tr([0,0,dz])), M['BELL']) for dz in (1, 3, 6, 10, 15)]
R['bayonet'] = dict(twist=twist_clear, past_stop=past_stop, lift=lift)
R['bayonet_pass'] = max(twist_clear) < 0.5 and max(lift) < 0.5 and (past_stop or 0) > 5

# 8 visor
press = [iv(M['V1'], moved(M['V2'], tr([0,0,-d]))) for d in (0.5, 2, 10, 50)]
pull = []
for d in (1, 3, 10, 40):
    for v in ("V1","V2"):
        for n in ("C1","C2","MAGS"):
            pull.append(iv(moved(M[v], tr([0,-d,0])), M[n]) or 0)
bolts = load('asm','BOLTS')
R['visor'] = dict(press_on=press, pull_off_max=max(pull))
R['visor_pass'] = max(press) < 0.5 and max(pull) < 0.5

json.dump(R, open('checks.json','w'), indent=1, default=str)
for k in ['bed_fit_pass','interference_pass','slide_pass','wrong_swap_pass','bayonet_pass','visor_pass']:
    print(f"{k:20} {R[k]}")
print("interference:", R['interference'])
print("wrong-swap clash mm3:", R['wrong_swap_clash_mm3'])
print("bayonet:", R['bayonet'])
print("biggest envelopes:", sorted(((v['env'], n) for n, v in bed.items()), key=lambda x: -max(x[0]))[:4])
