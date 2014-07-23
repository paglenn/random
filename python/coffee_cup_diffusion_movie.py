# Paul Glenn -- 14 July 2014
# a simple diffusion simulation - with graphics.
# usage: python coffee_cup_diffusion_movie.py

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
#lattice[49,:] = 1

def plot(setting,t = 0):
	global latticePlot
	global text
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
		ax.set_xlabel('x+50')
		ax.set_ylabel('y+50')
		text = pp.text(1,1,'t = %s'%t)
		pp.ion()
		latticePlot, = pp.plot(X,Y,marker='.',ls='',color='k')

	elif setting == 'update':
		latticePlot.set_xdata(X)
		latticePlot.set_ydata(Y)
		text.remove()
		text = pp.text(1,1,'t = %s'%t)
		pp.draw()
		pp.pause(0.001)

Nsteps = int(1e4)
plot('init')
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


	if step%100 == 0:
		plot('update',step)













