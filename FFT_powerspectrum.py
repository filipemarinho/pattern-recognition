# Da documentação https://docs.scipy.org/doc/numpy/reference/routines.fft.html
# "When the input a is a time-domain signal and A = fft(a), np.abs(A) is its amplitude spectrum and np.abs(A)**2 is its power spectrum. The phase spectrum is obtained by np.angle(A)."

import numpy as np

def PowerSpec(sequence):
    fft = np.fft.fft(sequence)
    spec =(np.abs(fft))**2 #
    return spec
