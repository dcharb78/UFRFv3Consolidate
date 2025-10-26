#!/usr/bin/env python3
import numpy as np, math, argparse, json, os

import numpy as np

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

LAM = gell_mann()

def su3_expm_from_theta(theta):
    """
    Near-identity exponential map using 4th-order series + polar reunitarization.
    U = exp(i G), with G = sum_a theta[a] * lambda_a / 2
    """
    G = sum(theta[a]*LAM[a] for a in range(8)) / 2.0
    iG = 1j*G
    I = np.eye(3, dtype=complex)
    # 4th-order Taylor
    X = I + iG + 0.5*(iG@iG) + (1/6.0)*(iG@iG@iG) + (1/24.0)*(iG@iG@iG@iG)
    # Polar projection to SU(3)
    Uu, s, Vh = np.linalg.svd(X)
    Q = Uu @ Vh
    det = np.linalg.det(Q)
    Q /= det**(1/3)
    return Q


def build_links(N, period=13, eps=0.12, seed=5):
    rng = np.random.default_rng(seed)
    Ux = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            base = np.array([
                0.18*np.sin(phase), 0.15*np.cos(phase), 0.12*np.sin(2*phase),
                0.09*np.cos(2*phase), 0.07*np.sin(3*phase), 0.05*np.cos(3*phase),
                0.04*np.sin(4*phase), 0.03*np.cos(4*phase)
            ]) * eps
            thx = base + 0.02*rng.standard_normal(8)
            thy = 0.9*base + 0.02*rng.standard_normal(8)
            Ux[y][x] = su3_expm_from_theta(thx)
            Uy[y][x] = su3_expm_from_theta(thy)
    return Ux, Uy

def idx(a,N): return a % N

def WilsonLoop(Ux,Uy,x0,y0,R,T):
    N = len(Ux)
    def Idx(a): return a % N
    U = np.eye(3, dtype=complex)
    x,y = x0,y0
    for _ in range(R):
        U = U @ Ux[Idx(y)][Idx(x)]; x += 1
    for _ in range(T):
        U = U @ Uy[Idx(y)][Idx(x)]; y += 1
    for _ in range(R):
        x -= 1; U = U @ Ux[Idx(y)][Idx(x)].conj().T
    for _ in range(T):
        y -= 1; U = U @ Uy[Idx(y)][Idx(x)].conj().T
    return U

def avg_W(Ux,Uy,R,T):
    N = len(Ux)
    tot = 0.0
    for y in range(N):
        for x in range(N):
            U = WilsonLoop(Ux,Uy,x,y,R,T)
            tot += (np.trace(U)/3.0).real
    return tot/(N*N)

def creutz_ratio(Ux,Uy,L):
    # square Creutz ratio χ(L,L)
    WLL     = avg_W(Ux,Uy,L,L)
    WpLpL   = avg_W(Ux,Uy,L+1,L+1)
    WpLL    = avg_W(Ux,Uy,L+1,L)
    WLpL    = avg_W(Ux,Uy,L,L+1)
    num = WpLpL * WLL
    den = WpLL * WLpL
    if den <= 0 or num <= 0:
        return float('nan')
    return -math.log(num/den)

def scan(N=18,Lmax=7,period=13):
    out = []
    for eps in [1.0, 0.5, 0.2, 0.1, 0.05]:
        Ux,Uy = build_links(N,period=period,eps=eps)
        chis = [creutz_ratio(Ux,Uy,L) for L in range(1,Lmax+1)]
        out.append({"eps":eps,"chi":chis,"mean":np.nanmean(chis)})
        print(f"ε={eps:4.2f}  χ(L=1..{Lmax}) = " + ", ".join(f"{c:.4f}" if c==c else "nan" for c in chis))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=18)
    ap.add_argument("--Lmax", type=int, default=7)
    ap.add_argument("--period", type=int, default=13)
    args = ap.parse_args()
    res = scan(N=args.N,Lmax=args.Lmax,period=args.period)
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/su3_creutz_scan.json","w") as f:
        json.dump({"N":args.N,"Lmax":args.Lmax,"period":args.period,"results":res}, f, indent=2)
    print("Saved artifacts/su3_creutz_scan.json")

if __name__ == "__main__":
    main()
