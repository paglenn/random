c = raw_input('Input wave speed: ')
N = raw_input('total number of grid points: ')
c = float(c); N = int(N)

import numpy as np
x = np.linspace(0,1,N)
dx = max(np.diff(x))
dt = dx/c

u0 = 0.5 * np.exp(-100*np.power(x-0.5*np.ones(x.shape),2))
#u0 = 0*u0; u0[N/2-10:N/2+10] = 1
u1 = np.copy(u0); u2 = np.copy(u0);

import pylab as pl
pl.plot(x,u0)
pl.axis([-0.1, 1.1, -1.1, 1.1 ] )
pl.xlabel('x') ;  pl.ylabel(r'$u_0(x,t)$')
pl.show()

time = 0
mu = (c*dt/dx)**2.

step = 0;
ind = 0;

for ix in range(1200):
	step = step + 1;
	time = time +dt;

