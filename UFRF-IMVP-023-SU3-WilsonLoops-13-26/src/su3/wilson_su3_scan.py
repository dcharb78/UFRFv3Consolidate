#!/usr/bin/env python3
import numpy as np, math, json, argparse, os

def gell_mann():
    zeros = np.zeros((3,3), dtype=complex)
    l1 = zeros.copy(); l1[0,1]=l1[1,0]=1
    l2 = zeros.copy(); l2[0,1]=-1j; l2[1,0]=1j
    l3 = zeros.copy(); l3[0,0]=1; l3[1,1]=-1
    l4 = zeros.copy(); l4[0,2]=l4[2,0]=1
    l5 = zeros.copy(); l5[0,2]=-1j; l5[2,0]=1j
    l6 = zeros.copy(); l6[1,2]=l6[2,1]=1
    l7 = zeros.copy(); l7[1,2]=-1j; l7[2,1]=1j
    l8 = (1/np.sqrt(3))*np.diag([1,1,-2]).astype(complex)
    return [l1,l2,l3,l4,l5,l6,l7,l8]

LAM = gell_mann()

def su3_near_identity(theta):
    G = sum(theta[a]*LAM[a] for a in range(8)) / 2.0
    iG = 1j*G
    I = np.eye(3, dtype=complex)
    X = I + iG + 0.5*(iG@iG) + (1/6.0)*(iG@iG@iG) + (1/24.0)*(iG@iG@iG@iG)
    Uu, s, Vh = np.linalg.svd(X)
    Q = Uu @ Vh
    det = np.linalg.det(Q)
    Q /= det**(1/3)
    return Q

def build_links(N, period=13, eps=0.15, seed=123):
    rng = np.random.default_rng(seed)
    Ux = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    Uy = [[np.eye(3,dtype=complex) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            base = np.array([
                0.15*np.sin(phase), 0.12*np.cos(phase), 0.10*np.sin(2*phase),
                0.08*np.cos(2*phase), 0.06*np.sin(3*phase), 0.05*np.cos(3*phase),
                0.04*np.sin(4*phase), 0.03*np.cos(4*phase)
            ]) * eps
            thx = base + 0.02*rng.standard_normal(8)
            thy = 0.9*base + 0.02*rng.standard_normal(8)
            Ux[y][x] = su3_near_identity(thx)
            Uy[y][x] = su3_near_identity(thy)
    return Ux, Uy

def wilson_loop(Ux, Uy, x0, y0, L):
    N = len(Ux)
    def idx(a): return a % N
    U = np.eye(3, dtype=complex)
    x, y = x0, y0
    for _ in range(L):
        U = U @ Ux[idx(y)][idx(x)]; x += 1
    for _ in range(L):
        U = U @ Uy[idx(y)][idx(x)]; y += 1
    for _ in range(L):
        x -= 1; U = U @ Ux[idx(y)][idx(x)].conj().T
    for _ in range(L):
        y -= 1; U = U @ Uy[idx(y)][idx(x)].conj().T
    return U

def average_wilson(Ux, Uy, L):
    N = len(Ux)
    tot = 0.0
    for y in range(N):
        for x in range(N):
            U = wilson_loop(Ux, Uy, x, y, L)
            tr = np.trace(U)
            tot += (tr/3.0).real
    return tot/(N*N)

def fft_power(seq):
    arr = np.array(seq, dtype=float)
    F = np.fft.rfft(arr)
    P = np.abs(F)
    return P

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=16)
    ap.add_argument("--Lmax", type=int, default=8)
    ap.add_argument("--period", type=int, default=13)
    args = ap.parse_args()
    Ux, Uy = build_links(args.N, period=args.period)
    W = [average_wilson(Ux, Uy, L) for L in range(1, args.Lmax+1)]
    P = fft_power(W)
    n = len(W)
    i13 = int(round((1.0/13.0)*n/2))
    i26 = int(round((1.0/26.0)*n/2))
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/su3_wilson.json","w") as f:
        json.dump({"W": W, "P": P.tolist(), "idx_1_13": i13, "idx_1_26": i26}, f, indent=2)
    print(f"[IMVP-023] W(L=1..{args.Lmax}) = {', '.join(f'{v:.4f}' for v in W)}")
    print(f"[IMVP-023] |FFT| near 1/13: {P[i13]:.3e}  near 1/26: {P[i26]:.3e}")
    print("Saved artifacts/su3_wilson.json")

if __name__ == "__main__":
    main()
