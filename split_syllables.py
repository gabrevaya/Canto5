# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:12:41 2017

@author: ger
"""

def split_syllables(signal, boo, margin):

'''
Use a boolean mask signal to split the signal.

input: signal (numpy array), boo (boolean array), margin (int)
output: syllables(list of numpy arrays)

'''

# find the indexes when the boolean array changes
indices = np.nonzero(boo[1:] != boo[:-1])[0] + 1

# extend the segments of syllables with a given margin
# if the signal starts with a syllable:
if boo[0]:
    ind[0::2] = indices[0::2] + margen 
    ind[1::2] = indices[1::2] - margen
    
# if the signal doesn't starts with a syllable
else:
    ind[0::2] = indices[0::2] - margen
    ind[1::2] = indices[1::2] + margen 
    
# split the signal
b = np.split(signal, indices)

# keep only the syllables and not the intermediate parts
b = b[0::2] if boo[0] else b[1::2]

return b

