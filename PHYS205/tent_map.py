import numpy as np
import matplotlib.pyplot as plt
import sympy

def f(x) :
    if x <= 0.5 :
        return 2*x
    elif x >= 0.5  and x <= 1.0:
        return 2*(1-x)
    else:
        print x , ' > 1'
        quit()
nsteps = 20000000
nsteps = 300
#y = 2./np.pi
# y = 1./2
y = 0.1*sympy.pi

#y = np.pi / 4.
#y = 1./np.exp(1)
print round(y,15)
Y = np.zeros(nsteps+1)
B = np.copy(Y)
Y[0]= round(y,15)
B[0] = round(y, 0)
f1 = 0.0 # fraction of zeroes preceded by a 1
TC = 0.0
for i in range(1,nsteps + 1) :
    print i, y, round(y,15)
    if i%2 == 0:
        #y = f(y) * (1 + 0.5e-16*np.pi)
        y = f(y)
    else:
        #y = f(y) * (1- 0.5e-16*np.pi)
        y = f(y)



    Y[i] = round(y,15)


    B[i]  = round(y)

    # check if 0 is preceded by 0 or 1
    if B[i] == 0 :
        f1 += B[i-1]
        TC += 1



print Y # start point
B = list(B)
n0 = B.count(0)
n1 = B.count(1)
print 'f0: ', n0 / TC
print 'f1: ', n1 / TC
print "freq of zeroes preceded by 1 , ", f1 / float(n0)
print B[-10:]

# next we will try converting the number to binary . o
if 0:
    x = Y[0]
    binaryStr = '.'
    for i in range(50):
        x *= 2
        if x >= 1 :
            binaryStr += '1'
            x -= 1
        else:
            binaryStr += '0'

    print 'binary: ', binaryStr
