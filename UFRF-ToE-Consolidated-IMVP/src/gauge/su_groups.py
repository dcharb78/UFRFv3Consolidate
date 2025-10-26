
import numpy as np, math

def su2_f():
    f = np.zeros((3,3,3), dtype=float)
    f[0,1,2]=1; f[1,2,0]=1; f[2,0,1]=1
    f[0,2,1]=-1; f[1,0,2]=-1; f[2,1,0]=-1
    return f

def su3_f():
    f = np.zeros((8,8,8), dtype=float)
    def set_f(a,b,c,val):
        f[a,b,c]=val; f[b,c,a]=val; f[c,a,b]=val
        f[b,a,c]=-val; f[c,b,a]=-val; f[a,c,b]=-val
    set_f(0,1,2,1.0)
    set_f(0,3,6,0.5); set_f(1,4,6,0.5); set_f(2,3,4,0.5); set_f(2,5,6,0.5)
    return f

def nonabelian_F(A_funcs, x, f_const, g=1.0, h=1e-6):
    n = f_const.shape[0]
    F = np.zeros((n,4,4))
    def dmu_Anu_comp(a, mu, nu):
        def comp(z): return A_funcs[nu](z)[a]
        xp = np.array(x, dtype=float); xm = np.array(x, dtype=float)
        xp[mu]+=h; xm[mu]-=h
        return (comp(xp)-comp(xm))/(2*h)
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

def gell_mann():
    Z = np.zeros((3,3), dtype=complex)
    l1 = Z.copy(); l1[0,1]=l1[1,0]=1
    l2 = Z.copy(); l2[0,1]=-1j; l2[1,0]=1j
    l3 = Z.copy(); l3[0,0]=1; l3[1,1]=-1
    l4 = Z.copy(); l4[0,2]=l4[2,0]=1
    l5 = Z.copy(); l5[0,2]=-1j; l5[2,0]=1j
    l6 = Z.copy(); l6[1,2]=l6[2,1]=1
    l7 = Z.copy(); l7[1,2]=-1j; l7[2,1]=1j
    l8 = (1/np.sqrt(3))*np.diag([1,1,-2]).astype(complex)
    return [l1,l2,l3,l4,l5,l6,l7,l8]

def su3_exp_from_theta(theta):
    LAM = gell_mann()
    G = sum(theta[a]*LAM[a] for a in range(8))/2.0
    iG = 1j*G
    I = np.eye(3, dtype=complex)
    X = I + iG + 0.5*(iG@iG) + (1/6.0)*(iG@iG@iG) + (1/24.0)*(iG@iG@iG@iG)
    U,S,Vh = np.linalg.svd(X)
    Q = U @ Vh
    det = np.linalg.det(Q)
    Q /= det**(1/3)
    return Q
