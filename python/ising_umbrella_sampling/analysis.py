from parameters import *

magFile = open(magFile,'r')
Mag_Values = []
k = 0
for unformatted_line in magFile.readlines():
    formatted_line = unformatted_line[:-1]
    Mag_Values.append(float(formatted_line))

import numpy as np
binContents, bins = np.histogram(Mag_Values,bins=100,density=True)
bins = bins[:-1]
M = list()
A = list()
for i in range(len(bins)):
    if binContents[i] != 0:
        M.append(bins[i])
        A.append(- (1./T) * np.log(binContents[i]) )

import matplotlib.pyplot as plt
#plt.plot(M,A,'r.',label='original')
j = 0
delta = [0. for x in window_edges]
for i in range(len(M)):
    if M[i] > window_edges[j] :
        j += 1
        # remove edge effects
        A[i-1] = A[i-2]
        delta[j] = A[i] - A[i-1]

    A[i] -= delta[j]


m = [mu/N for mu in M ]
plt.plot(m,A,'b-',label='joined')
#diff_A = [A[i] - A[i-1] for i in range(1,len(A))]
#plt.plot(M[1:],diff_A,'g.',label='differences')
#plt.vlines(window_edges,min(A),max(A))
plt.ylabel(r'$z$')
plt.xlabel(r'F($z$)')
plt.title('T = {0}'.format(T))
plt.legend()
plt.show()

