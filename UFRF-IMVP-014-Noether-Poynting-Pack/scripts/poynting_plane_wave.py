
#!/usr/bin/env python3
import math

c = 299792458.0
mu0 = 4e-7*math.pi
eps0 = 1.0/(mu0*c*c)

E0 = 2.0
lam = 1.0
k  = 2.0*math.pi/lam
w  = c*k

def Ey(x,t): return E0*math.cos(k*x - w*t)
def Bz(x,t): return (E0/c)*math.cos(k*x - w*t)

def cycle_average(n=1000):
    # average over one period in time at fixed x=0
    T = 2.0*math.pi/w
    dt = T/n
    u_sum = 0.0
    S_sum = 0.0
    for i in range(n):
        t = i*dt
        E = Ey(0.0,t)
        B = Bz(0.0,t)
        u = 0.5*(eps0*E*E + (B*B)/mu0)
        S = (1.0/mu0)*E*B   # |S| since E ⟂ B and we pick components
        u_sum += u
        S_sum += S
    return u_sum/n, S_sum/n

if __name__ == "__main__":
    u,S = cycle_average()
    print(f"<u> ≈ {u:.6e} J/m^3")
    print(f"<|S|> ≈ {S:.6e} W/m^2")
    print(f"Check S ≈ u*c → {S:.6e} vs {u*c:.6e}")
