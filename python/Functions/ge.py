from numpy import *


def ge(a,b):
    n = len(b)
    #GE
    for j in range(0,n-1):
        for i in range(j+1,n):
            mu = float(a[i,j]/a[j,j])
            for k in range(j+1,n):
               a[i,k] -= mu*a[j,k]
            b[i]-=mu*b[j]

    #BS
    # x=empty(n) #new array for solution
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            b[i] -= a[i,j]*b[j]
        b[i] /= a[i,i]
    return b

