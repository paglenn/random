# Lattice protein folding from primary structure
# initial conformation created using self-avoiding random walk
# Paul Glenn
import numpy as np
import random
import math
import matplotlib.pyplot as pp
from sys import argv

# user defined modules
from random_walk_2D_SA import SAW
from BasicStats import avg, var
from statistics import variance as var
randn = random.randint
rand  = random.uniform
exp = math.exp
unzip = lambda listOfTuples: zip(*listOfTuples)

###################################
# Definitions
# Initialize primary structure
global N, AA_dict

N = chainLength = 15
Nsteps = int(3e5)
fs = 1000 # frameskip
#PProtein = [randn(0,19) for x in range(N) ]
PProtein = np.random.randint(0,19,N)
# Interaction matrix J
#J = np.random.choice(np.linspace(-4,-2,1000),(20,20))
J = - 4*np.ones((20,20))
#J = 1*np.ones((20,20))
# Set thermodynamic settings
argc = len(argv)
if argc == 1: T = 10
else: T = int( argv[1] )
Tvals = np.hstack([ np.linspace(T,1.0,Nsteps/2),np.linspace(1.0,0.5,Nsteps/2)])
print('Temperature: %.2f'%T)
boltzmann = lambda dE: exp(-dE/T)

#AA_sites = SAW(chainLength)
AA_sites = list()
for itr in range(chainLength):
	AA_sites.append((itr,0))

print('Initial Structure generated')
AA_dict = dict(zip(AA_sites,range(N)))

def getBondsList(site,myAA_dict = AA_dict):
	resid = myAA_dict[site]
	bondsList = list()
	if resid != 0: bondsList.append(resid-1)
	if resid != N-1: bondsList.append(resid+1)

	return bondsList

def getContacts(site,myAA_dict = AA_dict):
	i,j = site
	contacts = []

	nnSites = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]
	for nnSite in nnSites:
		if nnSite in list(myAA_dict.keys()): contacts.append(myAA_dict[nnSite])
	return contacts

def energy(myAA_dict = AA_dict):
	E = 0.
	for pair in list(myAA_dict.keys()):

		i,j = pair

		contacts = getContacts(pair,myAA_dict)

		bondsList = getBondsList(pair,myAA_dict)

		for bonded in bondsList: contacts.remove(bonded)

		resName = PProtein[myAA_dict[pair]]

		for NB in contacts:
			contactResName = PProtein[NB]
			E += J[contactResName,resName]

	return E



def move_AA(x0,y0):
	site = (x0,y0)
	bonds = getBondsList(site,AA_dict)
	x = x0
	y = y0

	directions = dict([(1,(1,1)),(2,(1,-1)),(3,(-1,1)),(4,(-1,-1))])
	dkey = np.random.choice(list(directions.keys()))
	direction = directions[dkey]
	x = x0+direction[0]
	y = y0+direction[1]

	flag = (x,y) in list(AA_dict.keys())
	flag = flag or (x == -1 or x == N)
	flag = flag or (y == -1 or y == N)

	AA_dict_copy = dict(AA_dict)
	del AA_dict_copy[(x0,y0)]
	AA_dict_copy[(x,y)] = AA_dict[(x0,y0)]
	newContacts = getContacts((x,y),AA_dict_copy)
	if not all([ww in newContacts for ww in bonds]):
		flag = 1

	return (x,y) if flag == 0 else (x0,y0)

def Metropolis(AA_dict, myAA_dict):
	E0 = energy(AA_dict)
	Eprime = energy(myAA_dict)

	return 1 if rand(0,1) < boltzmann(Eprime-E0) else 0

def eed(AA_dict):

	first = 0
	last = N-1
	for key in list(AA_dict.keys()):
		if AA_dict[key] == first:
			x0 = np.array(key)
		elif AA_dict[key] == last:
			xn = np.array(key)

	return np.linalg.norm(xn-x0)

def gyration(AA_dict):

	X = [p[0] for p in list(AA_dict.keys())]
	Y = [p[1] for p in list(AA_dict.keys())]

	return var(X) + var(Y)

class plot:

	def getBond(self,i):
		for key1 in list(AA_dict.keys()):
			if AA_dict[key1] == i: break

		for key2 in list(AA_dict.keys()):
			if AA_dict[key2] == i+1: break

		X = np.linspace(key1[0],key2[0],2)
		Y = np.linspace(key1[1],key2[1],2)

		return X,Y

	def getCoordinates(self):
		# NOTE: zip(*list) is equivalent to unzip()
		#return zip(*AA_dict.keys() )
		return unzip(AA_dict.keys() )

	def __init__(self):
		fig = pp.figure()
		self.ax = fig.gca()
		self.ax.set_xticks([])
		self.ax.set_yticks([])
		axlim = 1.5*eed(AA_dict)
		self.ax.set_xlim(-axlim,axlim)
		self.ax.set_ylim(-axlim,axlim)
		pp.axis('off')
		pp.ion()
		X,Y = self.getCoordinates()
		self.line = pp.plot(X,Y,marker='o',color='b',ls='',ms=5)[0]
		self.BondLines = []
		self.textPos = 0.7*axlim
		text = 't = 0, T = %.2f'%T
		self.text = self.ax.text(self.textPos,self.textPos,text)
		for i in range(N-1):
			X,Y = self.getBond(i)
			self.BondLines.append(pp.plot(X,Y,color='k',lw=1.5)[0])

	def update(self,t,T):
		X,Y = self.getCoordinates()
		self.line.set_xdata(X)
		self.line.set_ydata(Y)
		for i in range(N-1):
			X,Y = self.getBond(i)
			self.BondLines[i].set_xdata(X)
			self.BondLines[i].set_ydata(Y)

		self.text.remove()
		text = 't = %s, T = %.2f'%(t,T)
		self.text = self.ax.text(self.textPos,self.textPos,text)
		pp.draw()
		pp.pause(0.00001)

	def SaveFinalImage(self):
		pp.savefig("protein_2D.png")

Energy = [ 0.0 ]
EED = [ eed(AA_dict) ]
radGyr = [gyration(AA_dict) ]

# Monte-Carlo

step = 0
movie = plot()
while step < Nsteps:
	# Choose a random site
	print('step {0} of {1} '.format(step, Nsteps) )
	site = random.choice(list(AA_dict.keys()))
	resid = AA_dict[site]
	T = Tvals[step]

	# Find valid conformation
	x,y = move_AA(*site)
	AA_dict_new = dict(AA_dict)
	del AA_dict_new[site]
	AA_dict_new[(x,y)] = resid

	if AA_dict != AA_dict_new:
		#Metropolis acceptance criteria
		if Metropolis(AA_dict, AA_dict_new):
			AA_dict = AA_dict_new

	step += 1

	if step % fs == 0:
		Energy.append(energy(AA_dict) )
		EED.append(eed(AA_dict) )
		radGyr.append(gyration(AA_dict) )
		movie.update(step, T)

movie.SaveFinalImage()

TS = range(0,Nsteps+1,fs)
pp.subplot(3,1,1)
pp.plot(TS,Energy)
pp.ylabel('Energy')

pp.subplot(3,1,2)
pp.plot(TS,EED)
pp.ylabel('end-to-end distance')

pp.subplot(3,1,3)
pp.plot(TS,radGyr)
pp.ylabel('radius of gyration')

pp.xlabel('Timestep')
pp.show()
