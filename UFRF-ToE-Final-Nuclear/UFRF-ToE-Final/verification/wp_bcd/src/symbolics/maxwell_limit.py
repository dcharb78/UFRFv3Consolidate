
import sympy as sp

def maxwell_dispersion():
    w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
    k2 = -w**2 + kx**2 + ky**2 + kz**2
    # Principal symbol of □ in Minkowski (−,+,+,+) gives ω^2 = |k|^2
    mag = sp.sqrt(kx**2 + ky**2 + kz**2)
    return sp.factor(k2), [mag, -mag]

if __name__ == "__main__":
    k2, branches = maxwell_dispersion()
    print({"dA_symbol": str(k2), "branches": [str(b) for b in branches]})
