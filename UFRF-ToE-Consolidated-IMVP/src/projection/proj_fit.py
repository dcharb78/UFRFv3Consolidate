
import numpy as np
def fit_projection(scales, observations, alphas):
    scales = np.asarray(scales, float); obs = np.asarray(observations, float); alphas = np.asarray(alphas, float)
    y = np.log(obs)
    X = np.column_stack([np.ones_like(scales), alphas*np.log(scales)])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    lnOstar, S = coef
    residuals = y - X@coef
    return np.exp(lnOstar), S, float(np.sqrt(np.mean(residuals**2)))
def demo(n=40, Ostar=1.37, S=-0.05, seed=0):
    rng = np.random.default_rng(seed)
    r = np.exp(rng.uniform(-3,3,size=n))
    a = rng.uniform(0.1,0.9,size=n)
    eps = rng.normal(0,0.01,size=n)
    lnO = np.log(Ostar) + a*np.log(r)*S + eps
    return fit_projection(r, np.exp(lnO), a)
