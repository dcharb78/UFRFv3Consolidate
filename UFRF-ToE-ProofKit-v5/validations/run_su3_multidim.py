
import numpy as np, math, json, os
from src.ym.torus_analysis import eigenphases, cartan_coords, chord_scores
from src.ym.wloop_fft2d import fft2d_power

def build_links(N=16, period=13, eps=0.2, seed=1):
    rng=np.random.default_rng(seed)
    Ux=[[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy=[[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase=2.0*math.pi*(x+y)/float(period)
            Jx=0.02*rng.standard_normal((3,3))+1j*0.02*rng.standard_normal((3,3))
            Jy=0.02*rng.standard_normal((3,3))+1j*0.02*rng.standard_normal((3,3))
            Jx=0.5*(Jx+Jx.conj().T); Jy=0.5*(Jy+Jy.conj().T)
            Ux[y][x]=np.linalg.expm(1j*(eps*np.sin(phase))*Jx)
            Uy[y][x]=np.linalg.expm(1j*(eps*np.cos(phase))*Jy)
    return Ux,Uy

def wilson_loop(Ux,Uy,x0,y0,L):
    N=len(Ux); idx=lambda a:a%N; U=np.eye(3,dtype=complex); x,y=x0,y0
    for _ in range(L): U=U@Ux[idx(y)][idx(x)]; x+=1
    for _ in range(L): U=U@Uy[idx(y)][idx(x)]; y+=1
    for _ in range(L): x-=1; U=U@Ux[idx(y)][idx(x)].conj().T
    for _ in range(L): y-=1; U=U@Uy[idx(y)][idx(x)].conj().T
    return U

def avg_W(Ux,Uy,L):
    N=len(Ux); tot=0.0
    for y in range(N):
        for x in range(N):
            U=wilson_loop(Ux,Uy,x,y,L); tot += (np.trace(U)/3.0).real
    return tot/(N*N)

def run_battery(N=16, Lmax=64, periods=(13,26), eps=0.2, seed=11):
    results={}
    for p in periods:
        Ux,Uy=build_links(N,period=p,eps=eps,seed=seed+p)
        W=np.zeros((Lmax,Lmax))
        for R in range(1,Lmax+1):
            for T in range(1,Lmax+1):
                W[R-1,T-1]=avg_W(Ux,Uy,min(R,T))
        P=fft2d_power(W)
        angs=[]; chords=[]
        for L in (8,16,32,48):
            U=wilson_loop(Ux,Uy,0,0,min(L,Lmax)); ang=eigenphases(U); angs.append(ang.tolist())
            phi=cartan_coords(ang); chords.append(chord_scores(phi))
        results[p]={"P_shape":P.shape,"P_sum":float(np.sum(P)),"eigenphases":angs,"chords":chords}
    return results

if __name__=='__main__':
    out=run_battery(); os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/su3_multidim.json","w") as f: json.dump(out,f,indent=2)
    print("Wrote artifacts/su3_multidim.json")
