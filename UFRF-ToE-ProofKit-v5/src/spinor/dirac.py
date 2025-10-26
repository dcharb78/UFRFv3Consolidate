
import numpy as np

def gamma_matrices():
    I2 = np.eye(2); O2 = np.zeros((2,2))
    sigma1 = np.array([[0,1],[1,0]])
    sigma2 = np.array([[0,-1j],[1j,0]])
    sigma3 = np.array([[1,0],[0,-1]])
    gamma0 = np.block([[I2, O2],[O2, -I2]])
    gammai = [
        np.block([[O2, sigma1],[-sigma1, O2]]),
        np.block([[O2, sigma2],[-sigma2, O2]]),
        np.block([[O2, sigma3],[-sigma3, O2]]),
    ]
    return gamma0, gammai

def plane_wave_spinor(p_vec, m=1.0):
    px,py,pz = map(float, p_vec)
    p2 = px*px+py*py+pz*pz
    E = np.sqrt(m*m + p2)
    u = np.zeros((4,1), dtype=complex)
    u[0,0]=np.sqrt(E+m); u[1,0]=0
    u[2,0]=pz/np.sqrt(E+m); u[3,0]=0
    return u, E

def current_density(psi):
    gamma0, gammai = gamma_matrices()
    psi_d = (psi.conj().T) @ gamma0
    j0 = float(np.real(psi_d @ psi))
    j = [float(np.real(psi_d @ (G @ psi))) for G in gammai]
    return j0, np.array(j)

def minimal_coupling_shift(p_vec, A_mu, e=1.0):
    p = np.array(p_vec, float); A = np.array(A_mu, float)
    E0 = np.sqrt(np.dot(p,p)+1.0); E = E0 - e*A[0]
    p_shift = p - e*A[1:4]
    return E, p_shift
