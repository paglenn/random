# Program 8.1 Forward difference method for heat equation
# Input: space interval [xl,xr], time interval [yb,yt],
#        number of space steps M, number of time steps N
# Output: array w such that w[i-1,j] approximates solution at 
#                     (xl+i*(xr-xl)/M, yb+j*(yt-yb)/N) where 1 <= i <= M-1, 0 <= j <= N
# Example usage: w=heatfd(0.,1.,0.,1.,1,0,250)

import numpy as np
from numpy import *

def heatfd(xl=None, xr=None, yb=None, yt=None, M=None, N=None):
    c = 1.                                               # diffusion coefficient
    h = (xr-xl)/M; k = (yt-yb)/N; m = M-1; n = N
    sigma = c*k/(h*h)
    a = (1-2*sigma)*diag(ones(m),k=0) + sigma*diag(ones(m-1),k=-1) + sigma*diag(ones(m-1),k=+1)
    lside = l(linspace(yb,yt,N+1)); rside = r(linspace(yb,yt,N+1))
    w = empty([m,N+1])                                   # initialize array w 
    w[:,0] = f(linspace(xl+h,xl+m*h,m))                  # initial conditions
    for j in range(0,N):
        w[:,j+1] = dot(a,w[:,j]) + sigma*hstack([lside[j],zeros(m-2),rside[j]])
    return w
    
def f(x=None):
    u = (sin(2*pi*x)) ** 2
    return u
    
def l(t=None):
    u = 0*t
    return u
    
def r(t=None):
    u = 0*t
    return u

xl=0.;  xr=1.;  yb=0.;  yt=1.; M=10;  N=250
    
w = heatfd(xl,xr,yb,yt,M,N)

print 'w=',w

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)

xvals = linspace(xl,xr,M+1,endpoint=True)
yvals = linspace(yb,yt,N+1,endpoint=True)
X = empty([M+1,N+1])
Y = empty([M+1,N+1])
W = empty([M+1,N+1])
for j in range(N+1):
    X[:,j] = xvals
for i in range(M+1):
    Y[i,:] = yvals
for i in range(1,M):
    for j in range(N+1):
        W[i,j] = w[i-1,j]
W[0,:]=l(yvals)
W[M,:]=r(yvals)

ax.plot_wireframe(X, Y, W, rstride=1, cstride=1)

plt.show()

