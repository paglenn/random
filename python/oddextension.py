from numpy import *
from pylab import *

x = linspace(-1.,1,100)
y = x**3.-x

X = linspace(-6,6,600)
Y = cos(n*X)##array(6*list(y))

plot(X,Y)
xlabel('x')
ylabel('g(x)')
title('Initial profile')
savefig('gextension.png')
show()