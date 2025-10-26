
# UFRF – ToE ProofKit v6 (Projection-Law CV added)

This extends v5 by adding a **projection-law cross‑validation** loader and runner that
consumes the LoCuSS-style technique split JSON you provided (with α priors), fits in
**difference space** y = ln M_{t1} − ln M_{t2} = d_M (α_{t1} − α_{t2}) S + ε, and
produces **held‑out predictions** and residuals.

## Quick Start (Projection CV)

```bash
export PYTHONPATH=$(pwd)
# Run synthetic LoCuSS-style demo (WL, HSE, SZ for 25 clusters)
python validations/projection_locusss_cv.py data/projection/locusss_splits.json data/projection/locusss_demo.csv
```

Outputs: `artifacts/projection_cv_summary.json` with per-split fits & held‑out predictions.
