
import numpy as np
from math import sin, pi
from src.gravity.ppn_core import ppn_from_metric, toy_I1_from_dp

def beats(t, freqs):
    # Simple sum of sines to simulate concurrent cycles
    return sum(sin(2*pi*f*t) for f in freqs)

def simulate_ppn_dynamics(
    steps=20000,
    dt=0.01,
    Phi0=1e-8,
    dp0=0.1,
    a=1e-9,
    b=1e-9,
    dM=np.log(144000/144),
    alpha=0.9,
    B0=1.0,
    freqs=(1/365.25, 1/4332.59, 1/10759.0),
    k_phi=1e-3,
    k_dp=1e-3,
    noise=0.0,
    seed=0
):
    rng = np.random.default_rng(seed)
    Phi = Phi0
    dp  = dp0
    gamma_series = np.zeros(steps)
    beta_series  = np.zeros(steps)
    for n in range(steps):
        t = n*dt
        # Beat-driven phase perturbation
        beat = beats(t, freqs)
        # Projection feedback (log-space)
        proj = dM * alpha * 1e-6  # tiny effective projection each step
        # Evolve state
        dp += k_dp*(beat) * dt + noise*rng.normal(0,1e-4)
        I1 = toy_I1_from_dp(dp, B0=B0)
        Phi *= (1 + k_phi*(sin(beat)+proj))  # mild multiplicative feedback
        # Extract PPN per step
        g,b = ppn_from_metric(Phi, I1, a=a, b=b, U=Phi)
        gamma_series[n] = g
        beta_series[n]  = b
    # Summary
    def stats(x):
        return {
            "mean": float(np.mean(x)),
            "std":  float(np.std(x)),
            "min":  float(np.min(x)),
            "max":  float(np.max(x))
        }
    return {
        "params": {"steps":steps,"dt":dt,"Phi0":Phi0,"dp0":dp0,"a":a,"b":b,"dM":dM,"alpha":alpha,"B0":B0,
                   "freqs":freqs,"k_phi":k_phi,"k_dp":k_dp,"noise":noise,"seed":seed},
        "gamma": stats(gamma_series),
        "beta":  stats(beta_series),
        "gamma_last10": stats(gamma_series[-10:]),
        "beta_last10":  stats(beta_series[-10:]),
        "series_tail": {
            "gamma": [float(v) for v in gamma_series[-100:].tolist()],
            "beta":  [float(v) for v in beta_series[-100:].tolist()]
        }
    }
