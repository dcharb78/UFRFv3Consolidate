
import sympy as sp

def principal_symbol_variable_couplings():
    # Symbols
    w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
    k2 = -w**2 + kx**2 + ky**2 + kz**2
    Z = sp.symbols('Z', positive=True, real=True)   # local value Z(Φ(x0))
    # In Lorenz gauge, principal part: Z □ A^ν  ⇒  symbol M = Z*(-k^2) δ^ν_σ on physical subspace
    # Return dispersion ω = ±|k| and the symbol factor
    mag = sp.sqrt(kx**2 + ky**2 + kz**2)
    return {"omega_branches": [mag, -mag], "symbol_factor": sp.simplify(-Z*k2)}

if __name__ == "__main__":
    out = principal_symbol_variable_couplings()
    print({"omega_branches": [str(s) for s in out["omega_branches"]], "symbol_factor": str(out["symbol_factor"]) })
