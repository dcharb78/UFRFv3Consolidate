
import numpy as np
from src.projection.fit import fit_projection
rng = np.random.default_rng(0)
r = np.exp(rng.uniform(-3,3,size=60))
a = rng.uniform(0.1,0.9,size=60)
lnO = np.log(1.37) + a*np.log(r)*(-0.05) + rng.normal(0,0.01,size=60)
O = np.exp(lnO)
fit = fit_projection(r,O,a)
print("Projection fit:", fit)
