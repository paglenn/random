from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

# u and v are parametric variables. 
# u is an array from 0 to 2*pi, with 100 elements
u  = r_[0:2*pi:100j]
# v is also an array from 0 to 2pi, with 100 elements. 
v = r_[0:2*pi:100j]
#x,y, and z are the coordinates of the points for plotting 
x = 10*outer(cos(u),sin(v))
y = 10*outer(sin(u),sin(v))
z = 10*outer(ones(size(u)),cos(v))
fig = p.figure()
ax = p3.Axes3D(fig)
ax.plot_surface(x,y,z)
ax.set_xlabel(r'X =r$sin(\theta)cos(\phi)$ ')
ax.set_ylabel(r'Y = $rsin(\theta)sin(\phi)$')
ax.set_zlabel(r'Z = r$cos(\theta)$')
p.show()