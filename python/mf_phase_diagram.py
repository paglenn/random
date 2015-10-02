import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import bisect
import math

NP = 100

def f(m,T):
    beta = 1./T
    K = 2.0 * math.log(4) * T
    num = 2*np.tanh(beta*m )
    den = 2. + math.exp(beta * K) / np.cosh(beta*m)

    return num/den - m

'''
def f2(m,T ):

     beta = 1./T
     num = math.tanh(beta*m )
     return num -m

T = np.linspace(0.05,0.7,200)

M = []
for t in T :
    try:
        root = bisect(f,0.001,1.0,args=(t,))
    except:
        root = fsolve(f, 20, args = (t,), factor=0.1)
    M.append(root)
    print t, root, f(root, t)

plt.plot(T,M)
plt.show()
'''

M = np.linspace(-1.0,1.0,4000)
mmf = f(M, 0.5)
print mmf
print np.where(np.abs(mmf) < 1e-4)
plt.plot(M,M)
plt.plot(M,mmf+M)
plt.show()
