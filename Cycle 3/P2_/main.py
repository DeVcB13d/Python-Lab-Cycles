"""
Implement Principle Component Analysis(PCA) of a matrix.
Reference :
http://kiwi.bridgeport.edu/cpeg540/PrincipalComponentAnalysis_Tutorial.pdf
"""

import numpy as np


#Generating a random 3X3 matrix
M = np.random.randint(1,10,size = (3,3))
print(M)

def PCA(A):
    #Get the mean values of each column
    Mean = np.mean(A.T,axis = 1)
    print(Mean)
    #Centering the columns
    Center = A - Mean
    print(Center)
    #Calculating the covaraince matrix
    V = np.cov(Center.T)
    print("Cov = \n")
    print(V)
    #Eigendecomposition of covariance matrix
    values,vectors = np.linalg.eig(V)
    print()
    print(vectors)
    print()
    print(values)
    print()
    P = vectors.T.dot(Center.T)
    print(P.T)
PCA(M)