
import numpy as np
def trace_fundamental(U):  return float((np.trace(U)/3.0).real)
def trace_square(U):       return float((np.trace(U@U)/3.0).real)
def polyakov_eigenphases(U): return np.sort(np.angle(np.linalg.eigvals(U)))
