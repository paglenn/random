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
		visited_sites = [(0,0) for i in range(Nsteps) ]

		for step in range(1,Nsteps):
			directions = [(0,1),(0,-1),(1,0),(-1,0)]
			random_dir = random.choice(directions)
			x = X[step-1] + random_dir[0]
			y = Y[step-1] + random_dir[1]
			if (x,y) in visited_sites:
				goodPath = 0
				break
			else:
				X[step] = x
				Y[step] = y
				visited_sites[step] = (x,y)
				goodPath = 1

	return visited_sites

import time
start_time = time.time()
for i in range(10000):J =  SAW(10)
print("{0:e}".format(time.time()-start_time) )

