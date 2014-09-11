import random, math
from parameters import *
# cluster algorithm for ising model
# adding umbrella potential for sampling of free energy landscape


magFile = open(magFile,'w')
#energyFile = open(energyFile,'w')
def adjust(S,window):
    ''' adjust(S-array, desired magnetization) '''
    width = window[1] - window[0]
    mean = 0.5*sum(window)
    mag = sum(S)
    while abs(mag - mean) > width/4:
        k = random.randint(0,N-1)
        if mag > mean and S[k] == 1:
            S[k] = -S[k]
        elif mag < mean and S[k] == -1:
            S[k] = -S[k]
        mag = sum(S)
        #print(mag)
    return S

nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}

for window in windows:
    #print(window)

    S = [random.choice([1, -1]) for k in range(N)]
    S = adjust(S,window)
    #print('adjusted')

    for step in range(nsteps):
        reject = False
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
            if sum(S) > window[1] or sum(S) < window[0]:
                S[j] *= -1
                reject = True
        if not reject:
            magFile.write('{0}\n'.format(sum(S)))

magFile.close()



