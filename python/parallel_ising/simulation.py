# Metropolis algorithm for 2D Ising model
# implementation of pseudocode from Schroeder, 2000
# Paul Glenn
import numpy as np
from numpy.random import sample
from parameters import *
import os
from multiprocessing import Pool

#magFile = open(magFile,'w')
progressFile = open(progressFile,'w')
windowFiles = dict(enumerate(open(window_files[i],'w') for i in range(num_windows)))

def adjust_magnetization(S,window):

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
def go(wi):
    w = windows[wi]
    wmin = minima[wi]

    for itr in range(npasses):
        adjust_magnetization(S,w )
        windowFiles[wi].write('{0:f}\t{1:f}\n'.format(0,np.sum(S)))
        for itr2 in range(nsteps):
            i = int(sample()*L)
            j = int(sample()*L)
            delta_E = 2 * sum(S[i,j]*S[x] for x in nbr[(i,j)] )
            delta_E += 0.5*k*(np.sum(S) - wmin)**2.

            if delta_E <= 0:
                # If flipping decreeases the energy, do it!
                S[i,j] = -S[i,j]

            else:
                # Compare to Boltzmann factor
                if sample() < np.exp(-delta_E/T):
                    S[i,j] = -S[i,j]
            #progressVars = [wi+1,num_windows,itr+1,npasses,itr2+1,nsteps]
            #progressFile.write('window\t{0}/{1}\tpass\t{2}/{3}\trun\t{4}/{5}\n'.format(*progressVars))


            # Magnetization at the end of each step
            M = np.sum(S)
            #magFile.write('{0:.2f}\n'.format(M))
            windowFiles[wi].write('{0:.1f}\t{1:.1f}\n'.format(itr2,M))
if __name__ == '__main__':
    pool = Pool(processes=num_windows)
    pool.map(go,range(num_windows))

metaFile = open('metadata.dat','w')
metaFile.write('#window_file\tz_min\tk\n')
for j in range(num_windows):
    if not os.path.isfile(window_files[j]): exit('Something went wrong')
    data = [os.path.abspath(window_files[j]),minima[j],k ]
    metaFile.write('{0}\t{1}\t{2}\n'.format(*data))
metaFile.close()
#magFile.close()
for key in windowFiles: windowFiles[key].close()
progressFile.write('finished!!\n')
progressFile.close()
