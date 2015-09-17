# Metropolis algorithm for 2D Ising model
# Author: Paul Glenn
import numpy as np
import random
from parameters import *
import math
sample = np.random.sample

magFile = open(magFile,'w')

def adjust_magnetization(S,window):

    w = window[1] - window[0]
    target = 0.5*sum(window) #+ 0.5 * w * np.random.rand()
    #if target > window[1] or target < window[0]: target = 0.5*sum(window)
    while np.sum(S) > target + tol :
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == 1 : S[i,j] = -1

    while np.sum(S) < target -tol :
        i = int(sample()*L)
        j = int(sample()*L)
        if S[i,j] == -1 : S[i,j] = 1

def getE(s) :
    E = 0.
    for i in range(L):
        for j in range(L):
            E -= s[i,j]*sum(s[x] for x in nbr[(i,j)] )

    if h != 0: E -= h * np.sum(s)

    return E

num_acc = 0
highTseq = np.linspace(5.,2.5,10)
lowTseq = np.linspace(2.0,0.1,10) # 2.269 is the critical temperature
midTseq = np.linspace(2.0,2.5,20)
TRANGE = np.hstack((highTseq,lowTseq))

M = []
E = []
E2 = []
#for T in TRANGE:
    S = np.random.choice([-1,1],(L,L))
    if T != 0.: beta  = 1./T
    else: beta  = np.inf
    #adjust_magnetization(S,w )
    #windowFiles[wi].write('{0:f}\t{1:f}\n'.format(0,np.sum(S)))
    m_int  = 0.
    e_int  = 0.
    e2_int = 0.
    for step in range(numSteps):
        i = int(sample()*L)
        j = int(sample()*L)
        deltaE = 2.*S[i,j]*sum(S[x] for x in nbr[(i,j)] )

        deltaE += 2*h*S[i,j]

        # Compare to Boltzmann factor
        weight = math.exp(  -beta * deltaE )
        if random.uniform(0.0,1.0) <= weight :
            S[i,j] *= -1 # flip spin
            num_acc += 1 # keep track of # accepted moves

        # write magnetization
        if step > eqTime and step%sampleRate == 0:
            m_int += np.sum(S) / float(N)
            e_int += getE(S) / float(N)
            e2_int += getE(S)**2. / float(N)

    m_avg = abs(m_int / (numSteps-eqTime) )
    e_avg = e_int  / (numSteps-eqTime)
    e2_avg = e2_int / (numSteps - eqTime)
    E.append(e_avg)
    E2.append(e2_avg)
    magFile.write('{:.4f}\t{:.3f}\t{:.3f}\n'.format(T,m_avg,e_avg))

# compute the specific heat
C = []
for i in range(len(TRANGE)-1):
    T = TRANGE[i]
    if T != 0.: Ch =  (E2[i] - E[i]**2.) / T**2.
    else: Ch = None
    C.append(Ch)

cFile = open('heat_capacity.dat','w')
for j in range(len(C)): cFile.write('%.2f\t%.2f\n'%(TRANGE[j],C[j]))
cFile.close()
magFile.close()




