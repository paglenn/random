# Paul Glenn -- 18 July 2014
# usage: python cluster_DLA.py [num steps]
# Create a diffusion-limited aggregation cluster.

#module imports
import numpy as np
import matplotlib.pyplot as pp
from random_walk_2D import random_step
import math as m
from sys import argv
#user defined imports
global points
argc = len(argv)
if argc > 1: Nsteps = int(argv[1])

# Parameters
a = 0.5 # lattice constant
latticeSize = L = 161
axlim = a*L/2
axis = range(-L/2,L/2+1)
seed = (0,0)
if argc == 1: Nsteps = 1000
offset = 3
r_min = 3*a
r_max = 2*r_min

# setup
points = [seed]
#for i,j in it.product(axis,axis ) :
#	lattice[(i,j)] = 0

def clusterDistances(x,y):
	global points
	distances = []
	for point in points:
		distance = abs(x-point[0]) + abs(point[1]-y)
		distances.append(distance)
	return distances

for t in range(1,Nsteps):
	(x,y) = seed
	effectiveRange = range(int(r_min), int(r_max)) + range(-int(r_max),int(r_min))
	while (x,y) in points: x,y = np.random.choice(effectiveRange,2)

	while abs(x) <= r_max and abs(y) <= r_max:
		dx,dy = random_step()

		x += a*dx
		y += a*dy

		if min(clusterDistances(x,y) ) == 1:
			points.append((x,y))
			r_min = max(clusterDistances(0,0)) + offset
			r_max = max([2*r_min, axlim])

			break

# plot final config
X = [p[0] for p in points ]
Y = [p[1] for p in points ]
pp.plot(X,Y,'k.')
pp.xlim(-axlim,axlim)
pp.ylim(-axlim,axlim)
pp.text(0.7*axlim, -0.8*axlim, 'N = %s'%len(X))
pp.savefig("cluster_DLA.png")


