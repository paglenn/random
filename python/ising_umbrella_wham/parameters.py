import math
L = 20
T = 2.0
nsteps = 5000
npasses = 1000
N = L * L
magFile = 'magnetization.dat'
energyFile = 'energy.dat'
progressFile = 'progress'

# definition of nearest neighbors
nbr = dict()
for i in range(L):
    for j in range(L):
        # periodic BCs
        nbr[(i,j)] = (((i+1)%L,j),((i-1)%L,j),(i,(j+1)%L),(i,(j-1)%L))

#umbrella sampling specific
num_windows = 10
k = 0.001
num_bins = 100
windows = []
minima = []
for x in range(num_windows):
    windows.append([N*(- 1 + 2.*x/num_windows),N*(-1. + 2.*(x+1)/num_windows) ] )
    overlap = 0.3*(windows[-1][1] - windows[-1][0])
    windows[-1][1] += overlap
    minima.append(0.5*sum(windows[-1]))
#windows[-1][1] -= overlap
#minima[-1] = 0.5*sum(windows[-1])

window_edges = [w[1] for w in windows]
window_files = dict(enumerate('window_%i'%i for i in range(num_windows)))
