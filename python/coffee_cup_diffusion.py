# Paul Glenn -- 14 July 2014
# a simple diffusion simulation.
# computes the diffusion constant.
# usage: python coffee_cup_diffusion.py


#Module imports
import numpy as np
import matplotlib.pyplot as pp
import math as m
# User-def'd imports and global vars
global L, numParticles, lattice

#Initialize coffee cup lattice
latticeSize = L = 100
numParticles = N = 100 # REQ: numParticles << L^2
lattice = np.zeros((L,L))
lattice[45:55,45:55] = 1

def plot(setting):
	global latticePlot
	X = list()
	Y = list()

	for i in range(lattice.shape[0]):
		for j in range(lattice.shape[1]):
			if lattice[i,j] == 1:
				X.append(i) ; Y.append(j)

	if setting == 'init':
		fig = pp.figure()
		ax = fig.gca()
		ax.set_xlim(0,100)
		ax.set_ylim(0,100)
		pp.ion()
		latticePlot, = pp.plot(X,Y,marker='.',ls='',color='k')

	elif setting == 'update':
		latticePlot.set_xdata(X)
		latticePlot.set_ydata(Y)
		pp.draw()
		pp.pause(0.0001)

Nsteps = int(1e4)
#plot('init')
R2 = dict()
D = dict()
for step in xrange(1,Nsteps+1):

	X,Y = np.where(lattice == 1)
	EX = EY = 0
	for (i,j) in zip(X,Y):
		seed = np.random.rand(2)
		# first unrestricted conditions
		dx = -1 if seed[0] < 0.5 else +1
		dy = -1 if seed[1] < 0.5 else +1

		# Calculate expectation values
		x = (i+dx)%L - 49
		y = (j+dy)%L - 49
		EX = EX + x**2. if lattice[(i+dx)%L,(j+dy)%L] == 0 else EX
		EY = EY + y**2. if lattice[(i+dx)%L,(j+dy)%L] == 0 else EY

		# check for occupancy of neighbor site -- PBC's
		if lattice[(i+dx)%L,(j+dy)%L] == 0:
			lattice[(i+dx)%L,(j+dy)%L] += 1.
			lattice[i,j] = 0.

	R2[step] = (EX + EY)/ float(N) # R2 = 4Dt
	D[step] = R2[step] / (4*step) if step != 0 else float('nan')

	#plot('update')

# plot diffusion coefficient and slope
pp.subplot(2,1,1)
pp.plot(D.keys(),D.values(),'.')
pp.ylabel('D')

dDdt = dict()
for step in xrange(2,Nsteps):
	dDdt[step] = D[step] - D[step-1]
pp.subplot(2,1,2)
pp.plot(dDdt.keys(), dDdt.values())
pp.ylabel('dD/dt')
pp.show()












