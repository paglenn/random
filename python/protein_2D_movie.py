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
# from lattice_step import random_step
randn = random.randint
rand  = random.uniform
exp = math.exp

###################################
# Definitions
# Initialize primary structure
global N, AA_dict

N = chainLength = 15
#PProtein = [randn(0,19) for x in range(N) ]
PProtein = np.random.randint(0,19,N)
# Interaction matrix J
J = np.random.choice(np.linspace(-4,-2,1000),(20,20))
# Set thermodynamic settings
T = 1.0 # Temperature
argc = len(argv)
if argc == 1: T = 1
else: T = int( argv[1] )
print 'Temperature: ', T
boltzmann = lambda dE: exp(-dE/T)

AA_sites = SAW(chainLength)
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
		if nnSite in myAA_dict.keys(): contacts.append(myAA_dict[nnSite])
	return contacts

def energy(myAA_dict = AA_dict):
	E = 0.
	for pair in myAA_dict.keys():

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

	directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
	#directions = [(1,0),(0,-1),(-1,0),(0,1)]
	random.shuffle(directions)
	successful_move = 0
	for direction in directions:
		x = x0 + direction[0]
		y = y0 + direction[1]
		flag = (x,y) in AA_dict.keys()
		flag = flag or (x == -1 or x == N)
		flag = flag or (y == -1 or y == N)
		if flag: continue
		if (x,y) in AA_dict.keys(): continue
		if x == -1 or x == N: continue
		if y == -1 or y == N: continue
		AA_dict_copy = dict(AA_dict)
		del AA_dict_copy[site]
		AA_dict_copy[(x,y)] = resid
		newContacts = getContacts((x,y),AA_dict_copy)
		if not all([ww in newContacts for ww in bonds]): continue

		successful_move = 1
		break
	if not successful_move:
		x = x0
		y = y0

	return x,y
'''

def check_move(oldSite,newSite):

	oldBonds = getBondsList(oldSite,AA_dict)

	AA_dict_copy = dict(AA_dict)
	AA_dict_copy[newSite] = AA_dict_copy.pop(oldSite)
	newContacts = getContacts(newSite, AA_dict_copy)

	flags = []
	flags.append(newSite in AA_dict.keys())
	flags.append(-1 in newSite or N in newSite)
	flags.append(not all([ww in newContacts for ww in oldBonds]) )

	PathIsGood = all([f == False for f in flags] )

	return	PathIsGood
'''




def Metropolis(AA_dict, myAA_dict):
	E0 = energy(AA_dict)
	Eprime = energy(myAA_dict)

	return 1 if rand(0,1) < boltzmann(Eprime-E0) else 0

def init_plot():
	global pointSet, bondLines

	fig = pp.figure()
	ax = fig.gca()
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_xlim(-N-1,N+1)
	ax.set_ylim(-(N+1),N+1)
	pp.ion()
	pointSet, = pp.plot(*zip(*AA_dict.keys()),ls='',marker='o',color='k')
	pp.xticks([])
	pp.yticks([])
	bondLines = []
	for i in range(N-1):
		for key1 in AA_dict.keys():
			if AA_dict[key1] == i: break

		for key2 in AA_dict.keys():
			if AA_dict[key2] == i+1 : break

		X = np.linspace(key1[0],key2[0],5)
		Y = np.linspace(key1[1],key2[1],5)
		bondLines.append( pp.plot(X,Y,color='k',lw=2)[0] )

# Monte-Carlo
Nsteps = int(2e5)
step = 1
init_plot()
while step < Nsteps:
	# Choose a random site
	site = random.choice(AA_dict.keys())
	resid = AA_dict[site]

	# Find valid conformation
	x,y = move_AA(*site)
	AA_dict_new = dict(AA_dict)
	del AA_dict_new[site]
	AA_dict_new[(x,y)] = resid
	step += 1

	#Metropolis acceptance criteria
	if Metropolis(AA_dict, AA_dict_new):
		AA_dict = AA_dict_new


	update_plot(AA_dict)

