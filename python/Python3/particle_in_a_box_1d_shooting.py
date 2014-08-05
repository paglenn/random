import numpy as np
import math as m

N = 10000
L = 2
dx = L/N # okay in Python3 since fp division is default
V = np.zeros(N+1)
V[N//2:-1] = 1e7
parity = 1 # 0 for even ; 1 for odd

def calculate():
	E = 0.
	dE = 0.5
	b = 1.0 # cutoff for psi[i]
	tol = 1e-6
	last_divergent = 0.
	psi = np.zeros(N+1)
	if parity == 0 :
		psi[0] = psi[1] = 1. # Even-parity solution
	else:
		psi[0] = 0 ; psi[1] = dx
	while m.fabs(dE) > tol:

		for i in range(1,N):
			psi[i+1] = 2*psi[i] - psi[i-1] - 2*(dx**2.)*(E-V[i])*psi[i]

			psi_diverges = m.fabs(psi[i+1]) > b
			if psi_diverges:
				break

		if last_divergent * psi[i+1] < 0:
			dE /= -2 # okay in Python3 since fp div is default

		E += dE
		last_divergent = np.sign(psi[i+1] )

	# Even parity of psi
	return psi, E

psi, E = calculate()
if parity == 0:
	psi = np.hstack((psi[::-1],psi[1:]))
else:
	psi = np.hstack((-psi[::-1],psi[1:]))
V = np.hstack((V[::-1],V[1:]))
#print('Error: {0:.2f}%'.format(100*abs(E - m.pi**2 /8)*8/m.pi**2))
import matplotlib.pyplot as pp
X = np.linspace(-L,L,2*N+1)

# Normalize psi
import scipy.integrate
psi2 = np.fabs(psi) ** 2.

C = 1/np.sqrt(scipy.integrate.simps(psi2[N//2:3*N//2+1],X[N//2:3*N//2+1]))
psi *= C
print(C)

pp.plot(X,psi,'k--',label=r'$\psi(x)$')
pp.plot(X,V,'k',lw=1.5, label=r'$V(x)$')
pp.text(0,-0.5,'E = {0:.4f}'.format(E))
pp.ylim(-1.1*L,1.1*L)
pp.legend()
pp.show()
quit()
