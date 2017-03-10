# -*- coding: utf-8 -*-
 
#from read_wav.py import read_wav
#from testing_ger_apa.py import envolvente
#from testing_split.py import silabas

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sw
from scipy import signal
from scipy import interpolate

audio_file="call1.wav"

def read_wav(audio_file):
    
    '''
    Read wav files.
    
    Input: file path.
    Output: raw audio amplitudes, corresponding times, sample rate, number of
    samples.
    '''    
    
    [sample_rate, raw_audio] = sw.read(audio_file)
    raw_audio = np.array(raw_audio)
    n_samples= len(raw_audio)
    t_fin = n_samples/sample_rate
    times = np.arange(0,t_fin,1/sample_rate)
    
    #plt.figure(figsize=(30,10))
    plt.plot(times,raw_audio)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.show()
    
    return raw_audio, times, sample_rate, n_samples
 
[raw_audio, times, sample_rate, data_points]=read_wav(audio_file)
 

def envolvente(raw_audio, times, sample_rate, data_points=None, bin_size=None, mean=0, der=0):
    """
    Finds a wrapping-signal of a raw-audio wave, dividing the set of pints in packages of a 
    given number of points (bin_size), and computing the max or mean value of the signal in 
    each one of them.

    Input: raw_audio, timebase, sample rate and total number of data points of the audio file,
           (output of read_wav.py executed on a single file). (Optional): specify bin_size 
           (=100 by default); specify if you want to consider the  maximum (mean=0, default) 
           or mean (mean=1) value of the data points in bin_size; specify if you want to 
           derivate the signal setting der=1 (0 by default).
    Output: resultant wrapping-signal
    """
    if data_points is None:
        data_points=len(times)
    
    if bin_size is None:
        bin_size=int(data_points/1e3)
    
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
    envolv = interpolate.splev(times, tck, der)
    
    #plt.figure(figsize=(30,10))
    plt.plot(times,raw_audio)
    #plt.plot(t_new,smooth_wave)
    plt.plot(times, envolv, linewidth=3)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    #plt.plot(times,peaks,'.')
    plt.show()
    
    return envolv, times
 
[env, t_env]=envolvente(raw_audio, times, sample_rate, data_points, 2500, 1, 0)

n_umbral=100

umbral=abs(np.max(env[:n_umbral]))

#print ("umbral=",umbral)

fbird=0.1

loc_silabas=np.greater(env,umbral*fbird)

plt.plot(times,raw_audio)
plt.plot(t_env, env, linewidth=3)
plt.plot(t_env,loc_silabas*10000)
plt.xlabel('tiempo (s)')
plt.ylabel('amplitud')

plt.show()

loc_index=np.diff(loc_silabas)

plt.plot(loc_index)

plt.show()

	    
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
        indices[0::2] = indices[0::2] + margin 
        indices[1::2] = indices[1::2] - margin
    
    # if the signal doesn't starts with a syllable
    else:
        indices[0::2] = indices[0::2] - margin
        indices[1::2] = indices[1::2] + margin 
    
    # split the signal
    b = np.split(signal, indices)

    # keep only the syllables and not the intermediate parts
    b = b[0::2] if boo[0] else b[1::2]

    return b	

silabas=split_syllables(raw_audio, loc_silabas, 50)
time_windows=split_syllables(times, loc_silabas, 50)

time_windows[0]=time_windows[0]-np.min(time_windows[0])
time_windows[1]=time_windows[1]-np.min(time_windows[1])
time_windows[2]=time_windows[2]-np.min(time_windows[2])

plt.plot(time_windows[0], silabas[0])
plt.plot(time_windows[1], silabas[1])
plt.plot(time_windows[2], silabas[2])

plt.xlabel('Time (s)')
plt.ylabel('Amplitud')

plt.show()


