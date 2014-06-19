from numpy import *
from pylab import *
import scipy as sp

L = 1.
M = 1000
h = L/float(M)
m = M - 1
T = 1.
N = 10000
#k = T/float(N)

epsilon = h
k = 2*epsilon**2
lamda = 2*epsilon**2/k

def V(x):
	#if x >= .5 and x <= .6:
	#	return 100.*(pi/(20.*epsilon))
	#else:
	return 0.

def l(t):
	return 0.

def r(t):
	return 0.

def f(x):
	x0 = L/4.
	sigma = L/20.
	K0 = pi/(20*epsilon)
	#return exp(1.0j*(L/(4.*T))*x)*exp(-2000.*(x-L/4.)**2/(2.*(L/20.)**2))
	return exp(1.0j*K0*x)*exp(-(x-x0)**2/(2.*(sigma)**2))


x = linspace(0,L,M+1)

A = array(eye(m),dtype=complex)
for i in range(m-1):
	A[i,i+1] = 1.
	A[i+1,i] = 1.
	A[i,i] = lamda*1.0j - 2. - epsilon*epsilon*V(x[1:-1][i])



B = array(eye(m), dtype = complex)
for i in range(m-1):
	B[i,i+1] = -1.
	B[i+1,i] = -1.
	B[i,i] = lamda*1.0j + 2. + epsilon*epsilon*V(x[1:-1][i])


w = f(x)
w = array(w,dtype=complex)
t = array(range(N+1))*k
w[0]= l(t[0])
w[-1]= r(t[0])
ion()
#hlines(.5,.5,.6)
#vlines([.5,.6],0., .5)
p, = plot(x,abs(w),'g')
#p, = plot(x,real(w),'g')
for j in range(N):
	wtemp = dot(B, w[1:-1])
	w[1:-1] = linalg.solve(A,wtemp)
	w[0] = l(t[j])
	w[-1] = r(t[j])
	if j % 100 is 0:
		#p.set_ydata(real(w))
		p.set_ydata(abs(w))
	draw()

ioff()
show()
