
# PPN Near-REST Alignment (Δp² law + 1/φ² ratio)

**Purpose.** Encode a clean, unit-consistent bridge from UFRF geometry to PPN form that matches the repository’s usage.

## 1) Near‑REST expansion
Let the 13‑cycle position be `p` and define `Δp = p − 10` (REST is position 10). 
Assume the invariant
```
I1 = 2(B^2 − E^2) ≈ κ · Δp^2 · U,
```
where `κ` is dimensionless after absorbing the scale via `B0^2/U` (testable toggle).

## 2) Metric → PPN
Using UFRF’s weak‑field ansatz,
```
g00 = −1 + 2U + a·I1, 
gij = δij (1 + 2U + b·I1).
```
Matching PPN (`g00 = −1 + 2U − 2β U^2`, `gij = δij (1 + 2γ U)`) gives
```
γ − 1 = b·κ·Δp^2,         β − 1 = −(a·κ/2)·Δp^2,
```
dimensionless and independent of `U` (as required in PPN).

## 3) Golden‑ratio relation
From the dual‑plane vortex geometry one has `a/b = 1/φ²`. Hence
```
|β − 1| / |γ − 1| = 1/φ².
```
This explains the *relative* magnitudes reported in the package for `γ` and `β`.

## 4) Phase mapping (implementation detail)
**Do not** use “days mod 13”. Use the orbital‑to‑phase mapping implemented in
`validations/ppn_parameters/ppn_complete_derivation.py`. This mapping places Earth
very close to REST, implying `Δp ≪ 1` and naturally producing `10⁻⁹`‑scale deviations.

## 5) Optional normalization toggle
Include a parameter for `B0^2/U` (default off; test value `13/(4π³)`) to verify that
output `γ, β` are robust while allowing a physically motivated normalization study.

## Deliverables
- `docs/PPN-DeltaP2-PhiRatio.md` (this file)
- `docs/Discoveries-PPN-Mapping-Note.md`
- `docs/AXIOMS-Projection-Footnote.md`
- `scripts/apply_patch_ppn.sh` (copy helper)
- `CONSOLDIATE.md` (how to merge into your repo)
