import numpy as np
import matplotlib.pyplot as plt

a = np.genfromtxt("output.dat")
t = a[:,0]
x0 = 2*np.cos(t)
x1 = -0.25 * np.sin(t) + 1./12 * np.sin(3*t)
xprime_0 = -2*np.sin(t)

x = a[:,1]
y = a[:,2]


plt.plot(t,x, label='exact solution')
plt.plot(t,x0,label='x0')
plt.plot(t,x0+ 0.5*x1,label='x_approx')
#plt.plot(t,abs(x-x0),label='diff')
plt.legend()
plt.show()

