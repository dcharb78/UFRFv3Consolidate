
import numpy as np
from src.spinor.dirac import plane_wave_spinor, current_density, minimal_coupling_shift
u,E = plane_wave_spinor([0,0,0.6], m=1.0)
j0,j = current_density(u)
Eshift, pshift = minimal_coupling_shift(np.array([0,0,0.6]), A_mu=[0.2,0.1,0,0], e=1.0)
print("Dirac: E=",E," j0=",j0," j=", j.tolist())
print("Minimal coupling: E'=",Eshift," p'=", pshift.tolist())
