# wham_driver.py
# plot FE from WHAM output file
from subprocess import call
import parameters as par
import numpy as np
import matplotlib.pyplot as plt
nb = 100
call("./wham"+" -400.0 400.0 %i 100.0 100.0 0 metadata.dat wham_output.dat"%nb,shell=True)
'''
infile = open('wham_output.dat','r')
M = list()
A = list()
for line in infile.readlines():
    cols = line.split('\t')[:-1]
    if any('#' in x for x in cols): continue
    M.append(float(cols[0]))
    A.append(float(cols[1]))

plt.xlabel(r'M')
plt.ylabel(r'$A(M)$')
plt.plot(M,A)
plt.title(r'T = %.2f'%par.T)
plt.savefig('fe.png')
plt.show()
'''
