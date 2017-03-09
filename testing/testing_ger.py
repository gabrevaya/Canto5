# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:34:20 2017

@author: ger
"""



import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile as sw
from scipy import signal
from scipy import interpolate

file = '/home/ger/Dropbox/Cursos/Workshop de Técnicas de Progamación Científica/Canto5/datos/albanella/call1.wav'
[sample_rate, raw_audio] = sw.read(file)
raw_audio = np.array(raw_audio)
data_points = len(raw_audio)
t_fin = data_points/sample_rate
times = np.arange(0,t_fin,1/sample_rate)



#peakind = signal.find_peaks_cwt(raw_audio, np.arange(1,5))
#pospeakind = [i for i in peakind if raw_audio[i] > 0]
#peaks = np.zeros(len(raw_audio))
#peaks[pospeakind] = raw_audio[pospeakind]

bin_size = 100
num_of_bins = int(data_points/bin_size)
new_len = num_of_bins*bin_size

segmented = np.reshape(raw_audio[:new_len],[num_of_bins,bin_size])
maxs = np.max(segmented, axis = 1)
#maxs = np.mean(np.abs(segmented), axis = 1) # cambiando maximo por valor medio, para separar sílabas
t_start = int((bin_size*0.5))-1
t_new = times[t_start:new_len:bin_size]

tck = interpolate.splrep(t_new, maxs, s=0)
envolvente = interpolate.splev(times, tck, der=0)

plt.figure(figsize=(30,10))
plt.plot(times,raw_audio)
#plt.plot(t_new,maxs)
plt.plot(times, envolvente, linewidth=3)
plt.xlabel('tiempo (s)')
plt.ylabel('amplitud')
#plt.plot(times,peaks,'.')
