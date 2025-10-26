
# IMVP-031 — Fine Structure Projection Reproduction

This lightweight validation reproduces the **projection-law explanation** for the fine-structure ratio within UFRF.

**Core equation** (from the package):  
`ln O = ln O* + d_M · α · S + ε`

- `O*` — intrinsic (projection-free) value; here `α⁻¹* = 137.036303776`
- `O` — observed value from our scale
- `d_M = ln(M_obs/M_tgt)`, using `M_obs = 144000`, `M_tgt = 144` → `ln(1000)`
- `α` — technique coupling (0..1)
- `S` — systematic surrogate (signed)
- `ε` — random residual (mean 0)

We compute `α⁻¹_observed` across techniques and compare deltas against a target observed value (default: 137.035999084).

## Quick start

```bash
python3 src/fs_projection/repro.py --M_obs 144000 --M_tgt 144 --O_star 137.036303776   --alpha 0.3 --S -0.1 --target 137.035999084
```

Multiple techniques:

```bash
python3 src/fs_projection/repro.py --M_obs 144000 --M_tgt 144 --O_star 137.036303776   --tech "optical:0.30:-0.10" "electronic:0.50:-0.06" "xray:0.70:-0.04" "grav:0.90:-0.02"   --target 137.035999084
```

Outputs `artifacts/fs_projection_results.json` with per-tech projections and deltas.

## Files

- `src/fs_projection/repro.py` — main runner
- `artifacts/fs_projection_results.json` — results
- `tests/test_projection.py` — sanity checks (d_M and single-tech projection)

## Notes

- This script is **unit-free**; it numerically mirrors the projection relation laid out in UFRF docs.
- Use it to demonstrate **technique dependence** and verify sign/scale of the projection delta.
