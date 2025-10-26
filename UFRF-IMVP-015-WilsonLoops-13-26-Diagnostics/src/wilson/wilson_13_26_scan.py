
#!/usr/bin/env python3
import math, json, argparse, os

# Minimal SU(2) helper: represent group elements via Pauli-vector parameterization near identity.
def su2_from_axis_angle(ax, ay, az, theta):
    n = math.sqrt(ax*ax + ay*ay + az*az)
    if n < 1e-15:
        return (1.0, 0.0, 0.0, 0.0)  # identity
    ax, ay, az = ax/n, ay/n, az/n
    c = math.cos(theta/2.0)
    s = math.sin(theta/2.0)
    # quaternion form: q = c + i*s*(n·sigma) ; we keep (w, x, y, z)
    return (c, s*ax, s*ay, s*az)

def su2_mult(a, b):
    # quaternion multiplication (w,x,y,z)
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return (aw*bw - ax*bx - ay*by - az*bz,
            aw*bx + ax*bw + ay*bz - az*by,
            aw*by - ax*bz + ay*bw + az*bx,
            aw*bz + ax*by - ay*bx + az*bw)

def su2_tr(a):
    # trace in fundamental rep: Tr(U) = 2*Re(w) for SU(2) quaternion w component
    return 2.0*a[0]

def su2_inv(a):
    w,x,y,z = a
    n2 = w*w + x*x + y*y + z*z
    return (w/n2, -x/n2, -y/n2, -z/n2)

def build_links(N, period=13, epsilon=0.2, seed=1234):
    # Construct link variables Ux(x,y), Uy(x,y) with small angle around sigma_z (approx. Abelian),
    # modulated by a sinusoid with given period to emulate a 13/26 phase structure.
    random = __import__("random")
    random.seed(seed)
    Ux = [[(1.0,0.0,0.0,0.0) for _ in range(N)] for _ in range(N)]
    Uy = [[(1.0,0.0,0.0,0.0) for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            phase = 2.0*math.pi*(x+y)/float(period)
            # Small axial angle; include tiny non-Abelian tilt to avoid purely Abelian case
            ax, ay, az = 0.05*math.sin(phase), 0.05*math.cos(phase), 1.0
            theta = epsilon*(0.5 + 0.5*math.sin(phase))
            Ux[y][x] = su2_from_axis_angle(ax, ay, az, theta)
            Uy[y][x] = su2_from_axis_angle(ay, ax, az, theta*0.9)
    return Ux, Uy

def wilson_loop(Ux, Uy, x0, y0, L):
    # Compute square Wilson loop of side L starting at (x0,y0) with periodic BCs.
    N = len(Ux)
    def idx(a): return a % N
    U = (1.0,0.0,0.0,0.0)
    x, y = x0, y0
    # +x
    for _ in range(L):
        U = su2_mult(U, Ux[idx(y)][idx(x)])
        x += 1
    # +y
    for _ in range(L):
        U = su2_mult(U, Uy[idx(y)][idx(x)])
        y += 1
    # -x
    for _ in range(L):
        x -= 1
        U = su2_mult(U, su2_inv(Ux[idx(y)][idx(x)]))
    # -y
    for _ in range(L):
        y -= 1
        U = su2_mult(U, su2_inv(Uy[idx(y)][idx(x)]))
    return U

def average_wilson(Ux, Uy, L):
    N = len(Ux)
    tot = 0.0
    for y in range(N):
        for x in range(N):
            U = wilson_loop(Ux, Uy, x, y, L)
            tot += 0.5*su2_tr(U)  # normalize trace by 2
    return tot/(N*N)

def fft_power(seq):
    # naive DFT power spectrum for small sequences
    import cmath
    n = len(seq)
    out = []
    for k in range(n):
        s = 0j
        for j, val in enumerate(seq):
            angle = -2.0*math.pi*k*j/n
            s += val*complex(math.cos(angle), math.sin(angle))
        out.append(abs(s))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=24)
    ap.add_argument("--Lmax", type=int, default=10)
    ap.add_argument("--period", type=int, default=13, help="Injected spatial period (try 13 or 26).")
    args = ap.parse_args()

    Ux, Uy = build_links(args.N, period=args.period, epsilon=0.2)
    W = [average_wilson(Ux, Uy, L) for L in range(1, args.Lmax+1)]
    P = fft_power(W)

    # Identify peaks near 1/13 and 1/26 in normalized frequency space k/Lmax
    n = len(W)
    def nearest_index(freq):
        return max(0, min(n-1, int(round(freq*n))))
    idx_13 = nearest_index(1.0/13.0)
    idx_26 = nearest_index(1.0/26.0)
    report = {
        "N": args.N,
        "Lmax": args.Lmax,
        "period_injected": args.period,
        "wilson_values": W,
        "fft_peaks": {"k_1_13": P[idx_13], "k_1_26": P[idx_26]},
        "fft_all": P
    }

    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/wilson_scan.json", "w") as f:
        json.dump(report, f, indent=2)
    print(f"[IMVP-015] W(L=1..{args.Lmax}) = {', '.join(f'{v:.4f}' for v in W)}")
    print(f"[IMVP-015] |FFT| near 1/13: {P[idx_13]:.3e}  near 1/26: {P[idx_26]:.3e}")
    print("Saved artifacts/wilson_scan.json")

if __name__ == "__main__":
    main()
