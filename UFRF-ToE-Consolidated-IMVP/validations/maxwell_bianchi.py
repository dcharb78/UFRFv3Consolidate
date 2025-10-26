
from src.gauge.ufrf_maxwell import F_tensor, bianchi_residual
B0=0.5
A0=lambda x: 0.0
A1=lambda x: -0.5*B0*x[2]
A2=lambda x:  0.5*B0*x[1]
A3=lambda x: 0.0
F = lambda z: F_tensor([A0,A1,A2,A3], z)
print("Maxwell Bianchi residual:", bianchi_residual(F))
