# -*- coding: utf-8 -*-
"""
Function to classify the syllables by the method  k-means  &  scatterplot

input : syllables
output: clusters, graphics scatterplot

"""
import numpy as np
import matplotlib.pyplot as plt
from cluster import KMeansClustering
from mpl_toolkits.mplot3d import Axes3D

def plot_cluster_syll(file):
    cl = KMeansClustering(file)
    clusters = cl.getclusters(3)


# crete list for class

    cla = []
    t=-1
    for i in file:
        t = t + 1
        f = 0
        for xx in range(0, 3):
            cant = len(clusters[xx])
            for yy in range(0,cant):        
                if file[t] == clusters[xx][yy] and f == 0:
                    f = 1
                    cla.append(xx)

# Plot  axes 0, 1, 2

    np.random.seed(5)

    centers = [[1, 1], [-1, -1], [1, -1]]

    X = np.asarray(file)

    y = np.asarray(cla)

    fignum = 1
    fig = plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    
    plt.cla()
    
    for name, label in [('Syll set 1', 0),
                        ('Syll set 2', 1),
                        ('Syll set 3', 2)]:
                            ax.text3D(X[y == label, 3].mean(),
                                      X[y == label, 0].mean() + 1.5,
                  X[y == label, 2].mean(), name,
                  horizontalalignment='center',
                  bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
                  
                  
                  
# Reorder the labels to have colors matching the cluster results

    y = np.choose(y, [1, 2, 0]).astype(np.float)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
    
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('f 1')
    ax.set_ylabel('f 2')
    ax.set_zlabel('f 3')
    
    return clusters
    
    plt.show()
