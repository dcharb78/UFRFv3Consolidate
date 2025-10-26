
import numpy as np
from src.common.utils import finite_diff_scalar

def F_tensor(A_funcs, x, h=1e-6):
    F = np.zeros((4,4), dtype=float)
    for mu in range(4):
        for nu in range(mu+1,4):
            dmu_Anu = finite_diff_scalar(A_funcs[nu], x, mu, h)
            dnu_Amu = finite_diff_scalar(A_funcs[mu], x, nu, h)
            val = dmu_Anu - dnu_Amu
            F[mu,nu]=val; F[nu,mu]=-val
    return F

def lagrangian_density(F, eta=None):
    if eta is None: eta = np.diag([1,-1,-1,-1])
    Fup = eta @ F @ eta
    return -0.25 * np.sum(F * Fup)

def bianchi_residual(F_at, x, h=1e-6):
    def dF(lam, mu, nu):
        def comp(z): return F_at(z)[mu,nu]
        return finite_diff_scalar(comp, x, lam, h)
    res_sq=0.0; cnt=0
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                if lam<mu<nu:
                    cyc = dF(lam,mu,nu)+dF(mu,nu,lam)+dF(nu,lam,mu)
                    res_sq+=cyc*cyc; cnt+=1
    return (res_sq/max(cnt,1))**0.5
