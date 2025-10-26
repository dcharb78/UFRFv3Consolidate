
import numpy as np
def project_su2(U, pair=(0,1)): i,j=pair; return U[np.ix_([i,j],[i,j])]
