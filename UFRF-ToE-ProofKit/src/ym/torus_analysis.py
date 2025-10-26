
import numpy as np

def eigenphases(U):
    # eigenphases of a unitary SU(3) matrix (sorted)
    w,_ = np.linalg.eig(U)
    ang = np.angle(w)
    ang.sort()
    return ang

def cartan_coords(ang):
    # map 3 phases (sum zero) to 2 independent torus coords
    th1,th2,th3 = ang
    return np.array([th1, -th3])

def chord_scores(phi):
    # simple 'chord' intervals: perfect 5th ~ 3/2 (mod 2π), perfect 4th ~ 4/3.
    # Here we just measure closeness to integer 13 bins too.
    bins13 = (phi%(2*np.pi))/(2*np.pi/13.0)
    dist13 = np.min([np.abs(bins13 - np.round(bins13)), 13 - np.abs(bins13 - np.round(bins13))], axis=0).sum()
    return {"dist13": float(dist13)}

def rayleigh_R(angles):
    z = np.exp(1j*angles)
    R = np.abs(np.mean(z))
    return float(R)
