# 2d random walk
import random


def random_step():
	directions = [(0,1),(0,-1),(1,0),(-1,0)]
	random_dir = random.choice(directions)
	return random_dir


def random_walk(Nsteps):
	X = dict() ; X[0] = 0
	Y = dict() ; Y[0] = 0

	for step in range(1,Nsteps):
		directions = [(0,1),(0,-1),(1,0),(-1,0)]
		random_dir = random.choice(directions)
		x = X[step-1] + random_dir[0]
		y = Y[step-1] + random_dir[1]
		X[step] = x
		Y[step] = y

	return X,Y







