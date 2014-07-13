# Lattice protein folding from chosen primary structure
# TO DO: SAW instead
# Paul Glenn
from matplotlib import pyplot as pp
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pylab
import numpy as np
import random
import math
import itertools as it

global AA_dict
randn = random.randint
rand  = random.uniform
exp = math.exp

###################################
# Initialize primary structure -- suppose alphabetical ordering for fun
N = chainLength = 30
NAA = 20
PProtein = [randn(0,NAA-1) for x in range(N) ]
# Interaction matrix J
J = np.random.choice(np.linspace(-4,-2,1000),(NAA,NAA))
# Set thermodynamic settings
T = 100. # energy scale in units of k_B
boltzmann = lambda dE: exp(-dE/T)

#align sites along x direction
AA_sites = zip(range(N), N*[int(N/2)],N*[int(N/2)])
AA_dict = dict(zip(AA_sites,range(N)))

def getBondsList(site,myAA_dict = AA_dict):
	resid = myAA_dict[site]
	bondsList = list()
	if resid != 0: bondsList.append(resid-1)
	if resid != N-1: bondsList.append(resid+1)

	return bondsList

def getContacts(site,myAA_dict = AA_dict):
	i,j,k = site
	contacts = []

	nnSites = [(i+1,j,k),(i-1,j,k),(i,j+1,k),(i,j-1,k),(i,j,k+1),(i,j,k-1) ]
	for nnSite in nnSites:
		if nnSite in myAA_dict.keys(): contacts.append(myAA_dict[nnSite])
	return contacts

def energy(myAA_dict = AA_dict):
	E = 0.
	for site in myAA_dict.keys():

		contacts = getContacts(site,myAA_dict)

		bondsList = getBondsList(site,myAA_dict)

		for bonded in bondsList: contacts.remove(bonded)

		resName = PProtein[myAA_dict[site]]

		for NB in contacts:
			contactResName = PProtein[NB]
			E += J[contactResName,resName]

	return E

def move_AA(x0,y0,z0,myAA_dict):

	site = (x0,y0,z0)
	bonds = getBondsList(site,AA_dict)
	x = x0
	y = y0
	z = z0

	directions = [(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0)]
	directions.extend([(0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1)] )
	directions.extend([(1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1)] )
	random.shuffle(directions)
	successful_move = 0
	for direction in directions:
		x = x0 + direction[0]
		y = y0 + direction[1]
		z = z0 + direction[2]
		if (x,y,z) in AA_dict.keys(): continue
		if x == -1 or x == N: continue
		if y == -1 or y == N: continue
		if z == -1 or z == N: continue

		AA_dict_copy = dict(AA_dict)
		del AA_dict_copy[site]
		AA_dict_copy[(x,y,z)] = resid
		newContacts = getContacts((x,y,z),AA_dict_copy)
		if not all([ww in newContacts for ww in bonds]): continue

		successful_move = 1
		break

	if not successful_move:
		x = x0
		y = y0
		z = z0

	return x,y,z

def Metropolis(AA_dict, myAA_dict):
	E0 = energy(AA_dict)
	Eprime = energy(myAA_dict)
	dE = Eprime - E0
	p = boltzmann(dE)
	return 1 if p > rand(0,1) else 0

def init_plot():
	global line, bondLines
	fig = pp.figure(figsize=(10,8))
	ax = Axes3D(fig)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.set_xlim(-1,N+1)
	ax.set_ylim(0,3*N/2)
	ax.set_zlim(0,3*N/2)
	pp.axis('off')
	pp.ion()
	X,Y,Z =  zip(*AA_dict.keys() )
	line, = pp.plot(X,Y,zs= Z,marker='o',color='b',ls='',ms=5)
	bondLines = []
	for k in range(N-1):
		pos = int(N/2)
		X = np.linspace(k, k+1,5)
		Y = np.linspace(pos,pos,5)
		Z = np.linspace(pos,pos,5)
		bondLines.append(pp.plot(X,Y,zs=Z,color='b',lw=1.5)[0])

def update_plot():
	global line, bondLines
	line.set_xdata(zip(*AA_dict.keys())[0])
	line.set_ydata(zip(*AA_dict.keys())[1])
	line.set_3d_properties(zip(*AA_dict.keys())[2])

	for i in range(N-1):
		for key1 in AA_dict.keys():
			if AA_dict[key1] == i: break

		for key2 in AA_dict.keys():
			if AA_dict[key2] == i+1 : break

		X = np.linspace(key1[0],key2[0],5)
		Y = np.linspace(key1[1],key2[1],5)
		Z = np.linspace(key1[2],key2[2],5)
		bondLines[i].set_xdata(X)
		bondLines[i].set_ydata(Y)
		bondLines[i].set_3d_properties(Z)

	pp.draw()
	pp.pause(0.00001)

####################################
# Monte-Carlo steps
Nsteps = int(5000)
step = 0
init_plot()
while step < Nsteps:
	# Choose a random site
	site = random.choice(AA_dict.keys())
	resid = AA_dict[site]

	# Find valid conformation
	x,y,z = move_AA(*site,myAA_dict = AA_dict)
	AA_dict_new = dict(AA_dict)
	del AA_dict_new[site]
	AA_dict_new[(x,y,z)] = resid
	if AA_dict == AA_dict_new: continue

	#Metropolis acceptance criteria
	if Metropolis(AA_dict, AA_dict_new):
		AA_dict = AA_dict_new

		update_plot()

	step += 1

