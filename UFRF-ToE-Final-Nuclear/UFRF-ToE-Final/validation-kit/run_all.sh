
#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=$(pwd)
python - <<'PY'
import json, os, sys, numpy as np
from src.common.io import write_json
# Collect quick results already computable without data
try:
    import importlib.util, numpy as _np
    spec = importlib.util.spec_from_file_location("em_metric","src/numerics/emergent_metric_solver.py")
    em_metric = importlib.util.module_from_spec(spec); spec.loader.exec_module(em_metric)
    g = em_metric.emergent_metric(_np.array([0.2,0,0]), _np.array([0,0.2,0]), _np.zeros(4), a=1e-3, b=5e-4, c=0.0)
    null_val = float(_np.array([-1.0,0,0,1.0]) @ (_np.linalg.inv(g) @ _np.array([-1.0,0,0,1.0])))
except Exception as e:
    null_val = None
# RG ripple sample
from src.symbolics.rg_flows import beta_qed_one_loop
c_coeff = 2.0/(3.0*np.pi)
results = {
  "principal_symbol_null_check": null_val,
  "beta_coeff_qed_one_loop_n1": float(c_coeff),
  "qhe_series_sample": __import__("src.numerics.qhe_plateaus_predictor", fromlist=['*']).fractional_series_13(6),
  "eta_over_s_enhanced": __import__("src.numerics.graphene_eta_s_ratio", fromlist=['*']).eta_over_s_enhanced(),
}
write_json("artifacts/results.json", results)
print(json.dumps(results, indent=2))
PY
