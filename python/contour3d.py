from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

delta = 0.025 
x = arange(-3.,3.,delta)
y = arange(-2.,2.,delta)
X, Y = p.meshgrid(x,y)
Z1 = p.bivariate_normal(X,Y,1. ,1. ,0. ,0.)
Z2 = p.bivariate_normal(X,Y,1.5 ,0.5 ,1 ,1 )
# difference of Gaussians
Z = 18*(Z2-Z1)

fig = p.figure()
ax = p3.Axes3D(fig)
ax.contourf3D(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.add_axes(ax)
p.show()
