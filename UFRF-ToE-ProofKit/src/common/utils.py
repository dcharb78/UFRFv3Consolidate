
import numpy as np

def finite_diff_scalar(f, x, axis, h=1e-6):
    xp = np.array(x, dtype=float); xm = np.array(x, dtype=float)
    xp[axis]+=h; xm[axis]-=h
    return (f(xp)-f(xm))/(2*h)
