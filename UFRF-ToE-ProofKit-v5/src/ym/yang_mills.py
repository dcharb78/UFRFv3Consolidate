
import numpy as np
from src.common.utils import finite_diff_scalar

def su3_f():
    f = np.zeros((8,8,8), dtype=float)
    def set_f(a,b,c,val):
        f[a,b,c]=val; f[b,c,a]=val; f[c,a,b]=val
        f[b,a,c]=-val; f[c,b,a]=-val; f[a,c,b]=-val
    set_f(0,1,2,1.0)
    set_f(0,3,6,0.5); set_f(1,4,6,0.5); set_f(2,3,4,0.5); set_f(2,5,6,0.5)
    return f

def nonabelian_F(A_funcs, x, f_const, g=1.0, h=1e-3):
    n = f_const.shape[0]; F = np.zeros((n,4,4))
    def dmu_Anu_comp(a, mu, nu):
        def comp(z): return A_funcs[nu](z)[a]
        return finite_diff_scalar(comp, x, mu, h)
    for a in range(n):
        for mu in range(4):
            for nu in range(mu+1,4):
                term = dmu_Anu_comp(a,mu,nu) - dmu_Anu_comp(a,nu,mu)
                nl=0.0
                for b in range(n):
                    for c in range(n):
                        nl += f_const[a,b,c]*A_funcs[mu](x)[b]*A_funcs[nu](x)[c]
                val = term + g*nl
                F[a,mu,nu]=val; F[a,nu,mu]=-val
    return F

def covariant_divergence(F_at, A_funcs, x, f_const, g=1.0, h=1e-3):
    n = f_const.shape[0]; eta = np.diag([1,-1,-1,-1])
    def F_up(z):
        F = F_at(z); Fup = np.zeros_like(F)
        for a in range(n): Fup[a] = eta @ F[a] @ eta
        return Fup
    def d_mu_F(a, mu, nu):
        def comp(z): return F_up(z)[a,mu,nu]
        return finite_diff_scalar(comp, x, mu, h)
    D = np.zeros((n,4))
    for nu in range(4):
        for a in range(n):
            s = 0.0
            for mu in range(4): s += d_mu_F(a,mu,nu)
            for b in range(n):
                for c in range(n):
                    for mu in range(4):
                        s += g*f_const[a,b,c]*A_funcs[mu](x)[b]*F_up(x)[c,mu,nu]
            D[a,nu] = s
    return D
