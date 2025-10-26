
#!/usr/bin/env python3
import math

def qed_alpha_running(mu, mu0, alpha0):
    # One-loop: alpha(mu) = alpha0 / (1 - beta0*alpha0*ln(mu/mu0)), beta0 = 2/(3π)
    beta0 = 2.0/(3.0*math.pi)
    L = math.log(mu/mu0)
    denom = 1.0 - beta0*alpha0*L
    return alpha0/denom

def qcd_alpha_running(mu, Lambda, Nc=3, Nf=5):
    # One-loop: alpha_s(mu) = 1 / (beta0 * ln(mu^2/Lambda^2)), beta0 = (11 Nc - 2 Nf)/(12 π)
    beta0 = (11.0*Nc - 2.0*Nf)/(12.0*math.pi)
    return 1.0/(beta0*math.log((mu*mu)/(Lambda*Lambda)))

def project_observed(g_star, dM, alpha_tech, S):
    # ln g_obs = ln g* + dM * alpha_tech * S
    return math.exp(math.log(g_star) + dM*alpha_tech*S)

def demo():
    mu0 = 1.0
    mu  = 10.0
    alpha0 = 1.0/137.036
    a_mu = qed_alpha_running(mu, mu0, alpha0)
    print(f"[QED] alpha({mu}) ≈ {a_mu:.9f} (from alpha({mu0})={alpha0:.9f})")

    # QCD sample
    alphas = qcd_alpha_running(mu=91.1876, Lambda=0.2, Nc=3, Nf=5)
    print(f"[QCD] alpha_s(mZ) ~ {alphas:.4f} (toy one-loop)")

    # Projection example (post-RG)
    dM = math.log(144000.0/144.0)  # observer–target distance ~ ln 1000
    g_obs = project_observed(a_mu, dM=dM, alpha_tech=0.3, S=-0.1)
    print(f"[Proj] projected alpha ~ {g_obs:.9f} for (alpha_tech=0.3, S=-0.1)")

if __name__ == "__main__":
    demo()
