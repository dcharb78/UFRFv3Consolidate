
import numpy as np, math

def fit_S_difference(data, clusters, t1, t2, dM, a1, a2):
    # y = ΔlnM = dM * (a1 - a2) * S + ε  -> slope S via least squares on a constant regressor
    # Here X is constant c = dM*(a1-a2); y is observed differences across clusters
    y = []
    for cl in clusters:
        y.append(data[cl][t1] - data[cl][t2])
    y = np.array(y, dtype=float)
    c = dM*(a1 - a2)
    if abs(c) < 1e-12:
        return {"S": 0.0, "stderr": float(np.std(y))}
    S_hat = float(np.mean(y)/c)
    resid = y - c*S_hat
    return {"S": S_hat, "stderr": float(np.sqrt(np.mean(resid**2)))}

def predict_difference(dM, S, a1, a2):
    return dM*(a1 - a2)*S
