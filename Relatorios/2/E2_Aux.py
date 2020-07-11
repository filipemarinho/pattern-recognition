import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.datasets import mnist
from sklearn.cluster import KMeans
from sklearn import datasets
from scipy.spatial.distance import cdist
from collections import Counter
import tensorflow as tf
from sklearn.model_selection import train_test_split



    

#matriz de adjacencia W
def Adj_matrix(data):
    n = len(data[0])
    W = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            # a distancia de um nó com ele mesmo é zero, portanto:
            if i!=j:
                d = np.sum([(data[row][i]-data[row][j])**2 for row in range(len(data))])
                d = 1/(np.sqrt(d)+0.0001) # para evitar divisões por zero
                W[i,j] = d
    return W

# Matriz de grau D
def Degree_matrix(W):
    D = np.zeros(W.shape)
    for i in range(len(W)):
        D[i,i] = np.sum(W[i,:])
    return D
