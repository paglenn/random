import numpy as np
import pylab as pl
from sys import argv
import matplotlib.cm as cm

if len(argv) == 1: N = int (input("input # steps: ") )
else: N = int( argv[1] )

x = 0
X = []
Y = [0]*N
p_R = 0.6
p_L = 0.4
for i in range(N):
	if np.random.rand() >= p_L:
		x += 1
	else:
		x -= 1
	X.append(x)

X = np.array(X)
Y = np.array(Y)
print("Final position:", x)
pl.quiver(X[:-1],Y[:-1], X[1:]-X[:-1], Y[1:]-Y[:-1],scale_units='xy',angles='xy',scale=1,color=cm.hot(0.5,1))
pl.plot(X[-1],Y[-1],'bo')
pl.title(' Phase space of a 1D random walk')
pl.xlabel('x')
pl.show()
#Calculate statistics
