
import sympy as sp
# Minimal symbolic sketch: Minkowski metric, treat Z,Theta as constants for variation
t,x,y,z = sp.symbols('t x y z')
coords = (t,x,y,z)
A0,A1,A2,A3 = sp.symbols('A0 A1 A2 A3', cls=sp.Function)
Phi = sp.Function('Phi')
Z, Theta = sp.symbols('Z Theta')
# Build fields (only t,z dependence for a plane-wave sketch)
At,Ax,Ay,Az = A0(t,z),A1(t,z),A2(t,z),A3(t,z)
Phi_f = Phi(t,z)
# Field strengths (sketchy subset)
Ftx = sp.diff(Ax,t) - sp.diff(At,x)  # = ∂t Ax as At independent of x in this sketch
Fzy = sp.diff(Ay,z) - sp.diff(Az,y)  # = ∂z Ay
# Scalars (reduced): E_x ~ Ftx; B_y ~ Fzy
E2 = Ftx**2
B2 = Fzy**2
I1 = 2*(B2 - E2)
L = -sp.Rational(1,4)*Z*(E2 - B2) + sp.Rational(1,2)*(sp.diff(Phi_f,t)**2 - sp.diff(Phi_f,z)**2)
# Euler-Lagrange for Ax and Phi (sketch; omit total derivatives)
Ax_var = sp.diff(sp.diff(L, sp.diff(A1(t,z),t)), t) + sp.diff(sp.diff(L, sp.diff(A1(t,z),z)), z) - sp.diff(L, A1(t,z))
Phi_var = sp.diff(sp.diff(L, sp.diff(Phi(t,z),t)), t) + sp.diff(sp.diff(L, sp.diff(Phi(t,z),z)), z) - sp.diff(L, Phi(t,z))
print(sp.simplify(Ax_var))
print(sp.simplify(Phi_var))
