# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:50:46 2017

@author: ger
"""


import os
import numpy as np


def get_files_paths(root, extension, info_file):

    '''
    Extrae todos las direcciones de archivos con una extensión deseada dentro de
    todas las subcarpetas de "root" y lee la información que se encuentra en el
    archivo "info_file".
    
    input:
        root: (string) dirección de raíz en la que se buscarán archivos
        extension: (string) extensión de los archivos que se busca
        info_file: (string) archivo que contiene información acerca de los archivos
        
    output:
        paths_to_files: (list) cada elemento de esta lista contiene una tupla, cada
            tupla contiene en la primera posición la info (string) asociada al
            archivo y en la segunda la dirección al archivo.
            
    Ej: paths_to_files = get_files_paths('./datos', 'wav', 'bird_name.txt')
    
    '''
    root = "./datos"
    extension = 'wav'
    info_file = "bird_name.txt"
    
    paths_to_files = []
    target = '.' + extension
    
    
    for (path, dirs, files) in os.walk(root):
        target_files = []
        target_files = [file for file in files if target in file]
        
        if not target_files == []:
    #        print((path, dirs, files))        
            with open(os.path.join(path,info_file),'r') as f:
                info = f.read()
            
            for target_file in target_files:
                target_file_path = os.path.join(path, target_file)        
                paths_to_files.append((info,target_file_path))
                
    return paths_to_files
