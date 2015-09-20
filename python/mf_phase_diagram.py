import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import bisect
import math

NP = 100

def f(m,T):
    beta = 1./T
    K = 0.0 * math.log(4) * T
    num = 2*math.tanh(beta*m )
    den = 2. + math.exp(beta * K) / math.cosh(beta*m)

    return num/den - m

def f2(m,T ):

     beta = 1./T
     num = math.tanh(beta*m )
     return num -m

T = np.linspace(0.05,1.1,200)
M = []
for t in T :
    try:
        root = bisect(f2,0.0001,1.0,args=(t,))
    except:
        root = fsolve(f, 20, args = (t,), factor=0.1)
    M.append(root)
    print t, root, f(root, t)

plt.plot(T,M)
plt.show()



