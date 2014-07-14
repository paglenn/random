# 2d self-avoiding random walk
#high rejection rate --> VERY SLOW...
import numpy as np
import matplotlib.pyplot as pp
import random

def SAW ( Nsteps):
	goodPath = 0

	while goodPath == 0:
		X = [0 for i in range(Nsteps) ]
		Y = [0 for i in range(Nsteps) ]
		Z = [0 for i in range(Nsteps) ]
		visited_sites = [(0,0,0) for i in range(Nsteps) ]

		for step in range(1,Nsteps):
			directions = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
			directions += [(0,1,0),(0,-1,0)]
			random_dir = random.choice(directions)
			x = X[step-1] + random_dir[0]
			y = Y[step-1] + random_dir[1]
			z = Z[step-1] + random_dir[2]
			if (x,y,z) in visited_sites:
				goodPath = 0
				break
			else:
				X[step] = x
				Y[step] = y
				Z[step] = z
				visited_sites[step] = (x,y,z)
				goodPath = 1

	return visited_sites

stepSequence = SAW(10)
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as pp
fig = pp.figure()
ax = Axes3D(fig)
X = [p[0] for p in stepSequence ]
Y = [p[1] for p in stepSequence ]
Z = [p[2] for p in stepSequence ]
pp.plot(X,Y,zs=Z)
pp.show()






