# Use Euler-Maruyama to generate realizations of Brownian Bridge
# stochastic differential equations
#
# Euler-Maruyama method for Stochastic Differential Equation 
#          dy(t)=f(t,y)dt+g(t,y)dB
# Input: functions f and g, initial y0, arrays t and B
#   t contains times t[i], i=0 to n at which solution desired
#   B contains B[i], i=0 to n basic Brownian motion at these times
# Output: array w with approximate solution w[i], i=0 to n
from numpy import *
import numpy as np
from random import *

def eulermaruyama(f,g,y0,t,B):
    n = shape(t)[0]-1; w = empty([n+1]); w[0] = y0
    for i in range(n):
        Deltati=t[i+1]-t[i];  DeltaBi = B[i+1]-B[i]
        w[i+1]=w[i]+f(t[i],w[i])*Deltati+g(t[i],w[i])*DeltaBi
    return w

# basic Brownian motion
# Input: array t with times t[i], i=0 to n
# array z with values z[i], i=0 to n-1 of 
# normally distributed (mu=0,sigma=1) random variables
# Output: array B with values B[i] of basic Browning motion

def basic_brownian(t,z):
    n = shape(t)[0]-1; B = empty([n+1]); B[0]=0.
    for i in range(n):
        DeltaBi = sqrt(t[i+1]-t[i])*z[i]
        B[i+1]=B[i]+DeltaBi
    return B

# Brownian bridge equation dy = (y1-y)/(t1-t) dt + dB
#                 is of form dy = f(t,y) dt + g(t,y) dB
def f(t=None, y=None):
    t1=3.; y1=2.
    return (y1-y)/(t1-t)

def g(t,y):
    return 1.

#
a=1.; b=3.; y0=1.                       # problem parameters
N=1000                                  # N large is number of subintervals for basic Brownian motion
t=linspace(a,b,N+1,endpoint=True);      # mesh both for basic Brownian motion and for E-M method approx.
nrealizations=4
w=empty([nrealizations,N+1]); B=empty([nrealizations,N+1])
colors=array(['r','g','b','k'])
for i in range(nrealizations):
   z=np.random.randn(N)                   # choice of random variables zz
   B[i,:]=basic_brownian(t,z)                  # determines basic Brownian
   w[i,:]=eulermaruyama(f,g,y0,t,B[i,:])       # Euler-Maruyama approximate solution at these times
   
import matplotlib.pyplot as plt
for i in range(nrealizations):
   plt.plot(t,B[i,:],colors[i]+'-',lw=0.5) # lw specifies line width, 1.0 is default
   plt.plot(t,w[i,:],colors[i]+'-',lw=1.5) 
plt.xlabel('t')
plt.title('Figure 9.16'+("%2d" % nrealizations)+' solutions (bold) to the Brownian bridge equation')
plt.savefig('eulermaruyama_brownianbridge.png')
plt.show()
