import math
import numpy as np

# the distribution
def P(x) :
    ans = 1./math.sqrt(2*math.pi)  * np.exp( -x * x / 2. )
    return ans

import random
numPoints = int(1e6)
U = np.random.rand(numPoints)

X = []
for itr in range(numPoints):
    u = U[itr]
    x = 10* (  np.random.rand() - 1./2)
    #print u
    #print x
    #print P(x)
    if u < P(x) :
        X.append(x)


#quit()
import matplotlib.pyplot as plt
plt.hist(X,50, normed = 1 )

xref = np.linspace(-5,5,100)
Pref = P(xref)
plt.plot(xref,Pref,'r')
plt.show()


