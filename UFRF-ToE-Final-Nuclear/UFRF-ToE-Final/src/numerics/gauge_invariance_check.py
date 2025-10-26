import math

def finite_diff(arr, axis, h):
    # axis 0: z, axis 1: t
    nz, nt = len(arr), len(arr[0])
    out = [[0.0]*nt for _ in range(nz)]
    if axis == 0:
        for i in range(1, nz-1):
            for j in range(nt):
                out[i][j] = (arr[i+1][j] - arr[i-1][j])/(2*h)
        # one-sided at boundaries
        for j in range(nt):
            out[0][j]  = (arr[1][j] - arr[0][j])/h
            out[-1][j] = (arr[-1][j] - arr[-2][j])/h
    else:
        for i in range(nz):
            for j in range(1, nt-1):
                out[i][j] = (arr[i][j+1] - arr[i][j-1])/(2*h)
        for i in range(nz):
            out[i][0]  = (arr[i][1] - arr[i][0])/h
            out[i][-1] = (arr[i][-1] - arr[i][-2])/h
    return out

def build_plane_wave(A0=1.0, k=1.0, w=1.0, chi0=0.7, Lz=2*math.pi, Lt=2*math.pi, Nz=257, Nt=257):
    dz = Lz/(Nz-1)
    dt = Lt/(Nt-1)
    zgrid = [i*dz for i in range(Nz)]
    tgrid = [j*dt for j in range(Nt)]
    # potentials
    Ax = [[A0*math.cos(k*z - w*t) for t in tgrid] for z in zgrid]
    Ay = [[0.0 for t in tgrid] for z in zgrid]
    Az = [[0.0 for t in tgrid] for z in zgrid]
    phi = [[0.0 for t in tgrid] for z in zgrid]
    # gauge function chi(z,t)
    chi = [[chi0*math.sin(0.7*k*z - 1.3*w*t) for t in tgrid] for z in zgrid]
    dchi_dt = finite_diff(chi, axis=1, h=dt)
    dchi_dz = finite_diff(chi, axis=0, h=dz)
    # gauge-transformed potentials: A' = A + ∇chi, phi' = phi - ∂chi/∂t
    Ax_p = Ax  # no x-dependence in chi, so Ax unchanged
    Ay_p = Ay
    Az_p = [[Az[i][j] + dchi_dz[i][j] for j in range(Nt)] for i in range(Nz)]
    phi_p = [[phi[i][j] - dchi_dt[i][j] for j in range(Nt)] for i in range(Nz)]
    return (Ax,Ay,Az,phi), (Ax_p,Ay_p,Az_p,phi_p), (dz,dt)

def curl_z(Ax, Ay, dz):  # only z-dependence: (∇×A)_y = ∂A_x/∂z
    return finite_diff(Ax, axis=0, h=dz)

def E_from_potentials(Ax, Ay, Az, phi, dt, dz):
    # E = -∂A/∂t - ∇phi. With z-only variation, ∇phi=(∂phi/∂z) zhat
    dAx_dt = finite_diff(Ax, axis=1, h=dt)
    dAy_dt = finite_diff(Ay, axis=1, h=dt)
    dAz_dt = finite_diff(Az, axis=1, h=dt)
    dphi_dz = finite_diff(phi, axis=0, h=dz)
    # components
    Ex = [[-dAx_dt[i][j] for j in range(len(Ax[0]))] for i in range(len(Ax))]
    Ey = [[-dAy_dt[i][j] for j in range(len(Ax[0]))] for i in range(len(Ax))]
    Ez = [[-dAz_dt[i][j] - dphi_dz[i][j] for j in range(len(Ax[0]))] for i in range(len(Ax))]
    return Ex,Ey,Ez

def B_from_potentials(Ax, Ay, Az, dz):
    # With z-only dependence, B has only y-component: By = ∂A_x/∂z
    By = curl_z(Ax, Ay, dz)
    Bx = [[0.0 for _ in row] for row in Ax]
    Bz = [[0.0 for _ in row] for row in Ax]
    return Bx,By,Bz

def max_abs_diff(A,B):
    m = 0.0
    for i in range(len(A)):
        for j in range(len(A[0])):
            m = max(m, abs(A[i][j]-B[i][j]))
    return m

def gauge_check():
    (Ax,Ay,Az,phi), (Axp,Ayp,Azp,phip), (dz,dt) = build_plane_wave()
    Ex,Ey,Ez = E_from_potentials(Ax,Ay,Az,phi,dt,dz)
    Bx,By,Bz = B_from_potentials(Ax,Ay,Az,dz)
    Exp,Eyp,Ezp = E_from_potentials(Axp,Ayp,Azp,phip,dt,dz)
    Bxp,Byp,Bzp = B_from_potentials(Axp,Ayp,Azp,dz)
    return {
        "max_abs_diff_E": max_abs_diff(Ex,Exp)+max_abs_diff(Ey,Eyp)+max_abs_diff(Ez,Ezp),
        "max_abs_diff_B": max_abs_diff(Bx,Bxp)+max_abs_diff(By,Byp)+max_abs_diff(Bz,Bzp)
    }
