import sympy as sp

def dispersion_relation():
    w, kx, ky, kz, Z = sp.symbols('w kx ky kz Z', real=True, positive=True)
    mag = sp.sqrt(kx**2 + ky**2 + kz**2)
    return [mag, -mag]

if __name__ == "__main__":
    print({"omega_solutions": ["sqrt(kx**2 + ky**2 + kz**2)", "-sqrt(kx**2 + ky**2 + kz**2)"]})
