def spectrum(audio,sample_rate):
    '''
    Esta función calcula el espectrograma de una señal. Tambien puede usarse
    (si se descomenta la segunda sección para conseguir un "filtrado" de los
    puntos del espectrograma, osea, las frecuancias con una amplitud mayor a la
    especificada por la variable "treshold" ).

    Argumentos: audio , sample_rate
    audio: un array 1D al que se le aplica el espectrograma
    sample_rate: la frecuenca de sampleo del audio.

    Devuelve: t,f,Sxx
    Los resultados del espectrograma
    '''
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
