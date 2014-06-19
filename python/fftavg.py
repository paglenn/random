import numpy as np
from numpy.fft import fft, ifft, fftshift
from pylab import *
from math import *

T = 30
n  =512

t = np.linspace(-T/2,T/2,n+1)[0:n]
r = range(0, n/2) + range(-n/2,0)
k = (2*pi/T) * np.array(r)
ks = fftshift(k)

sech = lambda x: 1./np.cosh(x)
u = sech(t)
ut = fft(u) # Fast fourier transform in O(NlogN)

# Gaussian 'white' noise: All colors
from numpy.random import randn
noise = 30
utn = ut + noise* ( randn(n) + 1j * randn(n) )
un = ifft(utn)

'''
subplot(211)
plot(t,u,'r')
plot(t, abs(un),'k')
'''
#subplot(212)
#plot(ks, abs(fftshift(ut)), 'r')
#plot(ks, abs(fftshift(utn)), 'b')
#show()
ave = np.zeros((n))
realizations = 100
ion()
pl = plot(ks, abs(fftshift(ut)), 'r')
pl2, = plot(ks, ave,'k')

'''
import time
for j in range(1,realizations+1):
	utn = ut + noise* ( randn(n) + 1j * randn(n) )
	ave = ave + utn
	ave2 = abs(fftshift(ave))/j
	pl2.set_ydata(ave2)
	draw()
	time.sleep(0.10)
'''

plot(ks, abs(fftshift(utn)), 'c')
show()

