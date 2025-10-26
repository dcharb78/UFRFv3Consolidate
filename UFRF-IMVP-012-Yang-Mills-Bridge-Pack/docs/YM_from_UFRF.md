
# Yang–Mills from UFRF Geometry (IMVP‑012)

**Goal.** Make the bridge from dual‑plane E×B rotation to a non‑Abelian SU(2) (and
optionally SU(2)×SU(2)) gauge structure. Provide a toy computation of F = dA + g A∧A.

## 1) Mapping ideas
- Dual magnetic rotations (B, B') and the 26 half‑spin substructure suggest
  an SU(2)×SU(2) embedding; near REST, effective Abelianization is expected.
- Identify gauge potential components A^a_μ and structure constants f^{abc}.

## 2) Equations
- Field strength: F^a_{μν} = ∂_μ A^a_ν − ∂_ν A^a_μ + g f^{abc} A^b_μ A^c_ν
- Bianchi: D_[μ F^a_{νρ]} = 0
- Yang–Mills: D_μ F^{a μν} = J^{a ν}

## 3) Minimal toy check
`toy_su2_field.py` constructs a simple space‑dependent SU(2) potential and
computes F and a discrete Bianchi residual.

## 4) How to run
```bash
python3 src/ym/toy_su2_field.py
```
Outputs norms of F and Bianchi residuals; small residuals indicate consistent discretization.
