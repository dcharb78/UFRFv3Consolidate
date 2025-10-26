
#!/usr/bin/env python3
import math

def eps(a,b,c):
    perm = (a,b,c)
    if len(set(perm))<3: return 0.0
    if perm in [(0,1,2),(1,2,0),(2,0,1)]: return 1.0
    return -1.0

def A_mu_a(x,y,mu,a,eps_amp,period=32.0):
    # near-abelian configuration: dominant a=2 component plus small transverse components ~ eps_amp
    base = math.sin(2.0*math.pi*(x+y)/period)
    if mu==0:  # x
        if a==2: return 0.6*base
        if a in (0,1): return eps_amp*0.1*math.cos(2.0*math.pi*x/period)
    if mu==1:  # y
        if a==2: return 0.6*base
        if a in (0,1): return eps_amp*0.1*math.sin(2.0*math.pi*y/period)
    return 0.0

def d_mu(f, x, y, mu, dx=1.0):
    if mu==0:
        return (f(x+dx,y)-f(x-dx,y))/(2*dx)
    else:
        return (f(x,y+dx)-f(x,y-dx))/(2*dx)

def F_comm_sq(x,y,eps_amp,g=0.5):
    # |g [A,A]|_xy^2 sum over a
    s2 = 0.0
    for a in range(3):
        comm = 0.0
        for b in range(3):
            for c in range(3):
                comm += eps(a,b,c)*A_mu_a(x,y,0,b,eps_amp)*A_mu_a(x,y,1,c,eps_amp)
        s2 += (g*comm)**2
    return s2

def F_deriv_sq(x,y,eps_amp):
    # |∂_x A_y - ∂_y A_x|^2 sum over a
    s2 = 0.0
    for a in range(3):
        fxy = d_mu(lambda xx,yy: A_mu_a(xx,yy,1,a,eps_amp),x,y,0) - d_mu(lambda xx,yy: A_mu_a(xx,yy,0,a,eps_amp),x,y,1)
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
        print(f"ε={eps_amp:4.2f}  ⟨|g[A,A]|⟩/⟨|∂A|⟩ ≈ {R:.3e}")

if __name__ == "__main__":
    scan()
