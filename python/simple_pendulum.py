#Demonstrates Verlet integration method

T_max = raw_input('Final time:  ')
T_max = int(T_max)

dt = 0.01
N = int(T_max/dt)

from numpy import *
t = linspace(0,T_max,N)
omega = zeros((N))
theta = copy(omega)
E = copy(theta)

# Physical parameters
g = 9.8
mass = 1
length = 1

energy = lambda theta, omega: 0.5 * mass * length**2 * \
		(omega**2 + (g/length)* theta**2)

# initial conditions
omega[0] = 0
theta[0] = 0.1
E[0] = energy(theta[0], omega[0])

time = 0;
'''
# Euler-Cromwell loop
for n in range(N-1):
	time += dt
	omega[n+1] = omega[n] - dt * g/length * theta[n]
	theta[n+1] = theta[n] + dt * omega[n+1]
	E[n+1] = energy(theta[n+1], omega[n+1])
'''

# Verlet loop
for n in range(1,N-1):
	time += dt
	theta[n+1] = 2*theta[n] - theta[n-1] - (g/length) * theta[n] * dt**2

	E[n] = energy(theta[n], (theta[n+1]-theta[n-1])/(2*dt))

E[n+1] = energy(theta[n+1], (theta[n+1]-theta[n-1])/(2*dt))
from pylab import *
plot(t, theta)
ylabel(r'$\theta$')
xlabel('t')
show()

print 'energy: ', E
