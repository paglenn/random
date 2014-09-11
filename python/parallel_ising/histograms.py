from parameters import *
import matplotlib.pyplot as plt
import numpy as np

windowFiles = [open(fname,'r') for fname in window_files.values() ]

for f in windowFiles:
    M = []
    for line in f.readlines()[:-1]:
        M.append(float(line.split('\t')[-1][:-1]))
    #plt.hist(M)
    binContents,bins = np.histogram(M,bins=20,density=True)
    bins = [0.5*sum(bins[i:i+2]) for i in range(len(bins)-1) ]
    plt.plot(bins,binContents)
plt.show()


