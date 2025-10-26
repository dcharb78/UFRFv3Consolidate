
import numpy as np

def emergent_metric(E, B, gradPhi, a=0.0, b=0.0, c=0.0):
    """
    Build a simple algebraic disformal metric:
      g = eta + a*eta*I1 + b*F_mu^alpha F_{nu alpha} + c*∂_muPhi ∂_nuPhi
    Here we collapse to a diagonal sketch using invariants in the lab frame.
    """
    # Minkowski eta = diag(-1,1,1,1)
    eta = np.diag([-1.0,1.0,1.0,1.0])
    E = np.asarray(E); B = np.asarray(B); gradPhi = np.asarray(gradPhi)
    I1 = 2.0*(np.dot(B,B) - np.dot(E,E))  # 2(B^2 - E^2)
    # Collapse F^T F contribution to spatial diagonal with |E|^2+|B|^2 proxy
    em_proxy = (np.dot(E,E)+np.dot(B,B))
    Fterm = np.diag([0.0, em_proxy, em_proxy, em_proxy])
    dphi = np.zeros((4,4)); dphi += np.outer(gradPhi, gradPhi)
    g = eta + a*I1*eta + b*Fterm + c*dphi
    return g
