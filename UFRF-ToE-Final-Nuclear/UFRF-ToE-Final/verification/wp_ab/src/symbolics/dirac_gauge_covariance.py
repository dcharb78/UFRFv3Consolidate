
import sympy as sp

def dirac_local_U1_covariance():
    # Symbols and fields
    x = sp.symbols('x0:4', real=True)
    q = sp.symbols('q', real=True)
    I = sp.I
    chi = sp.Function('chi')(*x)         # gauge parameter χ(x)
    psi = sp.Function('psi')(*x)         # abstract scalar stand-in for spinor (commutes with scalars)
    A = [sp.Function(f"A{mu}")(*x) for mu in range(4)]
    # Define D_mu ψ = ∂_μ ψ + i q A_μ ψ  (we only track scalar factors; gamma structure commutes with scalars)
    def D(mu, field):
        return sp.diff(field, x[mu]) + I*q*A[mu]*field
    # Gauge transform: ψ' = e^{-i q χ} ψ ,  A_μ' = A_μ + ∂_μ χ
    phase = sp.exp(-I*q*chi)
    psi_p = phase*psi
    A_p = [A[mu] + sp.diff(chi, x[mu]) for mu in range(4)]
    def Dprime(mu, field):
        # D'_μ built from transformed A and acting on 'field'
        return sp.diff(field, x[mu]) + I*q*A_p[mu]*field
    # Compute e^{+i q χ} D'_μ ( e^{-i q χ} ψ ) - D_μ ψ  ; should be 0 (covariance)
    resid = [ sp.simplify(sp.exp(I*q*chi)*Dprime(mu, psi_p) - D(mu, psi)) for mu in range(4) ]
    cov_ok = all(r == 0 for r in resid)
    # If D transforms covariantly, then L_D = ψ̄ (i γ^μ D_μ - m) ψ is invariant (spinor indices suppressed).
    return cov_ok, [sp.simplify(r) for r in resid]

if __name__ == "__main__":
    ok, resid = dirac_local_U1_covariance()
    print({"dirac_local_U1_covariance": ok, "residuals": [str(r) for r in resid]})
