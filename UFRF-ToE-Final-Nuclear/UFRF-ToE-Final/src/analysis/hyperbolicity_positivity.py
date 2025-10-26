
import json, math, random
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])

def F_from_EB(E, B):
    F = np.zeros((4,4), dtype=float)
    for i in range(3):
        F[0, i+1] =  E[i]
        F[i+1, 0] = -E[i]
    eps = np.zeros((3,3,3))
    eps[0,1,2] = eps[1,2,0] = eps[2,0,1] = 1.0
    eps[0,2,1] = eps[1,0,2] = eps[2,1,0] = -1.0
    for i in range(3):
        for j in range(3):
            s = 0.0
            for k in range(3):
                s += -eps[i,j,k] * B[k]
            F[i+1, j+1] = s
    return F

def raise_index(F):
    return ETA @ F

def invariants(F):
    ETAup = ETA
    Fup = ETAup @ F @ ETAup
    I1 = float(np.sum(F*Fup))
    E = np.array([F[0,1], F[0,2], F[0,3]])
    B = np.array([F[2,3], F[3,1], F[1,2]])
    I2 = -4.0 * float(E @ B)
    return I1, I2

def disformal_metric(E, B, a, b, c, dphi=None):
    F = F_from_EB(E,B)
    I1,_ = invariants(F)
    Fmu_a = raise_index(F)
    T = Fmu_a @ F.T  # T_{μν} = F_{μ}{}^{α} F_{να}
    grad = np.zeros((4,1))
    if dphi is not None:
        grad[:,0] = dphi
    g = ETA + a*I1*ETA + b*T + c*(grad @ grad.T)
    return g

def lorentzian(g):
    w = np.linalg.eigvalsh(g)
    w.sort()
    neg = np.sum(w < -1e-10)
    pos = np.sum(w >  1e-10)
    return (neg==1) and (pos>=3-(4-(neg+pos)))

def char_speeds(g):
    g_up = np.linalg.inv(g)
    speeds = []
    for _ in range(16):
        k = np.random.normal(size=3)
        nrm = np.linalg.norm(k)
        if nrm == 0: 
            continue
        k /= nrm
        gtt = g_up[0,0]
        gti = g_up[0,1:4]
        gij = g_up[1:4,1:4]
        A = gtt
        B = 2.0*float(gti @ k)
        C = float(k @ (gij @ k))
        disc = B*B - 4*A*C
        if disc < 0:
            return None, None
        sqrt_disc = math.sqrt(max(disc,0.0))
        if abs(A) < 1e-12:
            if abs(B) < 1e-12: 
                continue
            omega = -C/B
        else:
            omega1 = (-B + sqrt_disc)/(2*A)
            omega2 = (-B - sqrt_disc)/(2*A)
            omega = max(abs(omega1), abs(omega2))
        speeds.append(abs(omega))
    if not speeds:
        return None, None
    return max(speeds), min(speeds)

def scan(amax,bmax,cmax,emax,trials=300,tol=1e-6):
    passes = 0
    for _ in range(trials):
        a = np.random.uniform(-amax,amax)
        b = np.random.uniform(-bmax,bmax)
        c = np.random.uniform(0,cmax)
        E = np.random.uniform(-emax, emax, size=3)
        B = np.random.uniform(-emax, emax, size=3)
        g = disformal_metric(E,B,a,b,c)
        if not lorentzian(g): 
            continue
        vmax, vmin = char_speeds(g)
        if vmax is None: 
            continue
        if vmax <= 1.0 + tol and vmin >= 0.0 - tol:
            passes += 1
    return passes/trials

def find_safe_region():
    # coarse grid search to achieve ≥99% pass
    # shrink coefficients and fields together until criterion met
    for scale in [0.02, 0.015, 0.01, 0.0075, 0.005]:
        amax = bmax = cmax = scale
        emax = scale
        frac = scan(amax,bmax,cmax,emax,trials=600,tol=1e-6)
        if frac >= 0.99:
            return {"amax":amax,"bmax":bmax,"cmax":cmax,"emax":emax,"pass_fraction":frac}
    # if not found, report best
    best = {"pass_fraction":0.0}
    for scale in [0.02,0.015,0.01,0.0075,0.005]:
        frac = scan(scale,scale,scale,scale,trials=600,tol=1e-6)
        if frac > best.get("pass_fraction",0.0):
            best = {"amax":scale,"bmax":scale,"cmax":scale,"emax":scale,"pass_fraction":frac}
    return best

if __name__ == "__main__":
    # Report two regimes and the discovered safe region (≥99% pass if found)
    regimes = {
        "coarse_0p02": scan(0.02,0.02,0.02,0.02,trials=600),
        "coarse_0p01": scan(0.01,0.01,0.01,0.01,trials=600)
    }
    safe = find_safe_region()
    out = {"regimes": regimes, "safe_region": safe}
    with open("artifacts/hyperbolicity_report.json","w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
