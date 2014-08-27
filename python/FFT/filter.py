from numpy.fft import fft, ifft, fftshift
from pylab import plot, show, subplot
import numpy as np
from math import *
T = 30
n = 512

t = np.linspace(-T/2,T/2,n+1)[0:n]
r = range(0,n/2) + range(-n/2,0)
k = (2*pi/T) * np.array(r)
ks  =fftshift(k)

sech = lambda t: 1/np.cosh(t)
u = sech(t)
ut = fft(u)

from numpy.random import randn
noise= 20
utn = ut + noise*(randn(n)+1j*randn(n))
un = ifft(utn)

# Gaussian filter
gfilter = np.exp(-(k)**2 / 10)
utnf = utn*gfilter
unf = ifft(utnf)

from pylab import xlim, ylim, xlabel, ylabel
#subplot(211)
#plot(t,u)

subplot(211)
xlabel('t'); ylabel('Correlation')
#plot(t, u, 'k', t, abs(un), 'm')
plot(t, abs(unf), 'g')
plot(t,0.5*np.ones(np.shape(t)),'k:')
#if max(abs(unf)) > 0.5: print 'Fire!'
#plot(t, abs(un)/max(abs(un)), 'm')
subplot(212)
xlabel('k') ; ylabel('Amplitude')
#plot(ks,abs(fftshift(ut)/max(abs(fftshift(ut)))),\
#		ks, abs(fftshift(utn)/max(abs(fftshift(ut)))),'m')
plot(ks, abs(fftshift(utn))/max(abs(fftshift(utn))), 'm')
plot(ks, fftshift(gfilter), 'b')
plot(ks, abs(fftshift(utnf))/max(abs(fftshift(utnf))), 'g')
xlim((-25,25))
ylim((0,1))
show()

