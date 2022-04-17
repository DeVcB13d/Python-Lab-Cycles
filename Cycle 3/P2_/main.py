"""
Implement Principle Component Analysis(PCA) of a matrix.
Reference :
http://kiwi.bridgeport.edu/cpeg540/PrincipalComponentAnalysis_Tutorial.pdf
"""

import numpy as np

M = np.random.randint(-9,10,size = (3,3))
print(M)

#Getting the mean of each column
Mean_matrix = np.mean(M, axis=0)
# center columns by subtracting column means
Cen = M - Mean_matrix
print(Cen)
# calculate covariance matrix of centered matrix
V = np.cov(Cen.T)
# eigendecomposition of covariance matrix
values, vectors = np.linalg.eig(V)
projection_matrix = (vectors.T[:][:2]).T
# project data
P = projection_matrix.T.dot(Cen.T)
print(P.T)