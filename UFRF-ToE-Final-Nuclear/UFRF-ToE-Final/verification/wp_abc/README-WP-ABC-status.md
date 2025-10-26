# UFRF-ToE — WP‑A/B/C Verification Snapshot

This snapshot contains symbolic derivations and executable tests showing that the UFRF action
recovers Maxwell's equations (with sources) and the free Dirac equation in the appropriate limits.

## What was verified (executed in this environment)

- **Euler–Lagrange (A_ν)** from L = -¼ Z(φ) F² - ¼ Θ(φ) F·F~ - J^μ A_μ gives
  ∂_μ (Z F^{μν} + Θ F~^{μν}) = J^ν.  (Derived symbolically.)
- **Canonical momentum** π^{μν} = ∂L/∂(∂_μ A_ν) equals −(Z F^{μν} + Θ F~^{μν}).
- **Bianchi identity** ∂_{[α} F_{βγ]} = 0 (symbolically zero).
- **Gauge invariance of F** under A → A + ∂χ (exact).
- **Dirac dispersion** det(γ·p − m) = (p² − m²)² (exact).

## How to run

```bash
python src/symbolics/derive_eom_full.py   # prints a JSON result summary
python tests/test_eom_limits.py           # prints 'ALL TESTS PASSED' on success
```

## Files of interest

- `src/symbolics/derive_eom_full.py` — symbolic derivation and checks for EM+Θ term and Dirac dispersion.
- `tests/test_eom_limits.py` — lightweight test runner (no pytest needed).

Generated: 2025-10-19 04:51:04
