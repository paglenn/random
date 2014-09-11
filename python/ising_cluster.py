# originally from computational statistical mechanics course on Coursera.
# but IT HAS BEEN ANALYZED AND UNDERSTOOD :)
# provides a great alternative to umbrella sampling for calculating the
# free energy curve.
import random, math

L = 20
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}
T = 2.20
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 10000
S = [random.choice([1, -1]) for k in range(N)]
M = [sum(S)]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    Pocket, Cluster = [k], [k]
    while Pocket != []:
        j = random.choice(Pocket)
        for l in nbr[j]:
            if S[l] == S[j] and l not in Cluster \
                   and random.uniform(0.0, 1.0) < p:
                Pocket.append(l)
                Cluster.append(l)
        Pocket.remove(j)
    for j in Cluster:
        S[j] *= -1
    M.append(sum(S))

import numpy as np
binContents,bins = np.histogram(M,bins=500,density=True)

A = []
M = []
for j in range(len(bins)-1):

    if binContents[j] != 0:

        M.append(bins[j])
        A.append(- math.log( binContents[j]) )

import matplotlib.pyplot as plt
plt.plot(M,A)
plt.show()


