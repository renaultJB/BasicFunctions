# -*- coding: utf-8 -*-
"""
Created on 02-26-2016

@author: Jean-Baptiste
"""

import os
import time

print("Script that tries to delete 1D and 2D elements of current folder Abaqus input files")
print("Only works with Tetrahedral Elements")
#DELETE Non Volumetric elements of Abaqus Inp File
# !!! Works only for tetrahedral 3D Elements
cwdf = os.listdir(os.getcwd())
inp_files = []
for files in cwdf :
    if files[len(files)-4:len(files)]== '.inp':
        print("Found .inp files : "+files)
        output=''
        with open(files, "r") as f:
            line = f.readline()
            while line[0:3] != '***':
                output = output + line
                line = f.readline()
                #print(line)
            output = output + line  
            while line[0:18] != '*ELEMENT, type=C3D':
                line = f.readline()
            output = output + line    
            for line in f.readlines():
                output = output + line
        with open(files, "w") as f:
            print(files+" ---> done reading.")
            f.write(output)
            print(files+" ---> done writing.")

print("Auto-closing in 10s")
time.sleep(7)
print("Auto-closing in 3s")
time.sleep(3)
