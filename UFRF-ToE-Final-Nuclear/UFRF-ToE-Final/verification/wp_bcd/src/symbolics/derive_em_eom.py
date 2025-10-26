
import sympy as sp
from .field_core import coords, d, raise2, contract2, divergence2, hodge_dual

A = [sp.Function(f"A{mu}")(*coords) for mu in range(4)]
Phi = sp.Function("Phi")(*coords)

Z = sp.Function("Z")(Phi)
Theta = sp.Function("Theta")(Phi)

Fcov = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        Fcov[mu,nu] = d(mu, A[nu]) - d(nu, A[mu])

Fcon = raise2(Fcov)
Fdual = hodge_dual(Fcov)

I1 = contract2(Fcov, Fcon)
I2 = contract2(Fcov, Fdual)

L_em = -sp.Rational(1,4)*Z*I1 - sp.Rational(1,4)*Theta*I2

K = sp.MutableDenseNDimArray.zeros(4,4)
for mu in range(4):
    for nu in range(4):
        K[mu,nu] = sp.simplify(Z*Fcon[mu,nu] + Theta*Fdual[mu,nu])

EOM = divergence2(K)

subs_maxwell = {Z: 1, Theta: 0}
EOM_maxwell = [sp.simplify(e.subs(subs_maxwell)) for e in EOM]

divF = divergence2(Fcon)

def assert_maxwell_free_vacuum():
    diffs = [sp.simplify(EOM_maxwell[nu] - divF[nu]) for nu in range(4)]
    return all(sp.simplify(x)==0 for x in diffs)

divFdual = divergence2(hodge_dual(Fcov))

def assert_bianchi():
    return all(sp.simplify(expr)==0 for expr in divFdual)

if __name__ == "__main__":
    print("Maxwell:", assert_maxwell_free_vacuum())
    print("Bianchi:", assert_bianchi())
