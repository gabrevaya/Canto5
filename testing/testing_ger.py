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
[sample_rate, audio] = sw.read(file)
audio = np.array(audio)
data_points = len(audio)
t_fin = data_points/sample_rate
times = np.arange(0,t_fin,1/sample_rate)



#peakind = signal.find_peaks_cwt(audio, np.arange(1,5))
#pospeakind = [i for i in peakind if audio[i] > 0]
#peaks = np.zeros(len(audio))
#peaks[pospeakind] = audio[pospeakind]

bin_size = 10
num_of_bins = int(data_points/bin_size)
new_len = num_of_bins*bin_size

segmented = np.reshape(audio[:new_len],[bin_size, num_of_bins])
maxs = np.max(segmented, axis = 0)
t_start = int((bin_size*0.5))-1
t_new = times[t_start:new_len:bin_size]

tck = interpolate.splrep(t_new, maxs, s=0)
envolvente = interpolate.splev(times, tck, der=0)

# NO FUNCIONA LO DE LA ENVOLVENTE POR AHORA

plt.figure(figsize=(30,10))
plt.plot(times,audio)
#plt.plot(t_new,maxs)
plt.plot(times, envolvente)
plt.xlabel('tiempo (s)')
plt.ylabel('amplitud')
#plt.plot(times,peaks,'.')
