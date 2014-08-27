import math
import numpy as np

Tvals = np.linspace(1e-8,4,100)
T = 4.
f1 = lambda m: m
f2 = lambda m: math.tanh(4*m/T)

X = np.linspace(0,1,100)
Y1 = [f1(x) for x in X ]
Y2 = [f2(x) for x in X ]
def f(m):
    global T
    return m - math.tanh(4*m/T)
import matplotlib.pyplot as plt
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.show()

from scipy.optimize import newton
Y = []
for T in Tvals[:-1]:
    Y.append(newton(f,0.5))

plt.plot(Tvals[:-1],Y)
plt.show()

