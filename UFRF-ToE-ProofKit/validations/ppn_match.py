
from math import pi
from src.gravity.ufrf_metric import metric_from_invariants, ppn_from_metric, toy_I1_from_cycle
U = 1e-8; a=b=1e-9; dp=0.1
I1 = toy_I1_from_cycle(dp,1.0,2*pi/13)
g00,gij = metric_from_invariants(U,I1,a,b); gamma,beta = ppn_from_metric(U,I1,a,b,U)
print("PPN sample: gamma=", gamma," beta=", beta," g00=",g00," g_xx=",gij[0,0])
