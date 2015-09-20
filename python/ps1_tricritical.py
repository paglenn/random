import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import bisect
import math

NP = 100
T = np.linspace(0.333 ,0.8, NP)
#Delta = np.linspace(0.1,5.,100)

def f(Delta,t) :
    Beta = 1./t
    delta = 2 + np.exp(Beta *Delta )

    A = 0.5 * (1 -  2*Beta / delta )
    B = -0.25 * Beta**3  / delta * ( delta / 6. - 1 )
    C = Beta **5. / (360* delta **3. ) * \
            (- delta *delta + 30 * delta -120 )
    return B* B - 4*A*C

Kmax = 2./3 * math.log(2)
T2 = np.linspace(0.05,0.333,NP)

def f2(K, T )  :
   return ( K/T -1) *math.exp(K/T) - 1

Del = np.zeros(NP)
i = 0
for t in T2 :
    x0 = 0.1
    root = fsolve(f2, x0, args = (t,), maxfev = 300 )
    print t, float(root)
    Del[i] = float( root)
    i += 1

plt.plot(T2,Del)
plt.show()






