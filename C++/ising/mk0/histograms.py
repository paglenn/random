from parameters import *
import matplotlib.pyplot as plt
import numpy as np

windowFiles = [open(fname,'r') for fname in window_files.values() ]

for f in windowFiles:
    M = []
    for line in f.readlines():
        M.append(float(line.split('\t')[-1][:-1]))
    #plt.hist(M)
    binContents,bins = np.histogram(M,bins=10,density=True)
    bins = [0.5*sum(bins[i:i+2]) for i in range(len(bins)-1) ]
    #ref_var = np.var(M)
    #ref_mu = np.mean(M)
    #ref = (1./math.sqrt(2*math.pi*ref_var)) * np.exp(-0.5*((bins - ref_mu )/ref_var)**2.)
    plt.plot(bins,binContents)
    #plt.plot(bins,ref,'.')
plt.show()


