#!/usr/bin/env python3
import json, math, os

# Fundamental weights for SU(3) in (H1,H2) basis (normalized informally)
# ω1 ~ (1, 0), ω2 ~ (1/2, √3/2)
weights = [
    {"label":"w1", "H1":1.0,  "H2":0.0},
    {"label":"w2", "H1":0.5,  "H2":0.8660254037844386},
    {"label":"w3", "H1":-1.5, "H2":-0.8660254037844386}, # -w1 - w2
]

# Three SU(2) subgroups embedded in SU(3): (12), (13), (23)
subgroups = [
    {"pair":"12", "generators":["λ1","λ2","λ3"]},
    {"pair":"13", "generators":["λ4","λ5","(λ3+√3 λ8)/2"]},
    {"pair":"23", "generators":["λ6","λ7","(-λ3+√3 λ8)/2"]},
]

def halfspin_26():
    # 13 phases times 2 (half‑spin) → 26 indices
    out = []
    idx=1
    for n in range(13):
        theta = 2.0*math.pi*n/13.0
        for half in [0,0.5]:
            out.append({"index":idx,"phase_n":n,"half":half,"theta":theta + half*math.pi})
            idx += 1
    return out

def main():
    mapping = {
        "weights": weights,
        "subgroups": subgroups,
        "halfspin_26": halfspin_26(),
        "notes": "Associates SU(3) weight points with UFRF 26 half‑spin labels; use to tag spectral/loop features."
    }
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/su3_halfspin_map.json","w") as f:
        json.dump(mapping, f, indent=2)
    print("Wrote artifacts/su3_halfspin_map.json")

if __name__ == "__main__":
    main()
