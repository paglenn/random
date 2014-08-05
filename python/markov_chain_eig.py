import numpy as np
T = np.zeros((5,5))
T[0] = [0,0.6,0.4,0,0]
T[1] = [0.8,0,0,0.2,0]
T[2] = [0.5,0.3,0,0,0.2]
T[3] = [0,0,0,1,0]
T[4] = [0,0,0,0,1]
w, V = np.linalg.eig(T)
#print(T)
print(np.dot(V.T,V))
quit()
for i in range(5):
	#print(w[i],V[:,i])
	print(w[i],V[i])

