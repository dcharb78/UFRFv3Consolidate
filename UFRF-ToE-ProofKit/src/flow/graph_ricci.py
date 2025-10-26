
import numpy as np

def forman_curvature(adj):
    # Simple Forman curvature on weighted graph adj (symmetric, zeros on diagonal)
    n = adj.shape[0]
    deg = np.sum(adj>0, axis=1)
    F = np.zeros_like(adj)
    for i in range(n):
        for j in range(n):
            if i!=j and adj[i,j]>0:
                s = 2.0
                for k in range(n):
                    if k!=i and k!=j and adj[i,k]>0 and adj[k,j]>0:
                        s -= 1.0/(np.sqrt(adj[i,k]*adj[k,j]))
                F[i,j] = s
    return F

def ricci_smooth(adj, tau=0.1, steps=1):
    A = adj.copy().astype(float)
    for _ in range(steps):
        F = forman_curvature(A)
        A = A - tau*F
        A[A<0]=0.0
    return A
