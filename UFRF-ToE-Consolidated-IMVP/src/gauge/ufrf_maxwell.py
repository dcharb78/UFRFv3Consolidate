
import numpy as np
def finite_diff(f, x, axis, h=1e-6):
    xp = np.array(x, dtype=float); xm = np.array(x, dtype=float)
    xp[axis]+=h; xm[axis]-=h
    return (f(xp)-f(xm))/(2*h)

def F_tensor(A_funcs, x, h=1e-6):
    F = np.zeros((4,4), dtype=float)
    for mu in range(4):
        for nu in range(mu+1,4):
            dmu_Anu = finite_diff(A_funcs[nu], x, mu, h)
            dnu_Amu = finite_diff(A_funcs[mu], x, nu, h)
            val = dmu_Anu - dnu_Amu
            F[mu,nu]=val; F[nu,mu]=-val
    return F

def bianchi_residual(F_at):
    def dF(x, lam, mu, nu, h=1e-6):
        def comp(z): return F_at(z)[mu,nu]
        xp = np.array(x, dtype=float); xm = np.array(x, dtype=float)
        xp[lam]+=h; xm[lam]-=h
        return (comp(xp)-comp(xm))/(2*h)
    x0 = np.array([0.0,0.1,0.2,0.3])
    res_sq=0.0; cnt=0
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                if lam<mu<nu:
                    cyc = dF(x0,lam,mu,nu)+dF(x0,mu,nu,lam)+dF(x0,nu,lam,mu)
                    res_sq+=cyc*cyc; cnt+=1
    return (res_sq/max(cnt,1))**0.5
