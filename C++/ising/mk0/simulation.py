# Metropolis algorithm for 2D Ising model
# implementation of pseudocode from Schroeder, 2000
# Author: Paul Glenn
# modified for umbrella sampling
import numpy as np
from numpy.random import sample
from parameters import *
import os

progressFile = open(progressFile,'w')
windowFiles = dict(enumerate(open(window_files[i],'w') for i in range(num_windows)))
#magFile = open(magFile,'w')

def adjust_magnetization(S,wi):
    window = windows[wi]
    w = window[1] - window[0]

    target = minima[wi]  #+ 0.5 * w * np.random.rand()
    tol = 0.
    while np.sum(S) > target + tol :
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == 1 : S[i,j] = -1

    while np.sum(S) < target -tol :
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == -1 : S[i,j] = 1

num_acc = 0
def getE(s) :
    E = 0.
    for i in range(L):
        for j in range(L):
            E -= 0.5*s[i,j]*sum(s[x] for x in nbr[(i,j)] )
            E -= h * s[i,j]
    return beta*E

for wi in range(num_windows):
    w = windows[wi]
    wmin = minima[wi]
    S = np.random.choice([-1,1],(L,L))

    for itr in range(npasses):
        adjust_magnetization(S,wi )
        #windowFiles[wi].write('{0:f}\t{1:f}\n'.format(0,np.sum(S)))
        for itr2 in range(nsteps):

            # choose a random spin to flip
            i = int(sample()*L)
            j = int(sample()*L)
            delta_E = 2. * S[i,j]*sum(S[x] for x in nbr[(i,j)] )
            delta_E += 2*h*S[i,j]

            #print delta_E

            # flip spin just to calculate delta V
            M0 = int(np.sum(S))
            S[i,j] = - S[i,j]
            M1 = int(np.sum(S))
            S[i,j] = - S[i,j]
            deltaV = V[wi,M1+N] - V[wi,M0+N]
            delta_E += deltaV
            #print delta_E -dE0

            # Acceptance criterion
            acc = 0
            if delta_E <= 0: acc = 1
            elif np.random.uniform(0,1) <= np.exp(-beta*delta_E):
                acc = 1
            if acc: S[i,j] *= -1
            num_acc += acc

            # Magnetization at the end of each step
            if itr2%sampleRate == 0 and itr2 > deadTime:
                M = [ np.sum(S) , wi ]
                '''
                magFile.write('{} {}'.format(*M))
                Ei = getE(S)
                for n in range(num_windows):
                    Vwi = V[n,int(M[0]+N)]
                    magFile.write(' {}'.format(beta*(Ei + Vwi)))

                magFile.write('\n')
                '''
                windowFiles[wi].write('{0:.1f}\t{1:.1f}\n'.format(itr2,M[0]))

        progressVars = [wi+1,num_windows,itr+1,npasses,nsteps]
        progressFile.write('window\t{0}/{1}\tpass\t{2}/{3}\trun\t{4}\n'.format(*progressVars))


# Write summary data and close
metaFile = open('metadata.dat','w')
#metaFile.write('#window_file\tz_min\tk\n')
for j in range(num_windows):
    if not os.path.isfile(window_files[j]): exit('Something went wrong')
    data = [os.path.abspath(window_files[j]),minima[j],k[j] ]
    metaFile.write('{0}\t{1}\t{2}\n'.format(*data))
metaFile.close()
for key in windowFiles: windowFiles[key].close()
progressFile.write('finished!! {:%} steps accepted \n'.format(num_acc/float(numFrames)))
progressFile.close()
