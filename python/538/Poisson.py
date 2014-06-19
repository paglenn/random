# Program 8.3 Finite difference solver for 2D Poisson equation
#   with Dirichlet boundary conditions on a rectangle
# Input: rectangle domain [xl,xr]x[yb,yt], covered by MxN grid
# Output: matrix w where w[i-1,j-1] approximates solution 
#                    at (xl+i*(xr-xl)/M,yb+j*(yt-yb)/N), 1<=i<=M-1, 1<=j<=N-1
# Example usage: w=poisson83(0.,1.,1.,2.,10,10) 
import numpy as np
from numpy import *
def poisson83(xl=None, xr=None, yb=None, yt=None, M=None, N=None):
    m = M - 1; n = N - 1
    h = (xr-xl)/M; h2 = h**2; k = (yt-yb)/N; 
    r = h2/k**2; s = 2*(1+r)
    x = linspace(xl,xr,M+1,endpoint=True)   # mesh such that x[0]=xl, x[2]=xl+h and x[M]=xr
    y = linspace(yb,yt,N+1,endpoint=True)   # mesh such that y[0]=yb, y[2]=yb+k and y[N]=yt
    a = zeros([m*n,m*n]); b = zeros(m*n)    # initialize structure matrix a
# load structure matrix a
    z = zeros(m-2)                          # to be used in construction of a 
# inner core
    for i in range(2,m):      
        for j in range(2,n):
            a[-1+i+(j-1)*m,:] = hstack([zeros(i-1+(j-2)*m), r, z, 1., -s, 1., z, r, zeros((n-j)*m-i)])
            b[-1+i+(j-1)*m] = h2*f(x[i], y[j])        
# outer ring
    j = 1                                   # bottom row
    for i in range(2,m):
        a[-1+i+(j-1)*m,:] = hstack([zeros(i-2), 1., -s, 1., z, r, zeros((n-j)*m-i)])
        b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - r*gbottom(x[i])    
    j = n                                   # top row
    for i in range(2,m):
        a[-1+i+(j-1)*m,:] = hstack([zeros(i-1+(j-2)*m), r, z, 1., -s, 1., zeros(m-i-1)])
        b[-1+i+(j-1)*m]= h2*f(x[i], y[j]) - r*gtop(x[i])    
    i = 1                                   # left side
    for j in range(2,n):
        a[-1+i+(j-1)*m,:] = hstack([zeros(i-1+(j-2)*m), r, z, 0., -s, 1., z, r, zeros((n-j)*m-i)])
        b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - gleft(y[j])    
    i = m                                   # right side
    for j in range(2,n):
        a[-1+i+(j-1)*m,:] = hstack([zeros((j-1)*m-1), r, z, 1., -s, 0., z, r, zeros((n-j)*m-i)])
        b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - gright(y[j])    
# four corners
    i = 1; j = 1;                           # bottom left
    a[-1+i+(j-1)*m,:] = hstack([-s, 1, z, r, zeros((n-1)*m-1)])
    b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - r*gbottom(x[i]) - gleft(y[j])
    i = m; j = 1;                           # bottom right
    a[-1+i+(j - 1)*m, :] = hstack([z, 1, -s, 0, z, r, zeros((n - 2)*m)])
    b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - r*gbottom(x[i]) - gright(y[j])
    i = 1; j = n;                           # top left
    a[-1+i+(j - 1)*m, :] = hstack([zeros((n-2)*m), r, z, 0., -s, 1., zeros(m-2)])
    b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - r*gtop(x[i]) - gleft(y[j])
    i = m; j = n;                           # top right
    a[-1+i+(j - 1)*m, :] = hstack([zeros((n-1)*m-1), r, z, 1., -s]) 
    b[-1+i+(j-1)*m] = h2*f(x[i], y[j]) - r*gtop(x[i]) - gright(y[j])
#
    v = linalg.solve(a,b)                   # solve linear system a v = b for vector v
#
    w = zeros([m,n])                        # put solution into mesh
    for i in range(1,m+1):
        for j in range(1,n+1):
            w[i-1,j-1] = v[-1+i+(j-1)*m]
    return w
def f(x=None, y=None):                      # right hand side of equation
    u = 0
    return u
def gbottom(x=None):                        # bottom of rectangle
    # Use dot notation
    u = log(x**2+1.)
    return u
def gtop(x=None):                           # top of rectangle
    u = log(x**2+4.)
    return u
def gleft(y=None):# left side of rectangle
    u = 2*log(y)
    return u
def gright(y=None):# right side of rectangle
    u = log((y**2)+1.)
    return u
xl = 0.; xr = 1.; yb = 1.; yt = 2.; M = 10; N = 10
w = poisson83(xl,xr,yb,yt,M,N) 
print 'w =',w
from mpl_toolkits.mplot3d import Axes3D     # prepare to plot
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
W = zeros([M+1,N+1])                        # W such that W[i,j] approximates solution at
                                            #   (xl+i*(xr-xl)/M,yb+j*(yt-yb)/N) where  0 <= i <= M,  0 <= j <=N
yvals = linspace(yb,yt,N+1,endpoint=True)
W[0,:] = gleft(yvals)
W[N,:] = gright(yvals)
xvals=linspace(xl,xr,M+1,endpoint=True)
W[:,0] = gbottom(xvals)
W[:,M] = gtop(xvals)
for i in range(1,M):
  for j in range(1,N):
     W[i,j] = w[i-1,j-1]
                                            # the points (x,y,w) given by (X[i,j],Y[i,j],W[i,j]) will be plotted
                                            # in 3d as a wireframe figure.
X = zeros([M+1,N+1])
Y = zeros([M+1,N+1])
for i in range(M+1):
    Y[i,:] = yvals
for j in range(N+1):
    X[:,j] = xvals
ax.plot_wireframe(X, Y, W, rstride=1, cstride=1)
plt.show()
