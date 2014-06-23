# ising_metropolis.py
# implementation of pseudocode from Schroeder, 2000
# Paul Glenn

import numpy as np
from numpy.random import sample
from sys import argv
assert len(argv) != 1
T  = float(argv[1])
size = 20 #chain length of lattice

def deltaU(i,j,s):
	size = s.shape[0]
	# Toroidal boundary conditions
	top = s[size-1,j] if i is 0 else s[i-1,j]

	bottom = s[0,j] if i+1 is  size else s[i+1,j]

	left = s[i,size-1] if j is 0 else s[i-1,j]

	right = s[0,j] if j+1 is size else s[i,j+1]

	Ediff = 2* s[i,j] *(top+bottom+left+right)

	return Ediff

import matplotlib.pyplot as plt
def colorSpins(s,title,T):
	image = np.array(s)
	size = s.shape[0]
	nrows, ncols = size,size

	#row_labels = range(nrows)
	#col_labels = range(ncols)
	import matplotlib.cm as cm
	fig = plt.matshow(image, cmap=cm.gray)
	#plt.xticks(range(ncols), col_labels)
	#plt.yticks(range(nrows), row_labels)
	plt.grid(b=True, which='both')
	plt.title(title)
	plt.savefig('lattice_%.2f.png'%(T))

s = np.random.choice([-1,1],(size,size))
'''
def initialize():
	s = np.empty((size, size))
	for i in range(size):
		for j in range(size):
			s[i,j] = 1 if sample() < 0.5 else -1
	#colorSpins(s, 'Initial')
	return s
'''
# Begin
#s = initialize()
for itr in xrange(0, 10000* size**2):
	i = int(sample()*size)
	j = int(sample()*size)
	Ediff = deltaU(i,j,s)

	if Ediff <= 0:
		# If flipping decreeases the energy, do it!
		s[i,j] *= -1
		#colorSpins(s,'itr = %s'%(itr))

	else:
		# Compare to Boltzmann factor
		from math import exp
		if sample() < exp(-Ediff/T):
			s[i,j] *= -1
			#colorSpins(s,'itr = %s'%(itr))
# end loop

# colorSpins final spin matrix:
M = np.sum(s) # Magnetization
colorSpins(s, 'T = %.2f, M = %i'%(T,M) ,T)
#print M