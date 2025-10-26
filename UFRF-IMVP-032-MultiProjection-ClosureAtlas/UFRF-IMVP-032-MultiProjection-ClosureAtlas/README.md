# UFRF-IMVP-032 — Multi‑Projection Closure Atlas (Nuclear Magic Numbers)

This kit operationalizes the idea that **there isn’t one closure formula**; 
instead, closures appear as **concurrent projections** of the same S³/13‑cycle geometry.
It encodes *families* of candidate closures: 13‑cycle/14‑Law, triangular (T_n±k), 
2·T_n, **multiples of 13** (sub‑magic lane), and **SO(4)/tesseract markers** (16, 32)
that arise naturally from the SU(2)×SU(2) embedding.

## What’s here

- `formulas/closure_families.md` — definitions and when to use each family
- `formulas/projective_filters.py` — helpers to classify N into families
- `validations/run_ame2020_multi_projection.py` — drop‑in script to extend your AME‑2020 run
- `data/magic_numbers_baseline.csv` — canonical & sub‑magic set with family tags
- `patches/PATCH_GUIDE.md` — how to merge into your repo and publish artifacts

## Quick start

```bash
# (A) Dry run on the included baseline list
python3 formulas/projective_filters.py --scan data/magic_numbers_baseline.csv

# (B) Integrate with your AME‑2020 pipeline (example)
python3 validations/run_ame2020_multi_projection.py   --ame_csv path/to/AME2020.csv   --out artifacts/ame2020_multi_projection_report.json
```

## Family summary

- **14‑Law / 13‑cycle boundary (primary closures):** 2, 8, 20, 28, 50, 82, 126
- **Triangular projections:** `T_n - 1` → {2, 5, 8, 11, 14, 17, 20, …}; `T_n` → {1, 3, 6, 10, 15, 21, 28, …}; `2·T_n`
- **Multiples of 13 (sub‑magic lane):** 13·k → 26, 39, 52, 65, 78, 91, 104, 117
- **SO(4)/tesseract markers (SU(2)×SU(2) clue):** 16 (vertices), 32 (edges), 24 (squares), 8 (cubes)

Use the **union** of families, then gate by the **REST exclusion** (positions {0,5,10,12} mod 13)
and the **14‑Law hand‑off** (11‑12‑13 → 1‑2‑3) before calling a number “magic”.
