# ADR‑0001: Identify UFRF log variable S with RG scale ln μ

## Status
Accepted

## Context
The UFRF projection law features a log‑scale variable **S**. To embed renormalization‑group (RG) structure, we require a principled identification between S and the field‑theoretic scale μ.

## Decision
We set **S ≡ ln(μ/μ₀)** up to an additive constant. Running couplings appear in `Z(Φ;S)`, `Θ(Φ;S)`, and fermion mass functional `𝓜(Φ;S)`. Discrete scale ratio **r=13/12** introduces small log‑periodic modulations on otherwise smooth RG flow.

## Consequences
- Reproduces a QED‑like one‑loop flow `dα/dS = (2N_f/3π) α²` in our linearized REST background (see `src/symbolics/rg_flows.py`).
- Predicts tiny log‑periodic ripples with period `ΔS = ln r` sourced by UFRF’s 13/26 structure.
- Keeps the projection law consistent with physical scale dependence of measurements.
