# 2d self-avoiding random walk
#high rejection rate --> VERY SLOW...
import numpy as np
import matplotlib.pyplot as pp
import random
import time

def SAW(Nsteps):
	goodPath = 0

	while goodPath == 0:

		#R = np.zeros((2,Nsteps))
		start = (0,0)
		R = np.array(start)
		visited_sites = [start]

		for i in range(1,Nsteps):
			directions = [(0,1),(0,-1),(1,0),(-1,0)]
			random_dir = random.choice(directions)
			R += np.array(random_dir)

			#tR = tuple(R)
			if tuple(R) in visited_sites:
				goodPath = 0
				break
			else:
				visited_sites.append(tuple(R))
				goodPath = 1

	return visited_sites
print(SAW(10))
'''
start_time = time.time()
for i in range(10000): P = SAW(10)
print np.array(P).T
print("{0:e}".format(time.time()-start_time) )



pp.plot(path[0],path[1],'ro')
pp.plot(path[0],path[1],'k')
pp.xlim(min(path[0])-1,max(path[0])+1)
pp.ylim(min(path[1])-1,max(path[1])+1)
pp.show()

'''
