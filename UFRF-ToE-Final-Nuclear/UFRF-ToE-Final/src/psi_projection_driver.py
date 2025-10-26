
import json, numpy as np
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src.symbolics.psi_projection_operators import projection_kernel_1d, psi_from_EB_1d, phase_to_cycle

N, L, sigma = 2048, 100.0, 2.5
x = np.linspace(0, L, N, endpoint=False)
E = np.sin(2*np.pi*x/L*7)
B = np.cos(2*np.pi*x/L*7)
K = projection_kernel_1d(N,L,sigma)
psi = psi_from_EB_1d(E,B,K)
u = 0.5*(E**2+B**2)
ratio = (np.abs(psi)**2).sum()/(u.sum()+1e-16)
theta = np.angle(B + 1j*E)
phi13 = phase_to_cycle(theta).mean()

report = {
  "norm_ratio_sum_psi2_to_energy": float(ratio),
  "mean_cycle_index_phi13": float(phi13),
  "N": N, "L": L, "sigma": sigma
}
import pathlib, json
pathlib.Path("artifacts/psi_projection_report.json").write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
