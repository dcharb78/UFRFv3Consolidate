
# Runbook (Validations)

```bash
export PYTHONPATH=$(pwd)

# SU(3) gate + diagnostics
python validations/su3_gauge_invariance.py       # gate: W(L) invariance
python validations/su3_loop_spectra.py           # W(L) sequence + FFT (try Lmax=32/64)
python validations/su3_rest_abelianization.py    # ε-scan: commutator/derivative ratio

# Gravity / PPN example
python validations/ppn_sanity.py

# Projection-law synthetic demo
python validations/projection_synthetic.py
```
Artifacts are saved under `artifacts/` by default.
