from numpy import *

# Temperature values to test
T = linspace(0.01,10,1000)

# Rotational states
num_states = 2
Jvals = linspace(0,num_states, num_states)

# Energy , boltzmann factor, degeneracy, etc.
from math import sqrt
e = lambda j: j#j*(j+1)#j*sqrt(j)#j*(j+1)
B = lambda e,t: exp(-e/t)
g = lambda j:2 #2*j+1
beta = lambda i: 1./T[i]
Z = lambda t: sum([ g(j)*B(e(j),t) for j in Jvals ] )

logZ = lambda Z: log(Z)
Crot = empty(T.shape[0])
Zvals = copy(Crot); Zvals[0] = 1
# Loop over temperatures
for i in range(1,len(T)-2):

	t = T[i]
	z = Z(t)

	#print z

	#finite difference for derivative wrt beta
	E = lambda i: - (logZ(Z(T[i])) - logZ(Z(T[i-1])))/(beta(i)-beta(i-1))

	C = (E(i+1) - E(i) )/(T[i+1]-T[i])
	Crot[i] = C

	Zvals[i] = z
print Crot
from pylab import *
'''
# Plot specific heat
fig = figure(facecolor='w')
plot(T, Zvals)
title('Partition function T-dependence for diatomic molecule')
xlabel(r'T/$T_{rot}$')
ylabel('Z_rot')
ylim(0,10)
yticks(arange(1,10))
plot(10*[1], arange(10),'.')
plot(T[0::50],len(T[0::50])*[1], '.')
show()
'''
fig = figure(facecolor='w')
plot(T, Crot)
#plot(T[0::50],ones(T[0::50].shape),'k.')
Tmax = T[list(Crot).index(max(list(Crot[1:len(list(T))/2.])))] ; print Tmax
#plot(20*[Tmax],linspace(0,1.5,20),'.')
ylim(0,2)
xlim(min(list(T)), T[int(0.9*T.shape[0])])
#title('Rotational heat capacity for diatomic molecule')
title('Heat capacity: quadratic energy term, 2*j - degeneracy')
xlabel(r'T/$T_{rot}$')
ylabel(r'$C_V$')
savefig('quad_diff_deg.png')
#ylabel(r'$C_{rot}$')
#savefig('C_rotor.png')
show()
