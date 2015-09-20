import matplotlib.pyplot as plt
import numpy as np
import parameters
numWindows = parameters.num_windows
windowFiles = [open("window_%i"%w,'r') for w in range(numWindows) ]

for f in windowFiles:
    Z = []
    t = []
    for line in f.readlines():
        row = line.split('\t')
        try:
            t.append(float(row[0]))
            Z.append(float(row[1][:-1]))
        except:
            continue
    #plt.hist(Z)
    while len(Z) < len(t): t.pop()
    plt.plot(t,Z)
for window in parameters.windows:
    plt.hlines(window,0,parameters.nsteps)
#plt.savefig('ts.png')
#plt.title('k ~ 1e-7, T = 1e9' )
plt.show()

