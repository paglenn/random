import math as m

def fact(n):
	if n == 0: return 1
	if n < 100:return fact(n-1)
	else:
		Stirling = (n**(n/2.)) * m.exp(-n) * m.sqrt(2*m.pi*n) * (n**(n/2.))
		return Stirling

def series(x,n):
	iterm = lambda x,i: (x**i)/fact(i)
	s = 0.
	for i in range(n):
		s += iterm(x,i)

	return s

import numpy as np
x = np.linspace(90,100,100)
y = np.exp(-x)
ya = series(-x,200)

import pylab as plt
plt.plot(x,(y-ya)/y,label='deviation')
#plt.plot(x,ya,label='approx')
plt.legend()
plt.show()





