
import sys, os, importlib
THIS = os.path.dirname(__file__); ROOT = os.path.abspath(os.path.join(THIS, os.pardir))
sys.path.insert(0, ROOT)

dm = importlib.import_module("src.symbolics.disformal_metric_characteristics")
ok, info = dm.find_safe_bounds(10)
assert ok, f"Disformal metric failed safety scan: {info}"
print("WP‑D (linearized): disformal metric passes Lorentzian + subluminal scan in small‑parameter REST window.")
