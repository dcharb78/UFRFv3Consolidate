
import sympy as sp

t, x, y, z = sp.symbols('t x y z', real=True)
coords = (t, x, y, z)

A = [sp.Function('A0')(t,x,y,z),
     sp.Function('A1')(t,x,y,z),
     sp.Function('A2')(t,x,y,z),
     sp.Function('A3')(t,x,y,z)]

chi = sp.Function('chi')(t,x,y,z)

def d(mu, f): return sp.diff(f, coords[mu])

# F(A)
F = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        F[mu,nu] = d(mu, A[nu]) - d(nu, A[mu])

# A' = A + ∂χ
Aprime = [A[mu] + d(mu, chi) for mu in range(4)]

# F(A')
Fp = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        Fp[mu,nu] = d(mu, Aprime[nu]) - d(nu, Aprime[mu])

# Check invariance: Fp - F == 0
diff = [[sp.simplify(Fp[mu,nu] - F[mu,nu]) for nu in range(4)] for mu in range(4)]
print("F'(A+∂χ) - F(A) =", diff)
