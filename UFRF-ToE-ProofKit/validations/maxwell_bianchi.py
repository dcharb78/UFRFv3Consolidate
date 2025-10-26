
from src.field.maxwell import F_tensor, bianchi_residual, lagrangian_density
B0=0.5
A0=lambda x: 0.0
A1=lambda x: -0.5*B0*x[2]
A2=lambda x:  0.5*B0*x[1]
A3=lambda x: 0.0
F = lambda z: F_tensor([A0,A1,A2,A3], z)
x0=[0.0,0.1,0.2,0.3]
res = bianchi_residual(F, x0)
L = lagrangian_density(F(x0))
print("Maxwell Bianchi residual:", res, "  L:", L)
