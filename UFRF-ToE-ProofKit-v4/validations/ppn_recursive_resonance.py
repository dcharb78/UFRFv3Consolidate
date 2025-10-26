
import json, os
from src.dynamics.recursive_projection import simulate_ppn_dynamics

if __name__=='__main__':
    out = simulate_ppn_dynamics(steps=20000, dt=0.01, Phi0=1e-8, dp0=0.1, a=1e-9, b=1e-9,
                                k_phi=2e-3, k_dp=2e-3, noise=0.0, seed=42)
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/ppn_dynamics_summary.json","w") as f:
        json.dump(out, f, indent=2)
    print("PPN dynamics summary:")
    print(json.dumps(out["gamma"], indent=2))
    print(json.dumps(out["beta"], indent=2))
