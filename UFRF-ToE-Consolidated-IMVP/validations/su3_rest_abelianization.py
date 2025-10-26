
import numpy as np, math

def f_comm_over_deriv(N=40, eps_amp=1.0, period=40.0, g=0.5):
    # smooth field with large Cartan (λ3, λ8) + small transverse scaled by eps_amp
    def A_mu(x,y,mu):
        s = math.sin(2*math.pi*(x+y)/period)
        c = math.cos(2*math.pi*(x-y)/period)
        A = np.zeros(8, dtype=float)
        if mu==0:
            A[2] = 0.6*s; A[7] = 0.5*c
            A[0] = eps_amp*0.1*math.sin(2*math.pi*x/period)
            A[1] = eps_amp*0.1*math.cos(2*math.pi*x/period)
        else:
            A[2] = 0.6*c; A[7] = 0.5*s
            A[0] = eps_amp*0.1*math.cos(2*math.pi*y/period)
            A[1] = eps_amp*0.1*math.sin(2*math.pi*y/period)
        return A
    f = np.zeros((8,8,8), dtype=float)
    def set_f(a,b,c,val):
        f[a,b,c]=val; f[b,c,a]=val; f[c,a,b]=val
        f[b,a,c]=-val; f[c,b,a]=-val; f[a,c,b]=-val
    set_f(0,1,2,1.0); set_f(0,3,6,0.5); set_f(1,4,6,0.5); set_f(2,3,4,0.5); set_f(2,5,6,0.5)
    xs = range(8, N-8, 4); ys = range(8, N-8, 4)
    num=0.0; den=0.0; cnt=0
    for x in xs:
        for y in ys:
            Ax = A_mu(x,y,0); Ay = A_mu(x,y,1)
            # comm piece
            comm = np.zeros(8, dtype=float)
            for a in range(8):
                s=0.0
                for b in range(8):
                    for c in range(8):
                        s += f[a,b,c]*Ax[b]*Ay[c]
                comm[a] = 0.5*s
            num += np.linalg.norm(comm)
            # deriv piece (fd)
            h=1.0
            def Ayd(xx,yy): return A_mu(xx,yy,1)
            def Axd(xx,yy): return A_mu(xx,yy,0)
            dAx = (Ayd(x+1,y)-Ayd(x-1,y))/(2*h)
            dAy = (Axd(x,y+1)-Axd(x,y-1))/(2*h)
            den += np.linalg.norm(dAx-dAy)+1e-18; cnt+=1
    return (num/cnt)/(den/cnt)

if __name__=='__main__':
    eps_list = [1.0,0.5,0.2,0.1,0.05]
    vals = []
    for e in eps_list:
        R = f_comm_over_deriv(N=40, eps_amp=e, period=40.0, g=0.5)
        vals.append((e,R))
    print("REST abelianization ε-scan (ε, ratio):", vals)
