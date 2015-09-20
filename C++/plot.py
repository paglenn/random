infile = open('coordinates.txt','r')
lines = infile.readlines()
X , Y , Z = 3*[[]]
X = list()
Y = []
Z = []
for line in lines:
    x,y,z = [float(w) for w in  line.split() ]
    X.append(x)
    Y.append(y)
    Z.append(z)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X,Y,Z,s=200)
plt.show()
