"""
This function calcuates the spectrogram of a signal. It also can be used
for getting the coordinates of points with a frequency-amplitude greater
than certain treshold (uncommenting the last lines).
"""

# Created on Thu Mar  9 18:12:41 2017
#
# @author: ger
# """
def spectrum(audio,sample_rate):
    """
    input:
        audio (1D array). Signal to transform.
        sample_rate (float). Sampling frequency of the audio file corresponding
        to 'audio'.
    output:
        t (1d array). Times corresponding to the second component of 'Sxx'
        f (1d array). Frequencies corresponding to the first component of 'Sxx'
        Sxx (array). Spectrogram. Frequency-amplitudes as functions of times
        and frequencies.
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.signal as sig

    fs = sample_rate
    N = len(audio)
    time = np.arange(N) / float(fs)
    f, t, Sxx = sig.spectrogram(audio, fs,nperseg=500,nfft=512, noverlap=400,mode='magnitude')

    '''
    descomentar lo siguiente para usar el filtro de datos. xx e yy contienen los
    indices de la matriz Sxx donde se encuentran los valores mayores al umbral
    (treshold)
    '''
    # big = Sxx.max(axis=1)
    # big = big.max()
    # treshold = big * 0.50
    #
    # valid = np.where(Sxx>=treshold)
    # valid = np.c_[valid[0],valid[1]]
    # xx = valid[0]
    # yy = valid[1]
    # xs = np.arange(len(t))
    # ys = np.arange(len(f))

    return f,t,Sxx
