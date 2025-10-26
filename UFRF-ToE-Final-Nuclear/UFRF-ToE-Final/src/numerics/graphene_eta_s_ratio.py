
import math
def eta_over_s_base():
    return 1.0/(4.0*math.pi)
def golden_ratio():
    return (1.0+5.0**0.5)/2.0
def sqrt_phi():
    return golden_ratio()**0.5
def eta_over_s_enhanced():
    return eta_over_s_base()*sqrt_phi()
