#
def espectrograma(audio,times,standard_sample_rate,windows=[0.0]):
    import numpy as np
    ssr = standard_sample_rate
    NFFT = 1024


    # AHORA SOLO PLOTEO LOS RESULTADOS
    # ax1 = plt.subplot(211)
    # Pxx, freqs, bins, im = plt.specgram(audio, NFFT=NFFT, Fs=sample_rate, noverlap=900)
    # plt.subplot(212, sharex=ax1)
    # plt.plot(times,audio)
    # plt.show()
    # plt.savefig('espectrograma.png') esto no anda todavia

    f, t, Sxx = signal.spectrogram(audio, fs)
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

# file = './datos/upupa/call2.wav'                                    #@#@#@#
# [sample_rate, audio] = sw.read(file)
# audio = np.array(audio)
# data_points = float(len(audio))
# t_fin = data_points/sample_rate
# times = np.arange(0.,t_fin,t_fin/float(len(audio)))
