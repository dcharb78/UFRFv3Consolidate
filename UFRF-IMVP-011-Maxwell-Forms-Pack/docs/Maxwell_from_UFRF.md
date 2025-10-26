
# Maxwell from UFRF Geometry (IMVP‑011)

**Goal.** Show how the UFRF E×B vortex picture maps to standard Maxwell equations
using differential forms and provide a minimal numerical check (plane wave).

## 1) Geometry → Forms
- UFRF core: E ⟂ B from distinct dimensional origins (1D vs 2D).
- Identify a U(1) gauge potential 1‑form \(A\); field strength \(F = dA\).
- Maxwell in vacuum: \(dF = 0\) (Bianchi), \(d\star F = J\) (sources).

Mapping:
- \(F\) contains (E,B) components; \(\star F\) encodes constitutive relations.
- REST (E=B) corresponds to perfect impedance matching (free space).

## 2) Minimal numerical demonstration
We construct a 1D plane wave solution \(E_x=E_0\cos(kx-\omega t), B_y=(E_0/c)\cos(kx-\omega t)\) and verify discrete forms of:
- \(\nabla\cdot B = 0\)
- \(\nabla\times E + \partial_t B = 0\)
- \(\nabla\cdot E = 0\) (vacuum case)
- \(\nabla\times B - \mu_0\epsilon_0\partial_t E = 0\) (vacuum case)

## 3) How to run
```bash
python3 scripts/maxwell_plane_wave_check.py
```
Outputs relative residuals for the four vacuum equations.

## 4) Notes
- Forms make gauge covariance manifest: \(A \mapsto A + d\lambda\) leaves \(F\) invariant.
- Near REST, UFRF predicts efficient energy translation consistent with Poynting flow.
