import sys, os, importlib
THIS = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

rec = importlib.import_module("src.symbolics.recovery_limits")
okM, _ = rec.maxwell_from_ufrf_limit()
okD, _ = rec.free_dirac_limit()
assert okM and okD, "Recovery limits failed"
print("WP‑C smoke: Maxwell and free Dirac limits verified symbolically.")
