import math

def plane_wave_fields(A0=1.0, k=1.0, w=1.0, z=0.0, t=0.0):
    phase = k*z - w*t
    Ex = -w*A0*math.sin(phase)
    Ey, Ez = 0.0, 0.0
    Bx, By, Bz = 0.0, -k*A0*math.sin(phase), 0.0
    return (Ex,Ey,Ez), (Bx,By,Bz)

def residuals(A0=1.0, k=1.0, w=1.0, z=0.123, t=0.456):
    dz = 1e-6
    dt = 1e-6
    def E(z,t): return plane_wave_fields(A0,k,w,z,t)[0]
    def B(z,t): return plane_wave_fields(A0,k,w,z,t)[1]

    Ez_p = E(z+dz,t)[2]; Ez_m = E(z-dz,t)[2]
    Bz_p = B(z+dz,t)[2]; Bz_m = B(z-dz,t)[2]
    divE = (Ez_p - Ez_m)/(2*dz)
    divB = (Bz_p - Bz_m)/(2*dz)

    Ex_p = E(z+dz,t)[0]; Ex_m = E(z-dz,t)[0]
    By_p = B(z+dz,t)[1]; By_m = B(z-dz,t)[1]
    curlE_y = (Ex_p - Ex_m)/(2*dz)
    curlB_x = - (By_p - By_m)/(2*dz)

    Ex_p_t = E(z,t+dt)[0]; Ex_m_t = E(z,t-dt)[0]
    By_p_t = B(z,t+dt)[1]; By_m_t = B(z,t-dt)[1]
    dEdt_x = (Ex_p_t - Ex_m_t)/(2*dt)
    dBdt_y = (By_p_t - By_m_t)/(2*dt)

    r_faraday_y = curlE_y + dBdt_y
    r_ampere_x = curlB_x - dEdt_x
    return {"divE": divE, "divB": divB, "faraday_y": r_faraday_y, "ampere_x": r_ampere_x}

def check(w=1.0, k=1.0):
    r = residuals(k=k, w=w)
    vals = list(r.values())
    rms = math.sqrt(sum(v*v for v in vals)/len(vals))
    return r, rms
