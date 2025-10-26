
import json, sys, importlib.util
from pathlib import Path

# Re-run the derivation module (ensures import works)
mod_path = Path(__file__).parent.parent/"src/symbolics/derive_eom_general.py"
spec = importlib.util.spec_from_file_location("derive_eom_general", str(mod_path))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Validate the saved report
report_path = Path(__file__).parent/"test_eom_general_results.json"
data = json.loads(report_path.read_text())

ok = all([
    data.get("em_with_sources_identity") is True,
    data.get("dirac_minimal_coupling_identity") is True,
    data.get("maxwell_limit_ok") is True
])

print("UFRF-ToE/test_eom_general.py:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
