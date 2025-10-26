
#!/usr/bin/env python3
# Minimal SU(2) field: compute F = dA + g A∧A and a discrete Bianchi check on a 2D grid.
import math

# SU(2) structure constants: f^{abc} = epsilon^{abc}
def eps(a,b,c):
    # Levi-Civita for a,b,c in {0,1,2} mapping to {1,2,3} indices
    perm = (a,b,c)
    if len(set(perm))<3: return 0.0
    if perm in [(0,1,2),(1,2,0),(2,0,1)]: return 1.0
    return -1.0

# Grid and gauge
nx, ny = 40, 40
Lx, Ly  = 2.0, 2.0
dx, dy  = Lx/nx, Ly/ny
g = 0.5

def A_mu_a(x,y,mu,a):
    # Simple ansatz: A_x^1 = sin(πx)cos(πy), A_y^2 = cos(πx)sin(πy), others 0
    # mu: 0->x, 1->y ; a: 0,1,2 for SU(2)
    if mu==0 and a==0:
        return math.sin(math.pi*x)*math.cos(math.pi*y)
    if mu==1 and a==1:
        return math.cos(math.pi*x)*math.sin(math.pi*y)
    return 0.0

def d_mu(f, x, y, mu):
    h = dx if mu==0 else dy
    if mu==0:
        return (f(x+h,y)-f(x-h,y))/(2*h)
    else:
        return (f(x,y+h)-f(x,y-h))/(2*h)

def F_mu_nu_a(x,y,mu,nu,a):
    # ∂_μ A^a_ν − ∂_ν A^a_μ + g f^{abc} A^b_μ A^c_ν
    def A(mu,a): return A_mu_a(x,y,mu,a)
    dA = d_mu(lambda xx,yy: A_mu_a(xx,yy,nu,a), x,y,mu) - d_mu(lambda xx,yy: A_mu_a(xx,yy,mu,a), x,y,nu)
    comm = 0.0
    for b in range(3):
        for c in range(3):
            comm += eps(a,b,c)*A(mu,b)*A(nu,c)
    return dA + g*comm

def bianchi_residual(x,y):
    # D_[μ F_{νρ]} ≈ cycles over (x,y,t) but here spatial 2D, do a surrogate cyclic sum over indices (x,y) with fake t=0
    # We'll evaluate a discrete curl-like cyclic sum.
    mu, nu = 0, 1
    res = 0.0
    for a in range(3):
        # spatial cyclic surrogate: ∂_x F^a_{y?} + ∂_y F^a_{?x} ≈ 0 (toy)
        # We'll take ∂_x F^a_{y0} + ∂_y F^a_{0x} with A_0=0 -> reduces to ∂_x F^a_{y0} + ∂_y F^a_{0x} = 0
        # Using only spatial F_{xy} here:
        fxy = F_mu_nu_a(x,y,0,1,a)
        # discrete divergence of F_{xy}
        df_dx = (F_mu_nu_a(x+dx,y,0,1,a) - F_mu_nu_a(x-dx,y,0,1,a))/(2*dx)
        df_dy = (F_mu_nu_a(x,y+dy,0,1,a) - F_mu_nu_a(x,y-dy,0,1,a))/(2*dy)
        res += abs(df_dx + df_dy)
    return res

def run():
    # sample points
    xs = [i*dx for i in range(1,nx-1, max(1, nx//8))]
    ys = [j*dy for j in range(1,ny-1, max(1, ny//8))]
    f_norm = 0.0
    b_sum  = 0.0
    count  = 0
    for x in xs:
        for y in ys:
            for a in range(3):
                f = F_mu_nu_a(x,y,0,1,a)
                f_norm += abs(f)
            b_sum += bianchi_residual(x,y)
            count += 1
    print(f"[YM] avg |F_xy| over samples ~ {f_norm/(count*3):.3e}")
    print(f"[YM] avg Bianchi residual (toy) ~ {b_sum/count:.3e}")
    print("Lower is better for residual; nonzero F indicates field curvature present.")

if __name__ == "__main__":
    run()
