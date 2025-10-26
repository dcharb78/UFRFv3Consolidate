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


def random_su3(rng, scale=0.25):
    theta = scale * rng.standard_normal(8)
    return su3_expm_from_theta(theta)

def build_links(N, period=13, eps=0.12, seed=7):
    rng = np.random.default_rng(seed)
    Ux = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            base = np.array([
                0.16*np.sin(phase), 0.13*np.cos(phase), 0.11*np.sin(2*phase),
                0.09*np.cos(2*phase), 0.07*np.sin(3*phase), 0.05*np.cos(3*phase),
                0.04*np.sin(4*phase), 0.03*np.cos(4*phase)
            ]) * eps
            thx = base + 0.02*rng.standard_normal(8)
            thy = 0.9*base + 0.02*rng.standard_normal(8)
            Ux[y][x] = su3_expm_from_theta(thx)
            Uy[y][x] = su3_expm_from_theta(thy)
    return Ux, Uy

def gauge_transform(Ux,Uy,g):
    N = len(Ux)
    Ux2 = [[None]*N for _ in range(N)]
    Uy2 = [[None]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            Ux2[y][x] = g[y][x] @ Ux[y][x] @ g[y][(x+1)%N].conj().T
            Uy2[y][x] = g[y][x] @ Uy[y][x] @ g[(y+1)%N][x].conj().T
    return Ux2, Uy2

def idx(a,N): return a % N

def Wloop(Ux,Uy,x0,y0,L):
    N = len(Ux)
    def Idx(a): return a % N
    U = np.eye(3, dtype=complex)
    x,y = x0,y0
    for _ in range(L):
        U = U @ Ux[Idx(y)][Idx(x)]; x += 1
    for _ in range(L):
        U = U @ Uy[Idx(y)][Idx(x)]; y += 1
    for _ in range(L):
        x -= 1; U = U @ Ux[Idx(y)][Idx(x)].conj().T
    for _ in range(L):
        y -= 1; U = U @ Uy[Idx(y)][Idx(x)].conj().T
    return (np.trace(U)/3.0).real

def avg_W(Ux,Uy,L):
    N = len(Ux)
    tot = 0.0
    for y in range(N):
        for x in range(N):
            tot += Wloop(Ux,Uy,x,y,L)
    return tot/(N*N)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=16)
    ap.add_argument("--Lmax", type=int, default=8)
    ap.add_argument("--period", type=int, default=13)
    ap.add_argument("--seed", type=int, default=11)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    Ux,Uy = build_links(args.N, period=args.period, seed=args.seed)
    pre = [avg_W(Ux,Uy,L) for L in range(1, args.Lmax+1)]
    g = [[random_su3(rng, 0.4) for _ in range(args.N)] for _ in range(args.N)]
    Ux2,Uy2 = gauge_transform(Ux,Uy,g)
    post = [avg_W(Ux2,Uy2,L) for L in range(1, args.Lmax+1)]
    rel = [abs(post[i]-pre[i]) / max(1e-12, abs(pre[i])) for i in range(len(pre))]

    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/gauge_invariance.json","w") as f:
        json.dump({"pre":pre,"post":post,"rel_error":rel}, f, indent=2)
    print("W(L) pre:  " + ", ".join(f"{w:.6f}" for w in pre))
    print("W(L) post: " + ", ".join(f"{w:.6f}" for w in post))
    print("rel Δ:      " + ", ".join(f"{r:.2e}" for r in rel))
    print("Saved artifacts/gauge_invariance.json")

if __name__ == "__main__":
    main()
