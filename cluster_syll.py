# -*- coding: utf-8 -*-
"""
Function to classify the syllables by the method k-means
input : syllables
output: clusters

"""
from cluster import KMeansClustering

def cluster_syll(file):
    cl = KMeansClustering(file)
    clusters = cl.getclusters(3)
    return clusters
# 
