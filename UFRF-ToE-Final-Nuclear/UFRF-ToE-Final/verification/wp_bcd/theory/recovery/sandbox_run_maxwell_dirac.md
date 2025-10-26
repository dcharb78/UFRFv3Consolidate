# UFRF-ToE: Sandbox Maxwell & Dirac Recovery

SymPy available — performing symbolic EM derivation.

## Symbolic EM Results
Euler–Lagrange equations for each ν component (truncated view):
  ν=0: Add(Mul(Symbol('Z', positive=True, real=True), Add(Derivative(Function('A0')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x1', real=True), Integer(2)) ...
  ν=1: Add(Mul(Symbol('Z', positive=True, real=True), Add(Derivative(Function('A1')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x0', real=True), Integer(2)) ...
  ν=2: Add(Mul(Symbol('Z', positive=True, real=True), Add(Derivative(Function('A2')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x0', real=True), Integer(2)) ...
  ν=3: Add(Mul(Symbol('Z', positive=True, real=True), Add(Derivative(Function('A3')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x0', real=True), Integer(2)) ...

Bianchi identity (αβγ = 0,1,2) simplifies to:
  Integer(0)

Vacuum Maxwell check (ν=0) with Aμ=(φ,0,0,0), Z=1, J=0:
  eom_ν=0 → Add(Derivative(Function('phi')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x1', real=True), Integer(2))), Derivative(Function('phi')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x2', real=True), Integer(2))), Derivative(Function('phi')(Symbol('x0', real=True), Symbol('x1', real=True), Symbol('x2', real=True), Symbol('x3', real=True)), Tuple(Symbol('x3', real=True), Integer(2))))

## Dirac Dispersion Check
Chosen m=2.0, |p|^2=1.500000
E_on = sqrt(p^2 + m^2) = 2.345208
det(γ·p - m) on-shell   ≈ 7.396e-32+3.698e-32j
det(γ·p - m) off-shell  ≈ 2.241e+00-3.733e-16j
