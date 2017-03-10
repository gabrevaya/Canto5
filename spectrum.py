import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as sw

op = './datos/albanella/call1.wav'                                    #@#@#@#
[fs, x] = sw.read(op)

N = len(x)

time = np.arange(N) / float(fs)

f, t, Sxx = sig.spectrogram(x, fs,nperseg=500,nfft=512, noverlap=400,mode='magnitude')


print Sxx.shape
print Sxx[0,0],Sxx[1,0]
print t[0],t[1],t[2]


maximo = Sxx.max(axis=1)
maximo = maximo.max()
print "maximo= ", maximo

umbral = maximo * 0.50

validos = np.where(Sxx>=umbral)

validos = np.c_[validos[0],validos[1]]

puntos_validos = []
[puntos_validos.append([ t[v[1]],f[v[0]] ]) for v in validos]

print "fs= ", fs
print f[0:5],f[-1]
print Sxx
# ax1 = plt.subplot(211)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.subplot(212, sharex=ax1)
# plt.plot(puntos_validos[0],puntos_validos[1])
# plt.show()
