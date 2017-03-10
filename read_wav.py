# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sw

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
    plt.save('raw_audio.png')
    plt.close()

    return raw_audio, times, sample_rate, n_samples
