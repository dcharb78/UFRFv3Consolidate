
import sympy as sp

I = sp.I

# Pauli matrices
sx = sp.Matrix([[0,1],[1,0]])
sy = sp.Matrix([[0,-I],[I,0]])
sz = sp.Matrix([[1,0],[0,-1]])

# Gamma matrices (Dirac representation)
g0 = sp.diag(1,1,-1,-1)
g1 = sp.Matrix(sp.BlockMatrix([[sp.zeros(2),  sx],[-sx, sp.zeros(2)]]))
g2 = sp.Matrix(sp.BlockMatrix([[sp.zeros(2),  sy],[-sy, sp.zeros(2)]]))
g3 = sp.Matrix(sp.BlockMatrix([[sp.zeros(2),  sz],[-sz, sp.zeros(2)]]))

E, pz, m = sp.symbols('E pz m', real=True)

slash = g0*E - g3*pz
M = slash - m*sp.eye(4)
detM = sp.simplify(M.det())  # Expect (E**2 - pz**2 - m**2)**2

# Positive-energy spinor (motion along z): u = [sqrt(E+m) χ, (pz/sqrt(E+m)) χ]^T with χ=[1,0]
sqrt = sp.sqrt
chi_up = sp.Matrix([1,0])
u_up = sp.Matrix.vstack(sqrt(E+m)*chi_up, (pz/sqrt(E+m))*chi_up)

res = sp.simplify((M*u_up).subs(E**2, pz**2 + m**2))

print("det(γ·p - m) =", sp.factor(detM))
print("(γ·p - m) u_up =", res)
num0 = sp.simplify(sp.together(res[0])*sp.sqrt(E+m))
print("First component numerator (pre-dispersion):", sp.simplify(num0))
num0_disp = sp.simplify(sp.expand(num0).subs(E**2, pz**2 + m**2))
print("First component numerator under E^2 = pz^2 + m^2:", num0_disp)
