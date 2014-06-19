# Discrete Brownian motion
# Input: none
# Output: graph of a realization of discrete Brownian motion

from numpy import *
import numpy as np
from random import *


# discrete Brownian motion
# Input: array t with times t[i], i=0 to n
# array z with values z[i], i=0 to n-1 of 
# normally distributed (mu=0,sigma=1) random variables
# Output: array B with values B[i] of basic Browning motion

def discrete_brownian(t,z):
    n = shape(t)[0]-1; B = empty([n+1]); B[0]=0.
    for i in range(n):
        plus_minus = 1.
        if(z[i]<0.):
           plus_minus = -1.
        DeltaBi = sqrt(t[i+1]-t[i])*plus_minus
        B[i+1]=B[i]+DeltaBi
    return B
a=0.; b=10.;
import matplotlib.pyplot as plt
Nvalues = array([10,100,1000]); colors=array(['g','k','b'])
for icase in range(3):
   N = Nvalues[icase];  color = colors[icase];
# N is number of subintervals
   tt=linspace(a,b,N+1,endpoint=True);     # linearly space mesh
   zz=np.random.randn(N)                   # choice of random variables zz used in deciding
   DB=discrete_brownian(tt,zz)              # to step + or -
            # determines basic Brownian motion
   for i in range(N):
      plt.plot([tt[i],tt[i+1]],[DB[i],DB[i]],color+'-',lw=1.25) # lw specifies line width, 1.0 is default
      plt.plot([tt[i+1],tt[i+1]],[DB[i],DB[i+1]],color+'-')
plt.axes().set_aspect('equal', 'datalim')
plt.xlabel('t')
plt.title('Figure 9.10 Realizations of discrete Brownian motion')
plt.show()
