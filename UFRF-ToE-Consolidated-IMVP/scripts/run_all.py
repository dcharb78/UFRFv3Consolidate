
import os, subprocess, sys
def run(cmd):
    print("\n>>>", cmd); sys.stdout.flush()
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(r.stdout); 
    if r.stderr: print("[stderr]", r.stderr)
    return r.returncode
os.environ["PYTHONPATH"]=os.getcwd()
rc=0
rc |= run("python validations/maxwell_bianchi.py")
rc |= run("python validations/ppn_sanity.py")
rc |= run("python validations/projection_synthetic.py")
rc |= run("python validations/su3_gauge_invariance.py")
rc |= run("python validations/su3_loop_spectra.py")
rc |= run("python validations/su3_rest_abelianization.py")
sys.exit(rc)
