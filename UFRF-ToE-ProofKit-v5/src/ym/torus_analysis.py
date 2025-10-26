
import numpy as np

def eigenphases(U):
    w,_ = np.linalg.eig(U); ang = np.angle(w); ang.sort(); return ang

def cartan_coords(ang):
    th1,th2,th3 = ang; return np.array([th1, -th3])

def chord_scores(phi):
    bins13 = (phi%(2*np.pi))/(2*np.pi/13.0)
    d = np.min([np.abs(bins13-np.round(bins13)), 13-np.abs(bins13-np.round(bins13))], axis=0).sum()
    return {"dist13": float(d)}
