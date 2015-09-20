import math
L = 20
T = 1.0
h = 0.
beta = 1./float(T)
numSweeps = 5e3
nsteps =  int ( L*L * numSweeps )
sampleRate = L*L
deadTime = 100.
npasses = 1
N = L * L
magFile = 'magnetization.dat'
energyFile = 'energy.dat'
progressFile = 'progress'

# definition of nearest neighbors
nbr = dict()
for i in range(L):
    for j in range(L):
        # periodic BCs
        nbr[(i,j)] = (((i+1)%L,j),((i-1)%L,j),(i,(j+1)%L),(i,(j-1)%L))

#umbrella sampling specific
num_windows = 40
K = 5000
k = [K for j in range(num_windows) ]

#for j in range(4) + range(7,num_windows): k[j] = 20./N**1.5
num_bins = 100
windows = []
minima = []
for x in range(num_windows):
    windows.append([N*(- 1 + 2.*x/num_windows),N*(-1. + 2.*(x+1)/num_windows) ] )
    #overlap = 0.3*(windows[-1][1] - windows[-1][0])
    ##windows[-1][1] += overlap
    minima.append(0.5*sum(windows[-1]))
#windows[-1][1] -= overlap
#minima[-1] = 0.5*sum(windows[-1])
numFrames = nsteps * num_windows * npasses
window_edges = [w[1] for w in windows]
window_files = dict(enumerate('window_%i'%i for i in range(num_windows)))

import numpy as np
V = np.zeros((num_windows,2*N+1))
for wi in range(num_windows):
    for M in range(0,2*N+1,2):
        V[wi,M] = 0.5*k[wi]*((M - minima[wi] - N)/float(N))**2.

#print minima
#print [V[wi,minima[wi]+N] for wi in range(num_windows) ]
