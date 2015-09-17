import math
L = 20
T = 1.0
h = 0.
beta = 1./float(T)
N = L * L

numSweeps  = int(1e4)
numSteps = N * numSweeps
eqTime = 100*N
sampleRate = N

mag_file = 'mag_%s.dat'%T
energy_file = 'energy_%s.dat'%T
progress_file = 'progress'

# definition of nearest neighbors
nbr = dict()
for i in range(L):
    for j in range(L):
        # periodic BCs
        nbr[(i,j)] = (((i+1)%L,j),((i-1)%L,j),(i,(j+1)%L),(i,(j-1)%L))

