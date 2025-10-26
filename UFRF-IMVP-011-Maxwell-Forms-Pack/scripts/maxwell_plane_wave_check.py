
#!/usr/bin/env python3
# Discrete check of Maxwell's equations for a 1D transverse plane wave in vacuum.
import math

c = 299792458.0
mu0 = 4e-7*math.pi
eps0 = 1.0/(mu0*c*c)

E0 = 1.0
lam = 1.0
k  = 2.0*math.pi/lam
w  = c*k

nx = 400
Lx = 2.0
dx = Lx/nx
dt = (dx/c)*0.2

def Ex(x,t): return 0.0
def Ey(x,t): return E0*math.cos(k*x - w*t)
def Ez(x,t): return 0.0

def Bx(x,t): return 0.0
def By(x,t): return 0.0
def Bz(x,t): return (E0/c)*math.cos(k*x - w*t)

def ddt(f, x, t, h=1e-9):
    return (f(x,t+h)-f(x,t-h))/(2*h)

def ddx(f, x, t, h=None):
    # central difference with grid spacing dx if h None
    if h is None: h = dx
    return (f(x+h,t)-f(x-h,t))/(2*h)

def residuals(x, t):
    # Maxwell in vacuum:
    # 1) ∇·B = 0
    divB = ddx(Bx,x,t)+0.0+0.0

    # 2) ∇×E + ∂B/∂t = 0  (only z-component matters)
    curlE_z = ddx(Ey,x,t)  # dEy/dx
    dBz_dt  = ddt(Bz,x,t)
    faraday = curlE_z + dBz_dt

    # 3) ∇·E = 0 (no charges)
    divE = ddx(Ex,x,t)+0.0+0.0

    # 4) ∇×B - μ0ε0 ∂E/∂t = 0 (only y,z components contribute)
    curlB_y = 0.0  # varies only in x, B has only z component => curlB_y = 0
    curlB_z = 0.0  # varies only in x, B has only z component => curlB_z = 0
    # But standard identity: curl B has an x-derivative of Bz in y-component: (∇×B)_y = ∂Bx/∂z - ∂Bz/∂x = -∂Bz/∂x
    curlB_y = -ddx(Bz,x,t)
    dE_dt_y = ddt(Ey,x,t)
    ampere  = curlB_y - mu0*eps0*dE_dt_y

    return divB, faraday, divE, ampere

def run():
    xs = [i*dx for i in range(1,nx-1, nx//10)]
    t  = 0.123456789
    totals = [0.0,0.0,0.0,0.0]
    for x in xs:
        r = residuals(x,t)
        for i in range(4):
            totals[i] += abs(r[i])
    avgs = [v/len(xs) for v in totals]
    labels = ["divB","Faraday","divE","Ampere"]
    for L,v in zip(labels,avgs):
        print(f"{L} avg residual ~ {v:.3e}")
    print("Expected: all near machine/FD error.")

if __name__ == "__main__":
    run()
