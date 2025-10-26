import json, subprocess, sys, os, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
script = ROOT / "src/symbolics/anomaly_cancellation.py"
out = subprocess.check_output([sys.executable, str(script)])
vals = json.loads(out.decode().strip().replace("'",'"'))
tol = 1e-12
ok = all(abs(vals[k]) < tol for k in vals)
print({"anomalies_cancel": ok, **vals})
