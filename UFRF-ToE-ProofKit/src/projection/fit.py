
import numpy as np

def fit_projection(scales, observations, alphas):
    scales = np.asarray(scales, float); obs = np.asarray(observations, float); alphas=np.asarray(alphas,float)
    y = np.log(obs)
    X = np.column_stack([np.ones_like(scales), alphas*np.log(scales)])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    lnOstar, S = coef
    resid = y - X@coef
    return {"O_star": float(np.exp(lnOstar)), "S": float(S), "stderr": float(np.sqrt(np.mean(resid**2)))}
