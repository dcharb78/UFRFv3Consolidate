
import subprocess, os, json, sys

def run(path):
    r = subprocess.run(["python", path], capture_output=True, text=True, timeout=240)
    print("\n>>>", path)
    print(r.stdout.strip())
    if r.stderr: print("[stderr]\n", r.stderr.strip())
    return {"rc": r.returncode, "out": r.stdout, "err": r.stderr}

arts = {}
for s in [
    "validations/maxwell_bianchi.py",
    "validations/dirac_checks.py",
    "validations/ym_gate_invariance.py",
    "validations/ppn_match.py",
    "validations/projection_fit_demo.py",
    "validations/nuclear_magic_check.py"
]:
    arts[s]=run(s)

os.makedirs("artifacts", exist_ok=True)
with open("artifacts/summary.json","w") as f:
    json.dump(arts, f, indent=2)
print("\nSaved artifacts/summary.json")
