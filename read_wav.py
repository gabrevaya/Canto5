'''
Read wav files.
'''
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sw

def read_wav(audio_file):
    '''
    Input: file path.
    Output: raw audio amplitudes, corresponding times, sample rate, number of
    samples.
    '''

    [sample_rate, raw_audio] = sw.read(audio_file)
    raw_audio = np.array(raw_audio)
    n_samples= len(raw_audio)

    #t_fin = n_samples/sample_rate
    times = np.arange(0,n_samples,1)*(1/sample_rate)
    

    t_fin = n_samples/sample_rate
    times = np.arange(0,t_fin,1/sample_rate)


    #fig=plt.figure(figsize=(30,10))
    #fig=plt.figure()
    plt.plot(times,raw_audio)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')

    plt.show()
    #fig.savefig('raw_audio.png')
    #plt.close('all')

    return raw_audio, times, sample_rate, n_samples
