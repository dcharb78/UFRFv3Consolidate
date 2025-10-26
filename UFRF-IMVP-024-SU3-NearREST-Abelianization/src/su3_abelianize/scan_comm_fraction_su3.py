#!/usr/bin/env python3
import numpy as np, math

_f = {}
def _set(a,b,c,val):
    _f[(a,b,c)] = val
    _f[(b,a,c)] = -val

_set(1,2,3,1.0)
for triple in [(1,4,7),(1,6,5),(2,4,6),(2,5,7),(3,4,5),(3,6,7)]:
    _set(*triple, 0.5)
for triple in [(4,5,8),(6,7,8)]:
    _set(*triple, math.sqrt(3)/2.0)

def f(a,b,c):
    if a==b or b==c or a==c: return 0.0
    return _f.get((a,b,c), 0.0)

def A_mu_a(x,y,mu,a,eps_amp,period=32.0):
    s = math.sin(2.0*math.pi*(x+y)/period)
    c = math.cos(2.0*math.pi*(x-y)/period)
    if mu==0:
        if a==3: return 0.6*s
        if a==8: return 0.5*c
        return eps_amp*0.1*math.sin(2.0*math.pi*x/period)
    else:
        if a==3: return 0.6*c
        if a==8: return 0.5*s
        return eps_amp*0.1*math.cos(2.0*math.pi*y/period)

def d_mu(fun, x, y, mu, h=1e-3):
    if mu==0: return (fun(x+h,y)-fun(x-h,y))/(2*h)
    else:     return (fun(x,y+h)-fun(x,y-h))/(2*h)

def F_comm_sq(x,y,eps_amp,g=0.5):
    s2 = 0.0
    for a in range(1,9):
        comm = 0.0
        for b in range(1,9):
            for c in range(1,9):
                if b==c: continue
                comm += f(a,b,c) * A_mu_a(x,y,0,b,eps_amp) * A_mu_a(x,y,1,c,eps_amp)
        s2 += (g*comm)**2
    return s2

def F_deriv_sq(x,y,eps_amp):
    s2 = 0.0
    for a in range(1,9):
        Ay = lambda xx,yy: A_mu_a(xx,yy,1,a,eps_amp)
        Ax = lambda xx,yy: A_mu_a(xx,yy,0,a,eps_amp)
        fxy = d_mu(Ay, x,y,0) - d_mu(Ax, x,y,1)
        s2 += fxy*fxy
    return s2

def scan():
    Nx = 64
    xs = [i for i in range(8, Nx-8, 4)]
    ys = [i for i in range(8, Nx-8, 4)]
    for eps_amp in [1.0, 0.5, 0.2, 0.1, 0.05]:
        num=0.0; den=0.0; cnt=0
        for x in xs:
            for y in ys:
                num += math.sqrt(F_comm_sq(x,y,eps_amp))
                den += math.sqrt(F_deriv_sq(x,y,eps_amp) + 1e-18)
                cnt += 1
        R = (num/cnt)/(den/cnt)
        print(f"ε={eps_amp:4.2f}  <|g[A,A]|>/<|∂A|> ≈ {R:.3e}")

if __name__ == "__main__":
    scan()
