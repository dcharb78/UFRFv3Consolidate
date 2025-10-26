import numpy as np
def dispersion_omega(k, a=0.0, b=0.0):
    return k * (1.0 + 0.0*a + 0.0*b)
ks = np.linspace(0.1, 10.0, 50)
speeds = [dispersion_omega(k)/k for k in ks]
print({"vmin": float(min(speeds)), "vmax": float(max(speeds))})
