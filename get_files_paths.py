# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:50:46 2017

@author: ger
"""


import os
import numpy as np


def get_files_paths(root, extension, info_file):

    '''
    Extract all paths of files with a certain extension inside all subfolders
    of "root" folder. Also read the information contained in the file "info_file".
        
    input:
        root: (string) root path within which the files will be searched
        extension: (string) file extension of the desired files
        info_file: (string) file name of the information file
        
    output:
        paths_to_files: (list) each element in this list contains a tuple. The
            1st position of each tuple conteins the info (string) associated
            to the file and the 2nd position, the file path (string).
            
    Ex: paths_to_files = get_files_paths('./datos', 'wav', 'bird_name.txt')
    
    '''
    root = "./datos"
    extension = 'wav'
    info_file = "bird_name.txt"
    
    paths_to_files = []
    file_names=[]
    bird_names=[]
    target = '.' + extension
    
    # os.walk(root) generates a list which elements are tuples with the form
    # (path, dirs, files), one for each folders and subfolders of root
    for (path, dirs, files) in os.walk(root):
        
        # create a list with the file names of files with the target extension
        target_files = []
        target_files = [file for file in files if target in file]
        
        # if there is any target file in the current folder, save its path and
        # read the info file
        if not target_files == []:
    #        print((path, dirs, files))        
            with open(os.path.join(path,info_file),'r') as f:
                info = f.read()
            
            for target_file in target_files:
                target_file_path = os.path.join(path, target_file)        
                #paths_to_files.append((info,target_file_path))
                #paths_to_files.append((target_file_path,target_file[:-4]))
                paths_to_files.append(target_file_path)
                file_names.append(target_file[:-4])
                bird_names.append(info)
    return [paths_to_files, file_names, bird_names]
