
import numpy as np

def fft2d_power(W):
    # W is 2D array over (R,T) of averaged Wilson loops
    Wc = W - np.mean(W)
    F = np.fft.rfft2(Wc)
    P = np.abs(F)
    return P
