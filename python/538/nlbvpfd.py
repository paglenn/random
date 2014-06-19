# Program 7.1 Nonlinear Finite Difference Method for BVP
# Uses Multivariate Newton's Method to solve nonlinear equation
# Inputs: interval inter, boundary values bv, number of steps n
# Output: solution w
# Example usage: w=nlbvpfd([0 1],[1 4],40);
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros
from numpy import linalg
from numpy import linspace
def nlbvpfd(inter=None, bv=None, ninput=None):
    global h, n, ya, yb # needed in f and jac functions
    a = inter[0]    
    b = inter[1]    
    ya = bv[0]   
    yb = bv[1]    
    n = ninput
    h = (b - a) / (n + 1)# h is step size
    w = zeros([n])# initialize solution array w
    for i in range(20):    # loop of Newton step
        s = linalg.solve(jac(w),f(w))
        print 's=',s
        w = w - s    
    tt=linspace(a,b,n+2);
    ww = zeros([n+2])
    ww[0]=ya
    for im1 in range(n):
        i=im1+1
        ww[i]=w[im1]
    ww[n+1]=yb
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(tt,ww,'-')
    ax.plot([a,b],[ya,yb],'o')
    plt.show()
    return w
def f(w=None):
    global h, n, ya, yb
    y = zeros([n])
    y[0] = ya - (2 + h ** 2) * w[0] + h ** 2 * w[0] ** 2 + w[1]
    y[n-1] = w[n - 2] - (2 + h ** 2) * w[n-1] + h ** 2 * w[n-1] ** 2 + yb
    for im2 in range(n-2):
        i = im2 + 2
        y[i-1] = w[i-1 - 1] - (2 + h ** 2) * w[i-1] + h ** 2 * w[i-1] ** 2 + w[i-1 + 1]    
    return y   
def jac(w=None):
    global h, n, ya, yb
    a = zeros([n, n])
    for im1 in range(n):
        i = im1 + 1    
        a[i-1, i-1] = 2 * h ** 2 * w[i-1] - 2 - h ** 2    
    for im1 in range(n-1):
        i = im1 + 1    
        a[i-1, i-1 + 1] = 1.    
        a[i-1 + 1, i-1] = 1.   
    return a
print 'Starting nlbvp..'
w=nlbvpfd([0.,1.],[1.,4.],40)
print 'w=',w

    
