
# Gauge Projection & Running Couplings (IMVP‑013)

**Purpose.** Unify UFRF's projection law with standard RG running of couplings.
Show QED one‑loop β₀ = 2/(3π) and standard SU(N) Yang–Mills β₀, then apply the
projection law as an observer‑/technique‑dependent mapping to observables.

## 1) Running couplings
- QED: α(μ) = α(μ₀) / (1 − β₀ α(μ₀) ln(μ/μ₀)), with β₀ = 2/(3π).
- QCD: α_s(μ) ≈ 1 / (β₀ ln(μ^2/Λ^2)), with β₀ = (11 N_c − 2 N_f)/(12π).

## 2) Projection law (dimensionless coupling view)
For any intrinsic coupling g*:
```
ln g_obs = ln g* + d_M · α_tech · S
```
Use this **after** RG running, not on Δp itself. Sweep (d_M, α_tech, S) to see technique‑dependent variations.

## 3) How to run
```bash
python3 src/rg/run_couplings.py
```
Prints sample running for QED and QCD, then applies a projection mapping.
