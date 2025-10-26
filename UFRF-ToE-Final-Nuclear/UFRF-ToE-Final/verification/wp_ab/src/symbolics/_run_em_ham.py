import sympy as sp
from src.symbolics.em_hamiltonian_positivity import em_hamiltonian_density
resid, Pi1, Pi2, Pi3, symbols = em_hamiltonian_density()
print({"hamiltonian_residual": str(resid), "Pi_components": [str(Pi1), str(Pi2), str(Pi3)]})
