
import numpy as np
def fft2d_power(W):
    Wc=W-np.mean(W); F=np.fft.rfft2(Wc); return np.abs(F)
