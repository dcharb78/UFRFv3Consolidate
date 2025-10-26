
import numpy as np, math
from src.gauge.su_groups import su3_exp_from_theta

def gell_mann():
    Z = np.zeros((3,3), dtype=complex)
    l1 = Z.copy(); l1[0,1]=l1[1,0]=1
    l2 = Z.copy(); l2[0,1]=-1j; l2[1,0]=1j
    l3 = Z.copy(); l3[0,0]=1; l3[1,1]=-1
    l4 = Z.copy(); l4[0,2]=l4[2,0]=1
    l5 = Z.copy(); l5[0,2]=-1j; l5[2,0]=1j
    l6 = Z.copy(); l6[1,2]=l6[2,1]=1
    l7 = Z.copy(); l7[1,2]=-1j; l7[2,1]=1j
    l8 = (1/np.sqrt(3))*np.diag([1,1,-2]).astype(complex)
    return [l1,l2,l3,l4,l5,l6,l7,l8]

def build_links(N, period=13, eps=0.12, seed=1):
    rng = np.random.default_rng(seed); LAM = gell_mann()
    def exp_from_theta(theta):
        G = sum(theta[a]*LAM[a] for a in range(8))/2.0
        iG = 1j*G; I = np.eye(3, dtype=complex)
        X = I + iG + 0.5*(iG@iG) + (1/6.0)*(iG@iG@iG) + (1/24.0)*(iG@iG@iG@iG)
        U,S,Vh = np.linalg.svd(X); Q = U@Vh; det=np.linalg.det(Q); Q/=det**(1/3); return Q
    Ux = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            base = np.array([0.20*np.sin(phase), 0.16*np.cos(phase), 0.12*np.sin(2*phase),
                             0.10*np.cos(2*phase), 0.08*np.sin(3*phase), 0.06*np.cos(3*phase),
                             0.05*np.sin(4*phase), 0.04*np.cos(4*phase)]) * eps
            thx = base + 0.02*rng.standard_normal(8); thy = 0.9*base + 0.02*rng.standard_normal(8)
            Ux[y][x] = exp_from_theta(thx); Uy[y][x] = exp_from_theta(thy)
    return Ux,Uy

def wilson_loop(Ux,Uy,x0,y0,L):
    N=len(Ux); idx=lambda a:a%N
    U=np.eye(3,dtype=complex); x,y=x0,y0
    for _ in range(L): U=U@Ux[idx(y)][idx(x)]; x+=1
    for _ in range(L): U=U@Uy[idx(y)][idx(x)]; y+=1
    for _ in range(L): x-=1; U=U@Ux[idx(y)][idx(x)].conj().T
    for _ in range(L): y-=1; U=U@Uy[idx(y)][idx(x)].conj().T
    return U

def avg_W(Ux,Uy,L):
    N=len(Ux); tot=0.0
    for y in range(N):
        for x in range(N):
            U = wilson_loop(Ux,Uy,x,y,L)
            tot += (np.trace(U)/3.0).real
    return tot/(N*N)

def fft_power(seq):
    arr=np.array(seq,dtype=float); F=np.fft.rfft(arr-np.mean(arr)); return np.abs(F)

if __name__=='__main__':
    N=16; Lmax=32
    for period in (13,26):
        Ux,Uy = build_links(N, period=period, eps=0.12, seed=11+period)
        W = [avg_W(Ux,Uy,L) for L in range(1,Lmax+1)]
        P = fft_power(W)
        # simple indices near the fractional bins
        k13 = max(0, min(len(P)-1, int(round((1/13.0)*len(P)/2))))
        k26 = max(0, min(len(P)-1, int(round((1/26.0)*len(P)/2))))
        print(f"period={period}  |FFT|[~1/13]={P[k13]:.3e}  |FFT|[~1/26]={P[k26]:.3e}")
