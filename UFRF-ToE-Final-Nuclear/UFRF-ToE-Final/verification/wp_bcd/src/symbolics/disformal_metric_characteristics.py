
import sympy as sp
import random

def disformal_metric_matrix(a,b,c, E, B, dPhi):
    Ex,Ey,Ez = E
    Bx,By,Bz = B
    dt,d1,d2,d3 = dPhi
    eta = sp.diag(-1,1,1,1)
    F = sp.MutableDenseNDimArray.zeros(4,4)
    F[0,1],F[1,0] = Ex, -Ex
    F[0,2],F[2,0] = Ey, -Ey
    F[0,3],F[3,0] = Ez, -Ez
    F[1,2],F[2,1] = -Bz, Bz
    F[1,3],F[3,1] = By, -By
    F[2,3],F[3,2] = -Bx, Bx
    E2 = Ex**2+Ey**2+Ez**2
    B2 = Bx**2+By**2+Bz**2
    I1 = 2*(B2 - E2)
    F_up = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            F_up[mu,nu] = sum(eta[mu,b]*F[b,nu] for b in range(4))
    FF = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            FF[mu,nu] = sum(F_up[mu,a]*F[nu,a] for a in range(4))
    g = sp.MutableDenseNDimArray.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            g[mu,nu] = eta[mu,nu] + a*eta[mu,nu]*I1 + b*FF[mu,nu] + c*dPhi[mu]*dPhi[nu]
    return sp.Matrix(g)

def cone_speed_along_x(g):
    w = sp.symbols('w', real=True)
    ginv = g.inv()
    k = sp.Matrix([w, 1, 0, 0])  # kx = 1
    quad = sp.simplify((k.T*ginv*k)[0])
    sols = sp.solve(sp.Eq(quad, 0), w)
    vals = []
    for s in sols:
        v = sp.N(s)  # since kx=1, speed = w
        if abs(sp.im(v)) < 1e-9:
            vals.append(float(sp.re(v)))
    return sorted([abs(v) for v in vals])

def find_safe_bounds(num_trials=30):
    epsE = 0.2
    # Coeff bounds tuned for robust subluminality
    ea, eb, ec = 0.03, 0.005, 0.01   # |a|≤0.03, 0≤b≤0.005, 0≤c≤0.01
    for _ in range(num_trials):
        Ex = random.uniform(-epsE, epsE)
        Ey = random.uniform(-epsE, epsE)
        if Ex**2+Ey**2 < 1e-6:
            Ey = epsE
        # Perp B in xy-plane with |B|=|E|
        Bx, By = -Ey, Ex
        s = (Bx*Bx+By*By)**0.5
        scale = ((Ex**2+Ey**2)**0.5)/(s if s else 1.0)
        Bx,By,Bz = Bx*scale, By*scale, 0.0
        Ez = 0.0
        # Timelike ∂Φ: dt dominates spatial parts
        dt = random.uniform(0.05, 0.2)
        d1 = random.uniform(-0.05, 0.05)
        d2 = random.uniform(-0.05, 0.05)
        d3 = random.uniform(-0.05, 0.05)
        a = random.uniform(-ea, ea)
        b = random.uniform(0, eb)
        c = random.uniform(0, ec)
        g = disformal_metric_matrix(a,b,c,
                                    (Ex,Ey,Ez),
                                    (Bx,By,Bz),
                                    (dt,d1,d2,d3))
        # Signature: one negative, three positive
        evals = [complex(ev.evalf()) for ev in g.eigenvals().keys()]
        neg = sum(1 for ev in evals if ev.real < -1e-8)
        pos = sum(1 for ev in evals if ev.real >  1e-8)
        if not (neg==1 and pos==3):
            return False, {"a":a,"b":b,"c":c,"evals":[str(e) for e in evals]}
        # Cone along x
        speeds = cone_speed_along_x(g)
        if len(speeds)<2 or speeds[-1] > 1.0 + 1e-7:
            return False, {"a":a,"b":b,"c":c,"speeds":speeds}
    return True, {"bounds":{"E_B_bound":0.2,"grad_phi_timelike":"dt in [0.05,0.2], |spatial|<=0.05",
                            "|a|≤":0.03,"0≤b≤":0.005,"0≤c≤":0.01}}
