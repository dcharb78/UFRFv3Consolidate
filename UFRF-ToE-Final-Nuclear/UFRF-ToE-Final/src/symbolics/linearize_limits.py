
# Placeholder for linearization tools around REST and vacuum
def speed_from_permittivity_permeability(eps, mu):
    # c = 1/sqrt(mu*eps) in units with c=1 -> eps*mu=1
    return (mu*eps)**-0.5
