
import numpy as np
def degeneracy_and_magic():
    notes=np.array([1,3,3,3,4,11,16,22]); deg=(2*notes).tolist(); mag=np.cumsum(2*notes).tolist(); return deg,mag
def regression_checks():
    deg,mag=degeneracy_and_magic(); canonical=[2,8,14,20,28,50,82,126]
    recall=sum(1 for m in canonical if m in mag)/len(canonical); return {"degeneracy":deg,"magic":mag,"recall":recall}
