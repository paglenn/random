import math
allM = []
allP = []
for i in range(10):
    infile = open("window_%i"%i, 'r')
    M = []
    P = []
    for line in infile.readlines():
        formatted_line = line.split()
        m = float( formatted_line[0] )
        p = float( formatted_line[1] )
        M.append(m)
        P.append(p)
    P = [x/max(P) for x in P]
    allM.append(M)
    allP.append(P)

#print allM
#print allP
for i in range(9):
    m1 = allP[i][-1]/allP[i+1][0]
    #m1 = (allP[i][-1])**2 / allP[i][-2] / allP[i+1][0]
    allP[i+1] = [allP[i+1][x]*m1 for x in range(len(allP[i+1])) ]
    #allP[i+1][0] *= allP[i][-1]**2. / allP[i][-2]

m = []
logP = []
mod = 0.0
modFlag = False

for i in range(10):
    #if i != 0: regularizer = 2*math.log(allP[i-1][-1]) -  math.log(allP[i-1][-2]) - math.log(allP[i][0])
    #else: regularizer = 0

    for j in range(len(allP[i])):

        if allP[i][j] != 0:
            m.append(allM[i][j])
            if m[-1] >= 0.0 and not modFlag:
                mod = logP[-1] + math.log(allP[i][j])
                #mod = 0.0
                modFlag = True
            #if j +1 == len(allP[i]) : logp = - math.log(allP[i][j]) - regularizer
            #else: logp = - math.log(allP[i][j]) - regularizer
            #logP.append( - math.log(allP[i][j]) )
            logp = - math.log( allP[i][j]) + mod
            logP.append(logp)
        else:
            print 'Bad sampling '

import matplotlib.pyplot as plt
#import numpy as np
#from scipy.interpolate import spline
#xnew = np.linspace(min(m), max(m), 1000)
#logP_smooth = spline(m, logP, xnew)
#plt.plot(xnew, logP_smooth)
#for i in range(len(m)):
    #print m[i]
    #print logP[i]
plt.plot(m, logP,'o-')
plt.xlabel('magnetization per spin')
plt.ylabel(r'dimensionless free energy ($\beta$F)' )
#plt.title(r'T = 3.0$J/k_{B}, h = 1.0$ ')
plt.title('30x30 lattice , T = 1.0 [J/k]')
#plt.savefig('T=3p0_h=1.0.png')
#plt.savefig('T=3.png')
#plt.savefig('T=1.png')
plt.savefig('T=1_L=30.png')
plt.axhline()
plt.show()




