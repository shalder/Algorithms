#!/usr/local/bin/python

from numpy import *
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

#hardcoding np array 
#X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
c="/Users/buta/Desktop/scripts/PCA/pca_train_file.txt"
#loading np array from a file
X_file = loadtxt(c, delimiter=',')
print X_file
normed_matrix = normalize(X_file, axis=1, norm='l1')
#print normed_matrix
pca = PCA(n_components=2)
#pca.fit(X)
pca.fit(normed_matrix)
PCA(copy=True, n_components=2, whiten=False)
#print(pca.explained_variance_ratio_)
f=pca.components_[0]
print f
