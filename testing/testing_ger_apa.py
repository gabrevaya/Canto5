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


#def envolvente(raw_audio,times,sample_rate,data_points,bin_size=100,mean=0):

def envolvente(raw_audio,times,sample_rate,data_points=None,bin_size=None,mean=0):
    """
    Finds a wrapping-signal of a raw-audio wave, dividing the set of pints in packages of a 
    given number of points (bin_size), and computing the max or mean value of the signal in 
    each one of them.

    Input: raw_audio, timebase, sample rate and total number of data points of the audio file,
           (output of read_wav.py executed on a single file). (Optional): specify bin_size 
           (=100 by default); specify if you want to consider the  maximum (mean=0, default) 
           or mean (mean=1) value of the data points in bin_size. 
    Output: resultant wrapping-signal
    """
    if data_points is None:
        data_points=len(times)
    
    if bin_size is None:
        bin_size=data_points/1e3
    
    #[sample_rate, raw_audio] = sw.read(file)
    #raw_audio = np.array(raw_audio)
    #data_points = len(raw_audio)
    t_fin = data_points/sample_rate
    #times = np.arange(0,t_fin,1/sample_rate)

    #peakind = signal.find_peaks_cwt(raw_audio, np.arange(1,5))
    #pospeakind = [i for i in peakind if raw_audio[i] > 0]
    #peaks = np.zeros(len(raw_audio)) 
    #peaks[pospeakind] = raw_audio[pospeakind]

    #bin_size = 100
    num_of_bins = int(data_points/bin_size)
    new_len = num_of_bins*bin_size
    
    segmented = np.reshape(raw_audio[:new_len],[num_of_bins,bin_size])
    
    if mean==1:
        smooth_wave = np.mean(np.abs(segmented), axis = 1)
    else:
        smooth_wave = np.max(segmented, axis = 1)
    
    t_start = int((bin_size*0.5))-1
    t_new = times[t_start:new_len:bin_size]
    
    tck = interpolate.splrep(t_new, smooth_wave, s=0)
    envolvente = interpolate.splev(times, tck, der=0)
    
    plt.figure(figsize=(30,10))
    plt.plot(times,raw_audio)
    #plt.plot(t_new,smooth_wave)
    plt.plot(times, envolvente, linewidth=3)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    #plt.plot(times,peaks,'.')
    
    #return
    pass
