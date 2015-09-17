# Metropolis algorithm for 2D Ising model
# Author: Paul Glenn
import numpy as np
import random
from parameters import *
import math

magFile = open(mag_file,'w')
energyFile = open(energy_file,'w')

def getE(s) :
    E = 0.
    for i in range(L):
        for j in range(L):
            E -= s[i,j]*sum(s[x] for x in nbr[(i,j)] )

    if h != 0: E -= h * np.sum(s)

    return E

def trial_move(S) :
    acc = 0.
    i = int(random.random()*L)
    j = int(random.random()*L)
    deltaE = 2.*S[i,j]*sum(S[x] for x in nbr[(i,j)] )
    deltaE += 2*h*S[i,j]

    # Acceptance criterion
    acc = 0.
    if deltaE <= 0:
        acc = 1.
    else:
        weight = math.exp(  -beta * deltaE )
        acc = int( random.uniform(0.0,1.0) <= weight)

    S[i,j] *= -1*acc # flip spin

    return acc



m_int  = 0.
e_int  = 0.
e2_int = 0.
num_acc = 0.
S = np.random.choice([-1,1],(L,L))

for step in range(numSteps):
    accepted = trial_move(S)
    num_acc += accepted # keep track of # accepted moves

    # write magnetization
    if step > eqTime and step%sampleRate == 0:
        m_int += np.sum(S) / float(N)
        e_int += getE(S) / float(N)
        e2_int += getE(S)**2. / float(N)

pct_acc = num_acc / numSteps
numSamples = ( numSteps - eqTime) // sampleRate ;
m_avg = abs(m_int) / numSamples
e_avg = e_int  / numSamples
e2_avg = e2_int / numSamples

