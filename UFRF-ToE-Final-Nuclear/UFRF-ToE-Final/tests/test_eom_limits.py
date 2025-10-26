
import sympy as sp
from src.symbolics.derive_eom import coords, F, Ftilde, I1, Phi, Z_of_Phi, Theta_of_Phi, mu_of_Phi, nu_of_Phi, EOM_A

def _maxwell_limit_expr(nu_idx):
    # Set Z=1, mu=0, Theta,nu = constants (grad 0), and I1 arbitrary; then EOM_A reduces to ∂_μ F^{μν}
    Z_const = sp.Function('Z_const')
    Theta_const = sp.Function('Theta_const')
    nu_const = sp.Function('nu_const')

    subs_map = {}
    # Freeze running to constants
    subs_map.update({Z_of_Phi(Phi): 1})
    subs_map.update({mu_of_Phi(Phi): 0})
    subs_map.update({Theta_of_Phi(Phi): sp.Symbol('Theta0')})
    subs_map.update({nu_of_Phi(Phi): sp.Symbol('nu0')})

    expr = EOM_A[nu_idx].xreplace(subs_map)

    # Build explicit divergence ∂_μ F^{μν}
    div = sum(sp.diff(F[(mu_idx,nu_idx)], coords[mu_idx]) for mu_idx in range(4))

    return sp.simplify(expr - div)

def test_maxwell_limit_all_nu():
    for nu_idx in range(4):
        residual = _maxwell_limit_expr(nu_idx)
        # Should be identically zero if Maxwell limit holds
        assert sp.simplify(residual) == 0
