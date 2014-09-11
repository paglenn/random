# Metropolis algorithm for 2D Ising model
# implementation of pseudocode from Schroeder, 2000
# Paul Glenn

import numpy as np
from numpy.random import sample
from parameters import *

nbr = dict()
for i in range(L):
    for j in range(L):
        nbr[(i,j)] = (((i+1)%L,j),((i-1)%L,j),(i,(j+1)%L),(i,(j-1)%L))
magFile = open(magFile,'w')
def init_magnetization(S,window):

    w = window[1] - window[0]
    target = 0.5*sum(window) + w/2. * np.random.uniform(-1,1)
    while np.sum(S) > target+1:
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == 1 : S[i,j] = -1

    while np.sum(S) < target-1:
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == -1 : S[i,j] *= -1

    return S

S = np.random.choice([-1,1],(L,L))
for w in windows:

    for itr in range(npasses):
        S = init_magnetization(S,w )
        for itr2 in range(nsteps):
            i = int(sample()*L)
            j = int(sample()*L)
            delta_E = 2 * sum(S[i,j]*S[x] for x in nbr[(i,j)] )

            if delta_E <= 0:
                # If flipping decreeases the energy, do it!
                S[i,j] = -S[i,j]

            else:
                # Compare to Boltzmann factor
                if sample() < np.exp(-delta_E/T):
                    S[i,j] = -S[i,j]

            # Magnetization at the end of each step
            M = np.sum(S)
            if M < w[0] or M > w[1] :
                S[i,j] *= -1
            else:
                magFile.write('{0}\n'.format(M))

magFile.close()
