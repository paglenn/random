# 2d self-avoiding random walk
#high rejection rate --> VERY SLOW...
import numpy as np
import matplotlib.pyplot as pp
import random

def SAW ( Nsteps):
	goodPath = 0

	while goodPath == 0:
		X = [0 for i in range(Nsteps) ]
		Y = [0 for i in range(Nsteps) ]
		visited_sites = [(0,0) for i in range(Nsteps) ]

		for step in range(1,Nsteps):
			directions = [(0,1),(0,-1),(1,0),(-1,0)]
			#directions=  [(-1,1),(1,1),(1,-1),(-1,-1)]
			random_dir = random.choice(directions)
			x = X[step-1] + random_dir[0]
			y = Y[step-1] + random_dir[1]
			if (x,y) in visited_sites:
				goodPath = 0
				##pp.clf()
				break
			else:
				X[step] = x
				Y[step] = y
				visited_sites[step] = (x,y)
				goodPath = 1

	#pp.plot(X,Y)
	#pp.plot(X[0],Y[0],'r.',ms=12)
	#pp.xlim(-Nsteps,Nsteps)
	#pp.ylim(-Nsteps,Nsteps)
	#pp.show()

	return visited_sites

'''

Nsteps = int(20)
# print SAW(Nsteps)
Ntrials = 1000
trials = range(Ntrials)
#R2 = [0 for i in range(Nsteps)]
R2 = np.zeros(Nsteps)
for trial in trials:
	stepSeq = SAW(Nsteps)
	r2 = [ x[0]**2 + x[1]**2 for x in stepSeq]
	R2 += np.array(r2)/float(Ntrials)
	#R2 = [ R2[i] + r2[i]/float(Ntrials) for i in range(Nsteps)]

fig = pp.figure()
ax = fig.gca()
ax.set_xscale('log')
ax.set_yscale('log')
pp.plot(range(1,Nsteps),R2[1:],'ks')
testFn = np.array(range(Nsteps)) **1.44
pp.plot(range(1,Nsteps),testFn[1:],'b')


pp.show()
'''







