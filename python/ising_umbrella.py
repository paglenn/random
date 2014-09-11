# ising_metropolis.py
# implementation of pseudocode from Schroeder, 2000
# perform umbrella sampling to draw free energy landscape
# Paul Glenn

import numpy as np
from numpy.random import sample
from sys import argv
if len(argv) < 2:
	print("Usage: ./a.out [temp]")
	quit()
T  = float(argv[1])
size = 20 #chain length of lattice

def deltaU(i,j,s):
	size = s.shape[0]
	# Toroidal boundary conditions
	top = s[size-1,j] if i is 0 else s[i-1,j]

	bottom = s[0,j] if i+1 is  size else s[i+1,j]

	left = s[i,size-1] if j is 0 else s[i-1,j]

	right = s[0,j] if j+1 is size else s[i,j+1]

	diff = 2* s[i,j] *(top+bottom+left+right)

	return diff


#initialize window
N = size**2
num_bins = 100
w=  N/float(num_bins) # 10 intervals -> 20 simulations
bins= [w + i*w for i in range(num_bins) ]
freq = [1. for x in range(num_bins) ]
passes = 10
MC_cycles = int(1e5)
s = np.random.choice([-1,1],(size,size))

def init_magnetization(s,M):

	while np.sum(s) > M:
		i = int(sample()*size)
		j = int(sample()*size)
		if s[i,j] == 1 : s[i,j] = -1

	while np.sum(s) < M:
		i = int(sample()*size)
		j = int(sample()*size)
		if s[i,j] == -1 : s[i,j] *= -1

s = np.random.choice([-1,1],(size,size))
for itr1 in range(passes):

	init_magnetization(s,N*itr1/float(passes))

	for itr2 in range(0,MC_cycles):
		i = int(sample()*size)
		j = int(sample()*size)
		delta_E = deltaU(i,j,s)

		if delta_E <= 0:
			# If flipping decreeases the energy, do it!
			s[i,j] *= -1

		# Compare to Boltzmann factor
		else:
			from math import exp
			if sample() < exp(-delta_E/T):
				s[i,j] *= -1

		# Magnetization at the end of each step
		M = np.sum(s)

		k = 0
		while abs(M) > bins[k] : k+=1
		freq[k] += 1

# end loop over windows

# denote relative frequency by P
P = [float(x)/max(freq) for x in freq]
from math import log
logP = [log(x) for x in P]
A = [-x*float(T) for x in logP]

import pylab as pl
#for bin in bins: pl.axvline(bin, color='k', linestyle='solid')
bins[1:num_bins] = [0.5*(bins[i] + bins[i-1]) for i in range(1,num_bins) ]
bins[0] /= 2.
pl.plot(bins,A)
pl.xlabel(r'M/$\mu$')
pl.ylabel('A(T)')
pl.title('T = %.2f'%(T))
pl.show()
#pl.savefig('umbrella.png')

