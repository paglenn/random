import numpy
from rk4 import rk4
from pylab import plot, show

def damped_spring(t, state):
    pos, vel = state
    stiffness = 1
    damping = 0.05
    return numpy.array([vel, -stiffness*pos - damping*vel])

t = 0
dt = 1.0/40
state = numpy.array([5, 0])
print('%10f %10f' % (t, state[0]))
T = []
X = []
while t < 100:
    t, state = rk4(t, dt, state, damped_spring)
    T.append(t)
    X.append(state[0])
#    print('%10f %10f' % (t, state[0]))
T = numpy.array(T)
X = numpy.array(X)

plot(T,X)
show()
