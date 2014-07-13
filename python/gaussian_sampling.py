#sample from Gaussian, mean 0 variance 1
import random
import math
x0 = 0.
x_cut = 4.
dx = 0.5
sigma = 1
G = lambda x: math.exp(-0.5 * x**2.)/math.sqrt(2*math.pi)
rand = random.uniform
Nsteps = int(1e6)
numList = list()
x = x0
'''
##############################
# Metropolis sampling
def Metropolis_step(old, new, PDF):
	if abs(new) > abs(x_cut) : return old

	if rand(0.,1.) < PDF(new)/PDF(old):
		return new
	else:
		return old

for step in range(Nsteps):
	x_new = x + rand(-dx , dx)
	x = Metropolis_step(x,x_new,G)
	numList.append(x)

import numpy as np
result = np.histogram(numList,bins=40,density=True)
Y,X = result
X = [0.5 * (X[i-1]+X[i]) for i in range(1,X.size) ]
from pylab import plot, show
import pylab as pl

plot(X,Y)
pl.hlines(1./math.sqrt(2.*math.pi),-2,2)
pl.ylim(0,0.45)
show()
'''


########################################
# Direct sampling algorithm
G_max = 1./math.sqrt(2*math.pi)
X = list()
Y = list()
n_data = 1000
n_accept = 0
while n_accept < n_data:
	x = rand(-x_cut,x_cut)
	y = rand(0,G_max)
	if y <= G(x):
		X.append(x)
		Y.append(y)
		n_accept += 1

from pylab import plot, show
plot(X,Y,'k.')
import numpy as np
Xref = np.linspace(-x_cut,x_cut,1000)
Yref = [G(x) for x in Xref ]
plot(Xref,Yref,'b',lw=3)
show()



