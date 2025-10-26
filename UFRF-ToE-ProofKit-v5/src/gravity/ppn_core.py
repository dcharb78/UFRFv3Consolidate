
import numpy as np
def ppn_from_metric(Phi, I1, a=0.0, b=0.0, U=None):
    if U is None: U=Phi
    gamma = 1.0 + 0.5*b*I1/U if U!=0 else 1.0
    beta  = 1.0 - 0.5*a*I1/U if U!=0 else 1.0
    return gamma, beta
def toy_I1_from_dp(dp, B0=1.0, K=2.0*np.pi/13.0):
    return -4.0*(B0**2)*(K**2)*(dp**2)
