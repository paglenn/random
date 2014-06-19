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

def f(t=None, y=None):
    r=0.1
    return r*y

def g(t,y):
    sigma = 0.3
    return sigma*y

# geometric Brownian motion evaluate exact solution of 
#         dy(t)=r y dt+ sigma y dB
# which is geometric Brownian motion.
# Input: parameters r and sigma,  initial value y0
#   array t with times t[i], i=0 to n
#   array B with values B[i], i=0 to n of basic Brownian motion
# Output: array y with values y[i], i=0 to n of geometric Brownian

def geometric_brownian(r,sigma,y0,t,B):
    n = shape(t)[0]-1; y = empty([n+1]); y[0]=y0
    for i in range(1,n+1): # note i=n is last
        y[i]=y0*exp((r-sigma**2/2)*t[i]+sigma*B[i])
    return y
#
a=0.; b=2.; y0=1.;  r=0.1;  sigma=0.3   # problem parameters
N=1000                                  # N large is number of subintervals for basic Brownian motion
tt=linspace(a,b,N+1,endpoint=True);     # finely spaced mesh for basic Brownian motion
zz=np.random.randn(N)                   # choice of random variables zz
BB=basic_brownian(tt,zz)                # determines basic Brownian motion
n=10                                    # subintervals for Milstein method approximation
t=empty(n+1); B=empty(n+1)              # set up arrays for Milstein
for i in range(n+1):                    # From the arrays tt and BB,
   t[i]=tt[100*i]                       # pick n+1 evenly spaced times t[i] and 
   B[i]=BB[100*i]                       # values B[i] of basic Brownian motion
w=eulermaruyama(f,g,y0,t,B)             # Euler-Maruyama approximate solution at these times

GB=geometric_brownian(r,sigma,y0,tt,BB) # GS is exact solution of the S.D.E., given basic Brownian

import matplotlib.pyplot as plt
plt.plot(tt,BB,'b-',lw=0.75) # lw specifies line width, 1.0 is default
plt.plot(t,w,'bo')
plt.plot(tt,GB,'b-')
plt.xlabel('t')
plt.title('Figure 9.12 Solution to the geometric Brownian motion S.D.E.')
plt.show()
