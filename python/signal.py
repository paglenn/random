import numpy as np
from numpy.fft import fft, ifft, fftshift
from pylab import *
from math import *
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import axes3d, Axes3D
T = 60
n  =512

t = np.linspace(-T/2,T/2,n+1)[0:n]
r = range(0, n/2) + range(-n/2,0)
k = (2*pi/T) * np.array(r)
ks = fftshift(k)

Slice = np.arange(0,10,0.5)
T , S = np.meshgrid(t, Slice)

K , S = meshgrid(k, Slice)

sech = lambda x:  1/np.cosh(x)

U = sech(T - 10*np.sin(S)) #* np.exp(1j*0*T)

fig = figure()
font = { 'family': 'normal', 'weight':'bold', 'size':14}
rc('font', **font)

ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(211, projection='3d')
for i in range(np.size(U[:,1])):
	ax.plot_wireframe(T[i],S[i],U[i],color='k')
UT = np.zeros(np.shape(U))
ax.set_zlim(0,5)
#ax.view_init(-15,70)

''
for j in range(np.size(Slice)):
	UT[j,:] = abs(fftshift(fft(U[j,:])))
ax2 = fig.add_subplot(212,projection='3d')
for i in range(np.size(U[:,1])):
	ax2.plot_wireframe(fftshift(K[i]), S[i] , UT[i] , color  = 'b')
ax2.set_zlim(0,50)
#ax2.view_init(15, -70)
''
show()
