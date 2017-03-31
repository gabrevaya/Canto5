# -*- coding: utf-8 -*-
"""
Function to Principal component analysis 
input : syllables
output: acp.components_
"""


from sklearn.decomposition import PCA

def pca_syll(file):
    acp = PCA(n_components=4)
    acp.fit(file)
    return acp.components_        
