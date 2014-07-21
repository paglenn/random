# Paul Glenn -- 14 July 2014
# Lattice protein folding from chosen primary structure
# usage: python protein_3D_movie.py [initial temperature]
# note : temperature in units of k_B
from matplotlib import pyplot as pp
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pylab
import numpy as np
import random
import math
from sys import argv

##########################
#User-defined macros
from random_walk_3D_SA import SAW
global AA_dict
randn = random.randint
rand  = random.uniform
exp = math.exp

###################################
# Parameters
N = chainLength = 15
NAA = 20
Nsteps = int(5e5)
argc = len(argv) - 1
if argc == 0: T = 100.
else: T = float(argv[1])
Tvals = np.linspace(T,0.01,Nsteps)
boltzmann = lambda dE: exp(-dE/T)
J = -1*np.ones((NAA,NAA) )
#J = np.random.choice(np.linspace(-4,-2,100),(NAA,NAA))

####################################
# Initial Conditions
PProtein = [randn(0,NAA-1) for x in range(N) ]

#AA_sites = zip(range(N), N*[int(N/2)],N*[int(N/2)])
AA_sites = SAW(chainLength)
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

def EED(AA_dict):

	first = 0
	last = N - 1
	for key in AA_dict.keys():
		if AA_dict[key] == first: x0 = np.array(key)
		elif AA_dict[key] == last: xn = np.array(key)

	return np.linalg.norm(xn-x0)

class plot:

	def getBond(self,i):
		for key1 in AA_dict.keys():
			if AA_dict[key1] == i: break

		for key2 in AA_dict.keys():
			if AA_dict[key2] == i+1: break

		X = np.linspace(key1[0],key2[0],2)
		Y = np.linspace(key1[1],key2[1],2)
		Z = np.linspace(key1[2],key2[2],2)

		return X,Y,Z

	def getCoordinates(self):
		# NOTE: zip(*list) is equivalent to unzip()
		return zip(*AA_dict.keys() )

	def __init__(self):
		fig = pp.figure()
		self.ax = Axes3D(fig)
		self.ax.set_xticks([])
		self.ax.set_yticks([])
		self.ax.set_zticks([])
		axlim = 1.5*EED(AA_dict)
		self.ax.set_xlim(-axlim,axlim)
		self.ax.set_ylim(-axlim,axlim)
		self.ax.set_zlim(-axlim,axlim)
		pp.axis('off')
		pp.ion()
		X,Y,Z = self.getCoordinates()
		self.line = pp.plot(X,Y,zs= Z,marker='o',color='b',ls='',ms=5)[0]
		self.BondLines = []
		self.textPos = 0.7*axlim
		text = 't = 0, T = %.2f'%T
		self.text = self.ax.text(self.textPos,self.textPos,self.textPos,text)
		for i in range(N-1):
			X,Y,Z = self.getBond(i)
			self.BondLines.append(pp.plot(X,Y,zs=Z,color='k',lw=1.5)[0])

	def update(self,t,T):
		X,Y,Z = self.getCoordinates()
		self.line.set_xdata(X)
		self.line.set_ydata(Y)
		self.line.set_3d_properties(Z)
		for i in range(N-1):
			X,Y,Z = self.getBond(i)
			self.BondLines[i].set_xdata(X)
			self.BondLines[i].set_ydata(Y)
			self.BondLines[i].set_3d_properties(Z)

		self.text.remove()
		text = 't = %s, T = %.2f'%(t,T)
		self.text = self.ax.text(self.textPos,self.textPos,self.textPos,text)
		pp.draw()
		pp.pause(0.00001)

	def SaveFinalImage(self):
		pp.savefig("protein_3D.png")

####################################
# Monte-Carlo loop
step = 0
movie = plot()
while step < Nsteps:
	# Choose a random site
	site = random.choice(AA_dict.keys())
	resid = AA_dict[site]
	T = Tvals[step]

	# Find valid conformation
	x,y,z = move_AA(*site,myAA_dict = AA_dict)
	AA_dict_new = dict(AA_dict)
	del AA_dict_new[site]
	AA_dict_new[(x,y,z)] = resid
	if AA_dict == AA_dict_new: continue

	#Metropolis acceptance criteria
	if Metropolis(AA_dict, AA_dict_new):
		AA_dict = AA_dict_new
		if step%10 == 0:
			movie.update(step,T)

	step += 1

movie.SaveFinalImage()

