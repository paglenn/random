# Simulation of a Hodgkin-Huxley Neuron, using 4th-order Runge Kutta
# 01/08/2014

interval = [0,100] # Time interval
N = 2000 #Number of time steps

# initial values for voltage in and conductances
iv = [-65, 0,0.3,0.6]

# Neuron pulse parameters
global pStart, pEnd, pulse
pulse = raw_input('Pulse start, end, strength in microAmps')
pulse = pulse.split(',')
pStart = int(pulse[0]); pEnd = int(pulse[1]); pulse = int(pulse[2])

a,b = interval
h = dt = float(b-a)/N

import numpy as np
y = np.zeros((N,4))
y[0,:] = iv
t = np.zeros(N); t[0]  = a
print t

def HHsystem(t,w):
	global pStart, pEnd,pulse

	c = 1
	g1 = 120; g2 = 36; g3 = 0.3; # conductances in Siemens
	pMidpoint = (pStart + pEnd)/2.
	pLength = pEnd - pStart
	e0 = -65; e1 = 50; e2 = -77; e3 = -54.4 # reversal potentials in mV

	input = pulse*(1-np.sign(abs(t-pMidpoint) - pLength/2.))/2.
	v, m, n, h = w
	z = np.zeros(4)
	z[0] = (input - g1*(m**3)*h*(v-e1) -g2*(n**4)*(v-e2)-g3*(v-e3))/c;
	v -= e0;
	from math import exp
	z[1] = (1-m) * (2.5 - 0.1*v) / (exp(2.5-0.1*v)-1) -m*4*exp(-v/18)
	z[2] = (1-n) * (0.1 - 0.01*v) / (exp(1-0.1*v)-1) -n*0.125*exp(-v/80)
	z[3] = (1-h) * 0.07*exp(-v/20) -h/(exp(3-0.1*v) +1)
	return z

from rk4 import rk4
for i in range(N-1):
	t[i+1] = t[i] + h
	y[i+1,:] = rk4(t[i], y[i,:], HHsystem, h)

from pylab import *
subplot(3,1,1)
plot([a,pStart, pStart, pEnd,pEnd, b], [0,0,pulse, pulse, 0,0])
grid; axis([a-1, b+1, -0.5*pulse, pulse+0.5*pulse])
ylabel('input pulse')

subplot(3,1,2)
plot(t,y[:,0])
grid; axis([0,100,-100,100])
ylabel('voltage (mV) ')

subplot(3,1,3)
plot(t,y[:,1],t,y[:,2],t,y[:,3])
grid; axis([0,100,0,1])

show()

