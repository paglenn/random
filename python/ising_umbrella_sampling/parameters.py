import math
L = 20
T = 2.0
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 1000
npasses = 1000
N = L * L
magFile = 'magnetization.dat'
energyFile = 'energy.dat'

#umbrella sampling specific
num_windows = 10
windows = []
for x in range(num_windows):
    windows.append((N*(- 1 + 2*x/num_windows),N*(-1 + 2*(x+1)/num_windows) ) )
window_edges = [w[1] for w in windows]
