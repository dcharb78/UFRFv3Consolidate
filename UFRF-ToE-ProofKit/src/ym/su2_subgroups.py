
import numpy as np

def project_su2(U, pair=(0,1)):
    # Extract 2x2 block corresponding to indices 'pair'
    i,j = pair
    return U[np.ix_([i,j],[i,j])]
