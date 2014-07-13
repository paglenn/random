import numpy as np
import pylab as pl
from sys import argv
import matplotlib.cm as cm
import math

if len(argv) == 1: N = int (raw_input("input # steps: ") )
else: N = int( argv[1] )
num_trials = 100
S = []
for i in range(num_trials):
	[x,y] = [0,0]
	X = []
	Y = []
	for i in range(N):
		if np.random.rand() >= 0.5:
			x += 1
		else:
			x -= 1

		if np.random.rand() <= 0.5:
			y += 1
		else:
			y -= 1

		X.append(x)
		Y.append(y)

	X = np.array(X)
	Y = np.array(Y)
	#print "Final position: ", (x,y)
	#print "Distance from origin:" , math.sqrt(x**2+ y**2)
	pl.quiver(X[:-1],Y[:-1], X[1:]-X[:-1], Y[1:]-Y[:-1],scale_units='xy',angles='xy',scale=1,color=cm.hot(1./i,1))
	pl.plot(X[-1],Y[-1],'bo')
	S.append(math.sqrt(x**2+y**2))

print "average distance: ", 1.*sum(S)/num_trials
print "predicted: ", math.sqrt(N)

pl.title(' Phase space of a 2D random walk')
pl.xlabel('x')
pl.show()
#Calculate statistics
if 0: #num_trials > 1:
	pl.hist(S,100)
	pl.show()
