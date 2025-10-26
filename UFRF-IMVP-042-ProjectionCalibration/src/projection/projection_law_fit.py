import numpy as np

def fit_projection(scales, observations, alphas, S_guess=-0.05):
    """Linearize ln O = ln O* + d_M * α * S + ε and solve least squares.
    scales: array of M_obs/M_tgt per datum (or M_obs, M_tgt pairs turned to ratio)
    observations: array of O (positive)
    alphas: array of technique α in [0,1]
    Returns dict with O_star, S, stderr
    """
    scales = np.asarray(scales, dtype=float)
    obs = np.asarray(observations, dtype=float)
    alphas = np.asarray(alphas, dtype=float)
    assert np.all(obs>0), "Observations must be positive for log."
    y = np.log(obs)
    X = np.column_stack([np.ones_like(scales), alphas*np.log(scales)])
    # Solve y = c0 + c1 * (α ln r)  ⇒ c0 = ln O*, c1 = S
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    lnOstar, S = coef
    residuals = y - X @ coef
    stderr = np.sqrt(np.mean(residuals**2))
    return {"O_star": float(np.exp(lnOstar)), "S": float(S), "stderr": float(stderr)}

def demo_synthetic(n=30, O_star=2.0, S=-0.06, rng=0):
    """Generate synthetic data at random scale ratios and techniques, then fit."""
    rs = np.exp(np.random.default_rng(rng).uniform(-5.0, 5.0, size=n))  # ratios spanning many decades
    al = np.random.default_rng(rng+1).uniform(0.1, 0.9, size=n)
    noise = np.random.default_rng(rng+2).normal(0, 0.02, size=n)
    lnO = np.log(O_star) + np.log(rs)*al*S + noise
    O = np.exp(lnO)
    fit = fit_projection(rs, O, al)
    fit["rs"] = rs.tolist(); fit["alphas"] = al.tolist(); fit["O"] = O.tolist()
    return fit
