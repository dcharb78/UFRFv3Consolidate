
# IMVP‑019 — Projection Law Monte Carlo (Technique Dependence)

**Purpose.** Demonstrate that technique‑dependent couplings (α_E, α_B) induce
predictable spreads in observables *after* RG running, per the projection law.

**What this does**
- Samples techniques with α_E, α_B and computes α_total = √(α_E²+α_B²).
- Applies ln O = ln O* + d_M α_total S + ε to produce synthetic observations.
- Prints summary statistics and writes `artifacts/projection_mc.json`.

**Run**
```bash
python3 src/projection/mc_projection.py --dM 6.907 --S -0.10 --n 2000
```
