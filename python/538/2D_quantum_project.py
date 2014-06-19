from numpy import *
from pylab import *

	
L = 1.
M = 100
h = L/float(M)
m = M - 1
T = 1.
N = 100000
k = T/float(N)

epsilon = h
lamda = 2*epsilon**2/k

def V(x):
	if x >= .5 and x <= .6:
		return 20000.
	else:
		return 0.

def l(t):
	return 0.

def r(t):
	return 0.

def f(x):
	return exp(1.0j*(L/(4.*T))*x)*exp(-2000.*(x-L/4.)**2/(2.*(L/20.)**2))


x = linspace(0,L,M+1)
y = linspace(0,L,M+1)


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
xint = x[1:-1]
wint = w[1:-1]
w[0]= l(t[0])
w[-1]= r(t[0])
ion()
ylim(-.05,.25)
p, = plot(x,abs(w)**2,'g')
for j in range(N/310):
	wtemp = dot(B, w[1:-1])
	w[1:-1] = linalg.solve(A,wtemp)
	w[0] = l(t[j])
	w[-1] = r(t[j])
	p.set_ydata(abs(w)**2)
	draw()

ioff()
show()
