
from scipy import *
from pylab import *

#Creating grid of coordinates
x,y = ogrid[-1.:1.:0.01,-1.:1.:,0.01]

z = 3*y*(3*x**2-y**2)/4+0.5*cos(6*pi*sqrt(x**2+y**2)+arctan2(x,y))

hold(True)
#Creating image
imshow(z,origin = 'lower', extent = [-1,1,-1,1])

#Plotting contour lines
contour(z,origin = 'lower',extent  = [-1,1,-1,1])

xlabel('x')
ylabel('y')
title('A spiral!')

savefig('spiral')
