#Module imports
import numpy as np
import matplotlib.pyplot as pp
import math as m
# User-def'd imports and global vars
global L, numParticles, lattice

#Initialize coffee cup lattice
latticeSize = L = 50
numParticles = 100 # REQ: numParticles << L^2
lattice = np.zeros((L,L))
lattice[20:30,20:30] = 1
#lattice[49,:] = 1

Nsteps = int(2e4)
N = dict()
N[0] = numParticles
for step in xrange(1,Nsteps+1):

	X,Y = np.where(lattice == 1)
	EX = EY = 0
	# loop over points
	for (i,j) in zip(X,Y):
		seed = np.random.rand(2)
		# first unrestricted conditions
		dx = -1 if seed[0] < 0.5 else +1
		dy = -1 if seed[1] < 0.5 else +1

		# check for occupancy of neighbor site -- PBC's
		if lattice[(i+dx)%L,(j+dy)%L] == 0:
			lattice[(i+dx)%L,(j+dy)%L] += 1.
			lattice[i,j] = 0.

	lattice[20:30,L-1] = 0.
	N[step] = np.where(lattice == 1)[0].shape[0]

pp.plot(N.keys(),N.values(),'k.')

from scipy.optimize import curve_fit
def FF(t,T):
	return 100*np.exp(-t/float(T))
tau,idk = curve_fit(FF, N.keys(),N.values(),p0=1300)
pp.plot(N.keys(),[ FF(key,tau) for key in N.keys() ] , 'b')
pp.text(Nsteps/2., 60, 'T = %s'%tau)
pp.show()















