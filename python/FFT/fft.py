# fft.py
# FFT of a Gaussian

from numpy.fft import fft, fftshift, ifft
import numpy as np
from pylab import plot, show
from math import pi

L = 28
n = 128

x2 = np.linspace(-L/2,L/2,n+1) ; x = x2[1:n+1];

# Compute wave vector k
r = range(n/2) + range(-n/2,0)
k = (2*pi/L)*np.array(r)
print np.size(k), np.size(x)
u = np.exp(-x**2)
ut = fft(u)

plot(fftshift(k), abs(fftshift(ut)))
show()


sech = lambda x: 1.0/np.cosh(x)

u = sech(x)
ud = -sech(x)*np.tanh(x)
u2d = -sech(x)**3 * (np.sinh(x)**2 - 1)
u2d_other= sech(x) -2* sech(x)**3

ut = fft(u)
uds  = ifft((1j*k)*(ut))
u2ds = ifft( (1j*k)**2. * ut)
ks = fftshift(k)
plot(x, ud, 'r', x, uds, 'mo')
show()

