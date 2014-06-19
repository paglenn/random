from scipy.spatial import Voronoi, ConvexHull
from torus import torus, torusplot
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D


npoints = 10
a= 5
b = 1
P = torus(npoints, a, b)
tPoints = Voronoi(P)
hull = ConvexHull(P)

ax = torusplot(npoints, a, b)
ax.set_xlim3d(-a, a)
ax.set_ylim3d(-a,a)
ax.set_zlim3d(-a,a)


for simplex in hull.simplices:
	#print P[simplex, :]
	ax.plot_wireframe(P[simplex,0], P[simplex,1], P[simplex,2])



#sample points are P
#for point in P:


plt.show()
