import math
L = 20
T = 5.0
h = 0.
B = 1./float(T)
N = L * L

numSweeps  = int(1e4)
numSteps = N * numSweeps
eqTime = 100*N
sampleRate = N
tol = 4

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
num_windows = 1
k = dict()
K = 0.
for j in range(num_windows):
    if j < num_windows/3.: k[j] = K
    elif j > 2*num_windows/3.: k[j] = K
    else: k[j] = K

num_bins = 100
windows = []
minima = []
for x in range(num_windows):
    windows.append([N*(- 1 + 2.*x/num_windows),N*(-1. + 2.*(x+1)/num_windows) ] )
    minima.append(0.5*sum(windows[-1]))

numFrames = numSteps * num_windows
window_files = dict(enumerate('window_%i'%i for i in range(num_windows)))

import numpy as np
V = np.empty((num_windows,N+1))
for wi in range(num_windows):
    for M in range(-N,N+1,2):
        V[wi,M] = 0.5*k[wi]*((M - minima[wi])/float(N))**2.

