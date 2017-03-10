# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from envolvente import envolvente
from read_wav import read_wav
from get_files_paths import get_files_paths
from find_syllables import find_syllables
from split_syllables import split_syllables
#from spectrum import spectrum

#def main(bin_size, fbird):
#def main(directorio, bin_size, fbird):
'''
Función principal. Obtiene silabas separadas y caracterizadas desde un archivo wav.
'''
directorio = '.'
bin_size = 1000
fbird = 1.8    

[paths_to_files, file_names, bird_names]=get_files_paths(directorio, "wav", "bird_name.txt")

#audio_file="call1.wav"

for audio_file in paths_to_files:

    [raw_audio, times, sample_rate, data_points]=read_wav(audio_file)

	#Calculo e imprimo envolvente de máximos
    [envelope, t_envelope]=envolvente(raw_audio, times, sample_rate, data_points, 100, 0, 0)

    plt.plot(times, raw_audio)
    plt.plot(t_envelope, envelope)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitud')

    #Separación de sílabas:  Nuevo cálculo de envolvente (media)
    #bin_size=2500 #(depende)
    [env, t_env]=envolvente(raw_audio, times, sample_rate, data_points, bin_size, 1, 0)

    #Creación de señal lógica indicando ventanas donde están las sílabas
    npoints_umbral=100

    loc_silabas=find_syllables(raw_audio, times, env, t_env, npoints_umbral, fbird) 
    
    # Creada la señal lógica, con ella se corta el vector original
    margen=50   #puntos
 
    silabas=split_syllables(raw_audio, loc_silabas, margen)
    time_windows=split_syllables(times, loc_silabas, margen)

    nro_sil=len(silabas)
    #i_silabas=[0:nro_sil:1]

    # imprimo sílabas resaltándolas en igual posición en el grafico original
    plt.plot(times, raw_audio)

    for sil in range(nro_sil):
        plt.plot(time_windows[sil], silabas[sil])
        #aprovecho para corregir origen de vectores de tiempo resultantes del corte
        time_windows[sil]=time_windows[sil]-np.min(time_windows[sil])
    plt.show()

    #imprimo sílabas en graficos diferentes
#    fig= plt.subplots(nro_sil, 1, sharex='row')
#
#    for sil in range(nro_sil):
#       ax = plt.subplot(nro_sil,1,sil)
#       ax.plot(time_windows[sil], silabas[sil])
#   
#    plt.xlabel('Time (s)')
#    plt.ylabel('Amplitud')
#    plt.show()
#    #plt.savefig(directorio+'silabas.png')
#    plt.close()
#
