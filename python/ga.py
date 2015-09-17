import math
from itertools import product
import random
nbits = 3
initPopSize = 3;
stateSpace = [range(2) for x in range(nbits) ]
X = [list(x) for x in product(*stateSpace) ]
Y = [random.choice(X) for i in range(initPopSize) ]
Y = random.sample(X,initPopSize)

D = lambda s: sum(2**j * s[j] for j in range(nbits) )
f = lambda k: -k*k + 8*k + 15.

def FF(y):
    s = 0. # sum
    for x in X: s += f(D(x))
    return f(D(y))/s
'''
import matplotlib.pyplot as plt
plt.plot([D(x) for x in X],[FF(x) for x in X  ],'.')
plt.show()
quit()
'''
def crossover(yi,yj):
    pos = random.randint(0,nbits-1)
    old_yip = yi[pos]
    yi[pos] = yj[pos]
    yj[pos] = old_yip
    return yi,yj

def mutate(y):
    pos = random.randint(0,nbits-1)
    y[pos] = 1 - y[pos]
    return y

for gen in range(1000):
    fitness = [FF(y) for y in Y ]
    top = fitness.index(max(fitness))
    others = list(fitness); others.pop(top)
    second = fitness.index(max(others))
    victim = random.choice([top,second])
    last = fitness.index(min(fitness))

    p_mut = 0.001;
    p_cross = 0.2;
    if random.random() < p_mut: Y[victim] = mutate(Y[victim])
    elif random.random() < p_cross: Y[top],Y[second] = crossover(Y[top],Y[second])

    #Y.pop(last)
    #print Y
    postFitness = [FF(y) for y in Y ]
    top = postFitness.index(max(postFitness))
    Y = Y + [Y[top]]

print Y

