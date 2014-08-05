import numpy as np
import random

def exit() : raise SystemExit
L = 20

class lattice:

	def __init__(self,L):
		self.L = L
		self.matrix = np.zeros((2,L,L))
		self.NoSpanningCluster = True
		self.size = L**2
		self.pc = None
		self.occupied = []
		# end init

	def neighbors(self,site,otherSite):
		i,j = site
		ip,jp = otherSite
		nn = abs(i - ip) + abs(j - jp) <= 1
		return nn

	def merge(self,site):
		i,j = site
		isBridge = False
		C = self.matrix[1,i,j]
		crossover = list()
		if C != 0:
			if j+1 != self.L:
				N = self.matrix[1,i,j+1]
			else: N = 0
			if i+1 != self.L:
				E = self.matrix[1,i+1,j]
			else: E = 0
			if j != 0:
				S = self.matrix[1,i,j-1]
			else: S = 0
			if i != 0:
				W = self.matrix[1,i-1,j]
			else: W = 0
			for nn in [N,E,S,W]:
				isBridge = isBridge or (nn!=0 and C != nn)
				if nn!=0 and C!=nn: crossover.append(nn)

			if isBridge and len(crossover) != 0:
				for index in crossover:
					cluster2 = zip(*np.where(self.matrix[1] == index) )
					for pair in cluster2:
						ip,jp = pair
						self.matrix[1,ip,jp] = C

		# end merge(self,site)
	def isBroken(self):
		if all([x == 1 for x in np.ravel(self.matrix[0]) ]):
			print('is broken...')
			print(self.matrix)
			print(self.NoSpanningCluster)
			print(self.matrix[1,i,j])
			print(self.matrix[1,i,j] in self.matrix[1,-1,:])
			return True
		else:
			return False

	def GetN(self):
		return len(self.occupied)

	def cluster_label(self):
		clusterNumber = 1
		i,j = np.random.choice(range(self.L),2)
		self.occupied.append((i,j))
		self.matrix[:,i,j] = clusterNumber
		while self.NoSpanningCluster :
			i,j = np.random.choice(range(self.L),2)
			if (i,j) in self.occupied: continue
			self.occupied.append((i,j))
			self.matrix[0,i,j] = 1

			for site in self.occupied:
				if self.neighbors(site,(i,j)):
					ip,jp = site
					self.matrix[1,i,j] = self.matrix[1,ip,jp]
			self.merge((i,j))
			if self.matrix[1,i,j] == 0:
				clusterNumber += 1
				self.matrix[1,i,j] = clusterNumber


			span = self.matrix[1,i,j] in self.matrix[1,0,:]
			span = span and self.matrix[1,i,j] in self.matrix[1,-1,:]
			span = span and self.matrix[1,i,j] in self.matrix[1,:,0]
			span = span and self.matrix[1,i,j] in self.matrix[1,:,-1]
			if span:
				self.NoSpanningCluster = False
				self.pc = self.GetN()/self.size
				return True

			if self.isBroken():
				return False

'''
myLattice = lattice(L)
if myLattice.cluster_label() :
	print(myLattice.pc)
else:
	print('Failed to make spanning cluster')
	print(myLattice.matrix)
exit()
'''
P = []
for itr in range(10):
	myLattice = lattice(L)
	myLattice.cluster_label()
	if not myLattice.NoSpanningCluster: P.append(myLattice.pc)
#hist,bin_edges = np.histogram(P,bins=20,density=True)
#X = [ 0.5* (bin_edges[i] + bin_edges[i+1]) for i in range(len(bin_edges[:-1])) ]

import matplotlib.pyplot as plt
#plt.plot(X,hist,color='b',lw=1.5)
plt.hist(P,bins=20,normed=True,histtype='step')
plt.show()






