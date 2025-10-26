
import json, math, random
import numpy as np

def ppn_from_params(a,b,c,background_scale=1e-2):
    """
    Very first-order ansatz near REST:
      δg_00 = +2 U (1 + ε1),   δg_ij = +2 U (1 + ε2) δ_ij
    with ε1 ~ κ1 (a I1 + c |∂Φ|^2), ε2 ~ κ2 (a I1) + κ3 b Q
    Here, approximate I1 ~ O(background_scale^2), |∂Φ|^2 ~ O(background_scale^2), Q ~ O(background_scale^2).
    Set κi = O(1). Then:
      γ = (1+ε2)/(1+ε1),   β ≈ 1 + O(ε1)  (toy mapping to second order omitted)
    We report |γ-1| and |β-1| with κi=1 and characteristic background.
    """
    I1 = background_scale**2
    grad2 = background_scale**2
    Q = background_scale**2
    eps1 = a*I1 + c*grad2
    eps2 = a*I1 + b*Q
    gamma = (1.0 + eps2) / (1.0 + eps1)
    # crude β proxy from second-order correction of g00 ~ -1 + 2U - 2β U^2 ; take β-1 ~ 0.5*(eps1)
    beta = 1.0 + 0.5*eps1
    return gamma, beta

def sweep(bounds, N=2000, background_scale=5e-3):
    amax,bmax,cmax = bounds
    max_dev_gamma = 0.0
    max_dev_beta = 0.0
    samples = []
    for _ in range(N):
        a = random.uniform(-amax,amax)
        b = random.uniform(-bmax,bmax)
        c = random.uniform(0.0,cmax)
        gamma, beta = ppn_from_params(a,b,c,background_scale=background_scale)
        max_dev_gamma = max(max_dev_gamma, abs(gamma-1.0))
        max_dev_beta  = max(max_dev_beta,  abs(beta -1.0))
        samples.append((a,b,c,gamma,beta))
    return {
        "bounds": {"a":amax,"b":bmax,"c":cmax},
        "background_scale": background_scale,
        "max_abs_gamma_minus_1": max_dev_gamma,
        "max_abs_beta_minus_1": max_dev_beta,
        "example": {"a":samples[-1][0],"b":samples[-1][1],"c":samples[-1][2],"gamma":samples[-1][3],"beta":samples[-1][4]}
    }

if __name__ == "__main__":
    # Tight bounds show γ,β≈1 within 1e-6–1e-5 range
    tight = sweep((5e-3,5e-3,5e-3), N=2000, background_scale=5e-3)
    # Moderate bounds
    moderate = sweep((1e-2,1e-2,1e-2), N=2000, background_scale=1e-2)
    out = {"tight": tight, "moderate": moderate}
    with open("artifacts/ppn_report.json","w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
