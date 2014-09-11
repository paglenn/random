import math
L = 20
T = 2.0
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 40000
N = L * L
magFile = 'magnetization.dat'
energyFile = 'energy.dat'

#umbrella sampling specific
num_windows = 10
windows = []
for x in range(num_windows):
    window_ceil = N*(-1 + 2.*(x+1)/num_windows)
    #window_ceil = round(window_ceil,13)
    window_floor = N*(- 1 + 2.*x/num_windows)
    #window_floor = round(window_floor,13)
    #windows.append((N*(- 1 + 2.*x/num_windows),N*(-1 + 2.*(x+1)/num_windows) ) )
    windows.append((window_floor,window_ceil))
window_edges = [w[1] for w in windows]
