
import subprocess, json, os

def run(path):
    r = subprocess.run(["python", path], capture_output=True, text=True, timeout=240)
    print("\n>>>", path)
    print(r.stdout.strip())
    if r.stderr: print("[stderr]", r.stderr.strip())
    return {"rc": r.returncode, "out": r.stdout, "err": r.stderr}

arts={}
arts["ppn_recursive_resonance.py"]=run("validations/ppn_recursive_resonance.py")
os.makedirs("artifacts", exist_ok=True)
with open("artifacts/run_all_v4.json","w") as f:
    json.dump(arts, f, indent=2)
print("\nSaved artifacts/run_all_v4.json")
