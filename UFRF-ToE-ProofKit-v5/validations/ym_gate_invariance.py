
import numpy as np, math
from src.ym.yang_mills import su3_f, nonabelian_F, covariant_divergence
def A_mu(x,y,mu,eps=0.1,period=40.0):
    s=math.sin(2*math.pi*(x+y)/period); c=math.cos(2*math.pi*(x-y)/period)
    A=np.zeros(8); 
    if mu==0: A[2]=0.6*s; A[7]=0.5*c; A[0]=eps*0.1*math.sin(2*math.pi*x/period); A[1]=eps*0.1*math.cos(2*math.pi*x/period)
    else:     A[2]=0.6*c; A[7]=0.5*s; A[0]=eps*0.1*math.cos(2*math.pi*y/period); A[1]=eps*0.1*math.sin(2*math.pi*y/period)
    return A
def A_funcs(eps=0.05,period=40.0): return [lambda z,mu=mu: A_mu(z[1],z[2],mu,eps,period) for mu in range(4)]
f=su3_f(); x0=[0,20,20,0]; A=A_funcs()
F=lambda z: nonabelian_F(A,z,f,g=0.5,h=1e-2); D=covariant_divergence(F,A,x0,f,g=0.5,h=1e-2)
print("Yang–Mills ||D_mu F^{mu nu}||:", float(np.linalg.norm(D)))
