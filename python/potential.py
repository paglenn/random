from numpy import *
from pylab import *
N = 1000
xi = linspace(0,1,N)
t = linspace(0,1000,100*N)
p1,p2 = [1./6, 5./6]
'''
def V(x):
	a = 0.3 # shift energy up a bit...
	k = 10 #stiffness is good for a scale factor
	mp = 0.5*(p1+p2)
	V1 = lambda x: a+0.5*k*(x-p1)**2.
	V2 = lambda x: a+0.5*k*(x-p2)**2.
	Vx  = (x-p2)*V1(x) + (p1-x)*V2(x)
	return Vx
	#if x <= mp: Vx = a+0.5*k*(x-p1)**2.
	#elif x >= mp: Vx = a+0.5*k*(x-p2)**2.
	#return Vx
'''
Vx = []
xf = []
V = lambda x: 0.5*(1+sin(3*pi*(x-1./3)))

for x in xi:
	Vx.append( V(x))
	mp = 0.5*(p1+p2)
	if x <mp: xf.append(p1)
	elif round(x,4) == 0.5045: xf.append(mp)
	elif x > mp: xf.append(p2)

plot(xi, Vx,'b.',label=r'$V(x)$')
plot(xi,xf,'r.',label=r'$x_f(x_i)$')
xlabel(r'$x$')
legend(loc=2)
savefig('discontinuity.png')
show()


