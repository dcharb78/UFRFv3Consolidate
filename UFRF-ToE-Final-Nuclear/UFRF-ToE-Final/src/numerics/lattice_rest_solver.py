
import numpy as np
def rest_penalty(E, B, mu=1.0):
    E = float(E); B = float(B)
    return mu*(E*E - B*B)**2
def find_rest_window(E_range=(-2,2), B_range=(-2,2), steps=401):
    Emin,Emax = E_range; Bmin,Bmax = B_range
    Es = np.linspace(Emin,Emax,steps); Bs=np.linspace(Bmin,Bmax,steps)
    grid = np.zeros((steps,steps))
    minval = 1e99; argmin=(0,0)
    for i,e in enumerate(Es):
        for j,b in enumerate(Bs):
            v = rest_penalty(e,b)
            grid[i,j]=v
            if v<minval:
                minval=v; argmin=(e,b)
    return {"min_E":float(argmin[0]), "min_B":float(argmin[1]), "min_penalty":float(minval)}
