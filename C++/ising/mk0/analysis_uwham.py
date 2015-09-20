import uwham
import numpy as np
import matplotlib.pyplot as plt
import parameters

Z = []
K = parameters.num_windows
N_k = np.zeros(K)
u = list()
infile = open('magnetization.dat','r')
for unformattedLine in infile.readlines():
    line = unformattedLine.split(' ')
    line[-1] = line[-1][:-1] # remove \n
    #print line
    zval = float(line[0])
    window = float(line[1])
    N_k[window] += 1.
    u.append( [ float(line[k]) for k in range(2,K+2) ])


u_kln = np.zeros((K,K,max(N_k)))
counter = 0
for k in range(K):
    for j in range(int(N_k[k])):
        u_kln[k,:,j] = u[counter]
        counter += 1

results = uwham.UWHAM(u_kln,N_k)
plt.plot(range(K),results.f_k,'--')
plt.show()
#plt.savefig('uwham_fe.png')



