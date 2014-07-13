# 2d random walk
import numpy as np
import matplotlib.pyplot as pp
import random

Nsteps = int(200)
goodPath = 0

X = [0. for i in range(Nsteps) ]
Y = [0. for i in range(Nsteps) ]

pp.plot( X[0],Y[0],'.')
for step in range(1,Nsteps):
	directions = [(0,1),(0,-1),(1,0),(-1,0)]
	#directions=  [(-1,1),(1,1),(1,-1),(-1,-1)]
	random_dir = random.choice(directions)
	x = X[step-1] + random_dir[0]
	y = Y[step-1] + random_dir[1]
	X[step] = x
	Y[step] = y



pp.plot(X,Y)
pp.show()




