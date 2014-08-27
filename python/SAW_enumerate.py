# 2d self-avoiding random walk
#high rejection rate --> VERY SLOW...
# exhaustive --> SLOW * SLOW...
import numpy as np
import matplotlib.pyplot as pp
import random

def SAW ( numSteps):
	goodPath = 0

	while goodPath == 0:
		X = [0 for i in range(numSteps) ]
		Y = [0 for i in range(numSteps) ]
		visited_sites = [(0,0) for i in range(numSteps) ]

		for step in range(1,numSteps):
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

def SAW_enumerate(numSteps) :
	goodPath = 0
	siteMarker = np.zeros((numSteps,numSteps))

	directions = [(0,1),(0,-1),(1,0),(-1,0)]

	while(directions)


SAW_enumerate(5)








