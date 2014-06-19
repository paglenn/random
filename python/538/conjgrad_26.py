#    Conjugate gradient method for solving [A]{x} = {b}.
#    User must supply the function Av(v) that
#      returns the vector [A]{v}.
from numpy import *
from numpy.linalg import norm

def conjgrad_26(Av,b):
    n = len(b); tol=1.0e-9
    x = zeros([n,n+1]); d = zeros([n,n+1]); r = zeros([n,n+1]);
    xappx = x[:,0]; d[:,0] = b; r[:,0] = b
    print 'x_ 0=',x[:,0]; print ' r_ 0=',r[:,0]; print ' d_ 0=',d[:,0]
    alpha = zeros([n+1]); beta = zeros([n+1])
    for i in range(1,n+1):
        ri1 = r[:,i-1];
        if(norm(ri1)) < tol:
            break
        else:
            di1 = d[:,i-1];  Adi1 = Av(di1)
            alpha[i] = dot(ri1,ri1)/dot(di1,Adi1)
            print 'alpha_',i,'=',alpha[i]
            x[:,i] = x[:,i-1] + alpha[i]*di1
            xappx = x[:,i]
            print 'x_',i,'=',x[:,i]
            r[:,i] = b[:] - Av(x[:,i])
            print 'r_',i,'=',r[:,i]
            r[:,i] = r[:,i-1] - alpha[i]*Adi1
            print 'r_',i,'=',r[:,i]
            beta[i] = -dot(r[:,i],Adi1)/dot(di1,Adi1)
            print 'beta_',i,'=',beta[i]
            d[:,i] = r[:,i] + beta[i]*di1
            print 'd_',i,'=',d[:,i]
    return xappx
def Av(x):         # evaluate Av for example 2.28
    A=array([[2.,2.],[2.,5]]);
    return dot(A,x)
b = array([6.,3.]) # vector b for example 2.28
xsoln = conjgrad_26(Av,b)
print 'xsoln=',xsoln
