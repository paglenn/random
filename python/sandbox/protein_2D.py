# Lattice protein folding from primary structure
# initial conformation created using self-avoiding random walk
# usage python protein_2D.py [Temperature=10]
# Paul Glenn
import numpy as np
import random
import math
import matplotlib.pyplot as pp
from sys import argv
import time
import statistics as stat
import copy

# user defined modules
from random_walk_2D_SA import SAW
# from lattice_step import random_step
randn = random.randint
rand  = random.uniform
exp = math.exp

###################################
# Definitions
# Initialize primary struct
global N, struct

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
print('Temperature: %.2f'%T)
boltzmann = lambda dE: exp(-dE/T)

struct = SAW(chainLength)

def getBondsList(site,mystruct = struct):
	resid = mystruct.index(site)
	bondsList = list()
	if resid != 0: bondsList.append(resid-1)
	if resid != N-1: bondsList.append(resid+1)

	return bondsList

def getContacts(site,mystruct = struct):
	i,j = site
	contacts = []

	nnSites = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]
	for nnSite in nnSites:
		if nnSite in mystruct: contacts.append(mystruct.index(nnSite))
	return contacts

def energy(mystruct = struct):
	E = 0.
	for pair in mystruct:

		contacts = getContacts(pair,mystruct)

		bondsList = getBondsList(pair,mystruct)

		for bonded in bondsList: contacts.remove(bonded)

		resName = PProtein[mystruct.index(pair)]

		for NB in contacts:
			contactResName = PProtein[NB]
			E += J[contactResName,resName]

	return E



def move_AA(x0,y0):
	site = (x0,y0)
	bonds = getBondsList(site,struct)
	x = x0
	y = y0

	directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
	dkey = random.choice(range(4))

	direction = directions[dkey]
	x = x0+direction[0]
	y = y0+direction[1]

	flag = (x,y) in struct
	flag = flag or (x == -1 or x == N)
	flag = flag or (y == -1 or y == N)

	struct_copy = copy.copy(struct)
	struct_copy.remove(site)
	struct_copy.insert(struct.index(site),(x,y))
	newContacts = getContacts((x,y),struct_copy)
	if not all([ww in newContacts for ww in bonds]):
		flag = 1

	return (x,y) if flag == 0 else (x0,y0)

def Metropolis(struct, mystruct):
	E0 = energy(struct)
	Eprime = energy(mystruct)

	return 1 if rand(0,1) < boltzmann(Eprime-E0) else 0

def eed(struct):

	x0 = np.array(struct[0] )
	xn = np.array(struct[-1] )

	return np.linalg.norm(xn-x0)

def gyration(struct):
	var = stat.variance
	X = [p[0] for p in struct]
	Y = [p[1] for p in struct]
	print(X,Y)

	return var(X) + var(Y)

Energy = [ 0.0 ]
EED = [ eed(struct) ]
radGyr = [gyration(struct) ]

# Monte-Carlo
step = 0
while step < Nsteps:
	# Choose a random site
	site = random.choice(struct)
	resid = struct.index(site)

	# Find valid conformation
	x,y = move_AA(*site)
	newStructure = copy.copy(struct)
	newStructure.remove(site)
	newStructure.insert(struct.index(site),(x,y))

	if struct != newStructure:
		#Metropolis acceptance criteria
		if Metropolis(struct, newStructure):
			struct = newStructure

	step += 1

	if step % fs == 0:
		Energy.append(energy(struct) )
		EED.append(eed(struct) )
		radGyr.append(gyration(struct) )

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
