"""
Implement Principle Component Analysis(PCA) of a matrix.
Reference :
http://kiwi.bridgeport.edu/cpeg540/PrincipalComponentAnalysis_Tutorial.pdf
"""

import numpy as np
from random import randint as Rint



def PCA(A):
    print("INPUT MATRIX : ")
    print(A)
    #Get the mean values of each column
    Mean = np.mean(A.T,axis = 1)
    print("MEAN OF EACH COLUMN : "  )
    print(Mean)
    #Centering the columns
    Center = A - Mean
    print("CENTERING THE MATRIX : ")
    print(Center)
    #Calculating the covaraince matrix
    V = np.cov(Center.T)
    print("COVARIANCE MATRIX : ")
    print(V)
    #Eigendecomposition of covariance matrix
    values,vectors = np.linalg.eig(V)
    print("EIGENVECTORS")
    print(vectors)
    print("EIGENVALUES")
    print(values)
    print("TAKING DOT PRODUCT AND PROJECTION")
    P = vectors.T.dot(Center.T)
    proj = (vectors.T[:][:2]).T
    print(proj)
    # projecting the data
    P = proj.T.dot(Center.T)
    return P

def main():
    #Generating a random 3X3 matrix
    M = np.random.randint(1,10,size = (2,2))
    P = PCA(M)
    print("RESULT : ")
    print(P)
    print("ROUNDING : ")
    for i in P :
        for j in i:
            print(round(j,2),end="\t")
        print("\n")
main()