
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

def build_links(N=16, period=13, eps=0.12, seed=7):
    rng = np.random.default_rng(seed)
    LAM = gell_mann()
    def exp_from_theta(theta):
        G = sum(theta[a]*LAM[a] for a in range(8))/2.0
        iG = 1j*G
        I = np.eye(3, dtype=complex)
        X = I + iG + 0.5*(iG@iG) + (1/6.0)*(iG@iG@iG) + (1/24.0)*(iG@iG@iG@iG)
        U,S,Vh = np.linalg.svd(X); Q = U@Vh
        det = np.linalg.det(Q); Q/=det**(1/3)
        return Q
    Ux = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            base = np.array([0.20*np.sin(phase), 0.16*np.cos(phase), 0.12*np.sin(2*phase),
                             0.10*np.cos(2*phase), 0.08*np.sin(3*phase), 0.06*np.cos(3*phase),
                             0.05*np.sin(4*phase), 0.04*np.cos(4*phase)]) * eps
            thx = base + 0.02*rng.standard_normal(8)
            thy = 0.9*base + 0.02*rng.standard_normal(8)
            Ux[y][x] = exp_from_theta(thx)
            Uy[y][x] = exp_from_theta(thy)
    return Ux,Uy

def wilson_loop(Ux,Uy,x0,y0,L):
    N = len(Ux); idx=lambda a:a%N
    U = np.eye(3, dtype=complex)
    x,y=x0,y0
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

def random_su3(rng, scale=0.25):
    from src.gauge.su_groups import su3_exp_from_theta
    theta = scale * rng.standard_normal(8)
    return su3_exp_from_theta(theta)

def gauge_transform(Ux,Uy,g):
    N=len(Ux)
    Ux2=[[None]*N for _ in range(N)]
    Uy2=[[None]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            Ux2[y][x] = g[y][x] @ Ux[y][x] @ g[y][(x+1)%N].conj().T
            Uy2[y][x] = g[y][x] @ Uy[y][x] @ g[(y+1)%N][x].conj().T
    return Ux2,Uy2

if __name__=='__main__':
    import numpy as np
    Ux,Uy = build_links()
    pre = [avg_W(Ux,Uy,L) for L in range(1,9)]
    rng = np.random.default_rng(42)
    g = [[random_su3(rng,0.4) for _ in range(16)] for _ in range(16)]
    Ux2,Uy2 = gauge_transform(Ux,Uy,g)
    post = [avg_W(Ux2,Uy2,L) for L in range(1,9)]
    rel = [abs(post[i]-pre[i])/max(1e-12,abs(pre[i])) for i in range(8)]
    print("Gauge invariance rel. errors per L:", rel)
