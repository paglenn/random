import numpy as np
import math
import matplotlib.pyplot as plt
################################
# Exercise 1
def P(n,x,y) :
    fact = math.factorial
    _x_ = int(n * x  )+1
    _y_ = int(n * y)
    #print _x_
    #print _y_
    vals =[]
    for r in range(_x_, _y_) :
        vals.append( 1.*fact(n)/ (fact(n-r)* fact(r))  )

    return sum(vals) / 2.**n
'''
X =  np.linspace(0.0,0.9, 10)
Y = np.linspace(0.1,1.0,10)
#print X, Y
PMn = np.zeros(10)
N = [ 16, 32, 64, 128 ]
n = 128
for i in range(10):
    x = X[i]
    y = Y[i]
    PMn[i] = P(n,x, y)
    #print PMn[i]
plt.plot(0.5*( X + Y),PMn)
plt.show()
'''
###############################
# Exercise 2
#N = [16,32,64, 128]
'''
Nmax = 100
N = range(1,Nmax+1)
logP = np.zeros(Nmax)
for n in N :
    x = 0.6
    y = 1.0
    PMn = P(n,x,y)
    if PMn > 1e-6 : logP[n-1] = math.log(PMn)


plt.plot(N, logP)
plt.show()
'''

################################
# Exercise 3
Nmax = 150
N = range(Nmax/2,Nmax+1)
logP = np.zeros(Nmax/2+1)
Nx = 20
X = np.linspace(0.51,0.95,Nx)
I = np.zeros(Nx)
for i in range(Nx) :
    x = X[i]
    for j in range(Nmax/2) :
        y = 1.0
        n = N[j]
        PMn = P(n,x,y)
        if PMn > 0 : logP[j] = math.log(PMn)
        else: print x, y ; quit()
    I[i] = - np.polyfit(N,logP,1)[0]


_chi = 2*np.polyfit((X-0.5)**2, I , 1 )[0]
chi = 1./_chi
plt.plot((X - 0.5)**2., I)
plt.title(r'$\chi = %.2f$'%(chi))
plt.show()










