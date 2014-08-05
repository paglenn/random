# Paul Glenn -- 21 July 2014
# Draw a Koch curve on the interval [x_lower,x_upper].
# Usage: python koch_fractal.py [num_iterations =  1] [x_lower = 0] [x_upper = 1]

# Module imports
import numpy as np
import matplotlib.pyplot as pp
import math as m
from sys import argv

argc = len(argv) -1
if argc == 0: numIterations = 1
else: numIterations = int(argv[1])

if argc == 3:
	x_lower = int(argv[2])
	x_upper = int(argv[3])
else:
	x_lower = 0
	x_upper = 1

xi = np.array([x_lower,0.])
xf = np.array([x_upper,0.])

# Recursive function
def KochIteration(xi,xf, level):
	cos = m.cos(m.pi/3)
	sin = m.sin(m.pi/3)
	xyRotation = np.array([[cos, -sin],[sin, cos]])
	if level == 0:
		X = np.linspace(xi[0],xf[0],2)
		Y = np.linspace(xi[1],xf[1],2)
		pp.plot(X,Y,'k')
	else:
		dx = 1./3 * (xf - xi)
		x = [ 0 for i in range(5) ]
		x[0] = xi
		x[1] = x[0] + dx
		x[2] = x[1] + np.dot(xyRotation,dx)
		x[3] = x[0] + 2*dx
		x[4] = xf
		for i in range(4):
			KochIteration(x[i],x[i+1], level - 1)


KochIteration(xi,xf, numIterations)
pp.text(0.6*pp.xlim()[1],0.9*pp.ylim()[1],'%i iterations'%numIterations)
pp.axis('equal')
#pp.show()
pp.savefig('koch_fractal.png')
