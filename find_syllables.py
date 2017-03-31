'''
Finds the time windows where the syllables are, inside the raw-audio file.
'''
# -*- coding: utf-8 -*-

from read_wav import read_wav
from envolvente import envolvente
import numpy as np
import matplotlib.pyplot as plt

#audio_file="call1.wav"
#[raw_audio, times, sample_rate, data_points]=read_wav(audio_file)
#[env, t_env]=envolvente(raw_audio, times, sample_rate, data_points, 1000, 1, 0)

def find_syllables(raw_audio, times, env, t_env, npoints_umbral, fbird):
    '''
    Input: raw_audio, times - Amplitud and time vector of the original audio file
                              (only to plot a explanary graf).
           env, t_env       - Amplitude and time vector of the wrapping wave of the
                              audio signal.
           npoints_umbral   - Number of points counted from the start, considered
                              to estimate a threshold value "umbral" that the
                              amplitude of the syllable usually surpasses.
    Output: loc_silaba      - Boolean signal identifying the time windows where the
                              syllables are. (mask)

    '''

    #npoints_umbral=100

    umbral=np.max(env[:npoints_umbral])

    #print ("umbral=",umbral)

    fbird=1.8

    loc_silabas=np.greater(env,umbral*fbird)

    #indices=np.nonzero(loc_silabas[1:] != loc_silabas[:-1])[0] + 1
    #silabas=np.split(raw_audio,indices)


    plt.plot(times,raw_audio)
    plt.plot(t_env, env, linewidth=3)
    plt.plot(t_env,loc_silabas*10000)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')

    plt.show()
    #fig.savefig('loc_silabas.png')
    plt.close()

    #loc_index=np.diff(loc_silabas)
    #plt.plot(loc_index)
    #plt.show()

    return loc_silabas
