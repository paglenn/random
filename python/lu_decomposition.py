# implement Crout's algorithm for decomposing a matrix
import numpy as np

def factorLU(A):
    '''factorLU(square matrix A) '''
    B = np.zeros(A.shape)
    C = np.zeros(A.shape)
    for i in range(A.shape[0]): B[i,i] = 1

    #C[0,:] = A[0,:]
    #B[:,0] = A[:,0]/C[0,0]

    for j in range(A.shape[0]):
        C[0,j] = A[0,j]
        for i in range(1,j):
            C[i,j] = A[i,j]
            for k in range(i-1):
                C[i,j] -= B[i,k]*C[k,j]
        C[j,j] = A[j,j]
        for k in range(j-1):
            C[j,j] -= B[j,k]*C[k,j]

        for i in range(j+1,A.shape[0]):
            B[i,j] = A[i,j]/C[j,j]
            for k in range(i-1):
                B[i,j] -= B[i,k]*C[k,j] / C[j,j]

    return B,C



A = np.ones((4,4))
print('L:')
print(factorLU(A)[0])
print('U:')
print(factorLU(A)[1])
myL,myU = factorLU(A)
from scipy.linalg import lu
P,L,U = lu(A)
print('L:')
print(L)
print('U:')
print(U)
print(np.dot(myL,myU))


