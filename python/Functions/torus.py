from numpy import *
from matplotlib.axes import Axes
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def torusplot(npoints, offset =1, radius=1, style='points'):
	''' torus(num_points, offset from center, radius)'''
	ax = (plt.figure()).add_subplot(111,  projection= '3d', aspect=1)
	theta = linspace(0.,2*pi,npoints)
	phi = linspace(0, 2*pi, npoints)
	offset  = offset * ones((npoints))
	
	# Torus formulae
	X = outer(offset + radius*cos(phi), cos(theta))
	Z = outer(radius*sin(phi),ones((npoints)))
	Y = outer(offset + radius*cos(phi), sin(theta))
	
	if style == 'points': ax.scatter(X,Y,Z)
	elif style == 'surf': ax.plot_surface(X,Y,Z)
	
	return ax

def torus(npoints, offset =1, radius=1):
	''' torus(num_points, offset from center, radius)'''
	
	theta = linspace(0 ,2*pi ,npoints)
	phi = linspace(0, 2*pi, npoints)
	offset  = offset * ones((npoints))
	X = outer(offset + radius*cos(phi), cos(theta))
	Z = outer(radius*sin(phi),ones((npoints)))
	Y = outer(offset + radius*cos(phi), sin(theta))
	
	x = matrix(X.ravel()).transpose()
	y = matrix(Y.ravel()).transpose()
	z = matrix(Z.ravel()).transpose()
	
	Points = hstack((x,y,z))
	return Points

