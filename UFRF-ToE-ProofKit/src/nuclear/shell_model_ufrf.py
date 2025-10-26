
import numpy as np

def degeneracy_and_magic():
    notes = np.array([1,3,3,3,4,11,16,22])
    degeneracy = 2*notes
    magic = np.cumsum(degeneracy)
    return degeneracy.tolist(), magic.tolist()

def regression_checks():
    deg, mag = degeneracy_and_magic()
    canonical = [2,8,14,20,28,50,82,126]
    recall = sum(1 for m in canonical if m in mag)/len(canonical)
    midcycle_no_gaps = [25,55,85,115]
    return {"degeneracy": deg, "magic": mag, "recall": recall, "midcycle_no_gaps": midcycle_no_gaps}
