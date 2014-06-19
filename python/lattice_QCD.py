
def S(j,x):
	jp = (j+1)%N
	jm = (J+1)%N
	return 0.5*a*x[j]**2. + x[j]*(x[j]-x[jp]-x[jm])/a

def update(x):
	from random import uniform
	for j in range(0,N):
		old_x = x[j]
		old_Sj =S(j,x)
		x[j] += uniform(-eps,eps)	#update x[j]
		dS = S(j,x) - old_Sj		#change in action
		if dS >0 and exp(-dS) < uniform(0,1):
			x[j] = old_x 			# rejection criteria

def compute_G(x,n):
	g = 0
	for j in range(0,N):
		g += x[j]*x[(j+N)%N]
	return g/N

def MCaverage(x,G):
	for j in range(0,N): 			#initialize x
		x[j] = 0
	for j in range(0,5*N_cor):
		update(x)
	for alpha in range(0,N_cf):

