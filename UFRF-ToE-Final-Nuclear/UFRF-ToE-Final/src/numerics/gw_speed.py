import numpy as np
def gw_speed_near_rest(a=1e-3, b=5e-4, c=0.0, E=(0.0,0.0,0.0), B=(0.0,0.0,0.0), dPhi=(0,0,0,0)):
    E = np.asarray(E,float); B = np.asarray(B,float)
    E2 = float(E@E); B2 = float(B@B)
    I1 = 2*(B2 - E2)
    gtt = -1.0 + a*I1
    gss = 1.0 + a*I1 + b*(E2 + B2)
    v2 = (-gtt)/gss
    return float(np.sqrt(max(v2, 0.0)))
