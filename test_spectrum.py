import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as sw

op = './datos/albanella/call1.wav'
[fs, x] = sw.read(op)

N = len(x)
nnfft = 512
time = np.arange(N) / float(fs)

f, t, Sxx = sig.spectrogram(x, fs,nperseg=500,nfft=nnfft, noverlap=400,mode='magnitude')


print Sxx.shape
print Sxx[0,0],Sxx[1,0]
print t[1],t[2],t[3]


maximo = Sxx.max(axis=1)
maximo = maximo.max()
print "lentime",len(time)

umbral = maximo * 0.05

validos = np.where(Sxx>=umbral)
xx = validos[0]
yy = validos[1]
xs = np.arange(len(t))
ys = np.arange(len(f))

validos = np.c_[validos[0],validos[1]]
puntos_validos = []

t_convert = np.abs(t[3]-t[2])
f_convert = f[1]#fs/float(nnfft)

real_data = [ [v[0]*t_convert,v[1]*f_convert] for v in validos]
[puntos_validos.append([ t[v[1]],f[v[0]] ]) for v in validos]
# print len(puntos_validos)
# print time
# print fs
print validos[0]
print real_data[0]
# ax1 = plt.subplot(211)
# plt.pcolormesh(t, f, Sxx)
# plt.pcolormesh(xs,ys,Sxx)
# # plt.ylabel('Frequency [Hz]')
# # plt.xlabel('Time [sec]')
# plt.subplot(212, sharex=ax1)
# plt.scatter(yy,xx)
'''
ahora escaleo todo a unidades fisicas
'''
plt.scatter(real_data[0],real_data[1])
# plt.xlim(0.,float(len(xs))*t_convert)
# plt.ylim(0.,float(len(ys))*f_convert)
# # plt.scatter(puntos_validos[0],puntos_validos[1])
plt.show()


#esto andaba para plotear
# ax1 = plt.subplot(211)
# plt.pcolormesh(xs,ys,Sxx)
# plt.subplot(212, sharex=ax1)
# plt.scatter(yy,xx)
# plt.xlim(0.,float(len(xs)))
# plt.ylim(0.,float(len(ys)))



#para intentar plotear con unidades
# ax1 = plt.subplot(211)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.subplot(212, sharex=ax1)
# plt.plot(puntos_valid[0],puntos_valid[1])
# plt.show()
