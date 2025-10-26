
import sympy as sp

def hamiltonian_density_temporal_gauge():
    # Fields A_i(x,t) with A_0 = 0 (temporal gauge)
    t, x, y, z = sp.symbols('t x y z', real=True)
    A1 = sp.Function('A1')(t,x,y,z)
    A2 = sp.Function('A2')(t,x,y,z)
    A3 = sp.Function('A3')(t,x,y,z)
    Adot = [sp.diff(A1,t), sp.diff(A2,t), sp.diff(A3,t)]
    # Curl B = ∇×A
    dAx = [sp.diff(A1,x), sp.diff(A1,y), sp.diff(A1,z)]
    dAy = [sp.diff(A2,x), sp.diff(A2,y), sp.diff(A2,z)]
    dAz = [sp.diff(A3,x), sp.diff(A3,y), sp.diff(A3,z)]
    B1 = dAz[1] - dAy[2]
    B2 = dAx[2] - dAz[0]
    B3 = dAy[0] - dAx[1]
    B = [B1,B2,B3]
    # E = -Ȧ
    E = [-Ad for Ad in Adot]
    Z, Theta = sp.symbols('Z Theta', positive=True, real=True)
    E2 = sum(e*e for e in E)
    B2 = sum(b*b for b in B)
    EdotB = sum(E[i]*B[i] for i in range(3))
    L = sp.simplify( Z*sp.Rational(1,2)*(E2 - B2) + Theta*EdotB )
    # Legendre transform
    a1,a2,a3 = sp.symbols('a1 a2 a3')
    Ltmp = L.subs({Adot[0]:a1, Adot[1]:a2, Adot[2]:a3})
    pi1 = sp.diff(Ltmp, a1).subs({a1:Adot[0], a2:Adot[1], a3:Adot[2]})
    pi2 = sp.diff(Ltmp, a2).subs({a1:Adot[0], a2:Adot[1], a3:Adot[2]})
    pi3 = sp.diff(Ltmp, a3).subs({a1:Adot[0], a2:Adot[1], a3:Adot[2]})
    Pi = [pi1,pi2,pi3]
    H = sp.simplify(sum(Pi[i]*Adot[i] for i in range(3)) - L)
    Htarget = sp.simplify( Z*sp.Rational(1,2)*(E2 + B2) )
    return sp.simplify(H), Htarget, sp.simplify(H - Htarget)

def run():
    H, Htarget, residual = hamiltonian_density_temporal_gauge()
    print({"residual_H_minus_target": str(residual)})

if __name__ == "__main__":
    run()
