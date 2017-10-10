# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:01:59 2017

@author: Jean-Baptiste
"""


import os
import time
import numpy as np

os.chdir('C:\Users\Jean-Baptiste\Documents\These\Methodes\BasicFunctions\Python\GMSH')

import matlab.engine
from script_checks import matlab_module_exists,find_ProsthFiles
matlab_module_exists('matlab.engine')
 
Nodes = []
Elmts3D = dict()
Elmts3DCentroid = dict()
Elmts2D = dict()
ElmtCon = dict()

SurfInElmts = []

NodeSetIn = []
NodeSetOut = []

SurfacesCounter = 0

files = 'test3_stl.inp'

with open(files, "r") as f:
    line = f.readline()
    while '*NODE' not in line:
        line = f.readline()
        #print(line)
        
    line = f.readline()
    while '***' not in line:
        previousline = line
        Nodes.append([float(j) for j in previousline.split(", ")[1:]])
        line = f.readline()

    
    NdCon = dict((key, []) for key in range(1,1+len(Nodes)))
    
    line = f.readline()
    while line[0:18] != '*ELEMENT, type=C3D':
        line = f.readline()
        while '*ELEMENT' not in line and '*ELSET' not in line:
            previousline = line
            Elmts2D[int(previousline.split(", ")[0])] = [int(j) for j in line.split(", ")[1:]]
            line = f.readline()
        SurfacesCounter +=1
    
    line = f.readline()
    while 'PhysicalSurface' not in line:
        previousline = line
        ElmtId = int(previousline.split(", ")[0])
        Elmts3D[ElmtId] = [int(j) for j in previousline.split(", ")[1:]]
        Elmts3DCentroid[ElmtId] = np.mean([np.asarray(Nodes[nd-1])  for nd in Elmts3D[ElmtId]],axis=0)
        for ElmtNd in [int(j) for j in previousline.split(", ")][1:]:
            NdCon[ElmtNd].append(int(previousline.split(", ")[0]))
        line = f.readline()
    
    while 'ELSET=PhysicalSurface2' not in line:
        line = f.readline()
    
    
    line = f.readline()
    while '*' not in line:
        previousline = line
        SurfInElmts.append([int(j) for j in previousline.split(", ")[0:-1]])
        line = f.readline()
    

    while 'NSET=PhysicalSurface' not in line:
        line = f.readline()
    
    line = f.readline()
    while '*' not in line:
        previousline = line
        NodeSetIn.append([int(j) for j in previousline.split(", ")[0:-1]])    
        line = f.readline()
    
    line = f.readline()
    while '*' not in line:
        previousline = line
        NodeSetOut.append([int(j) for j in previousline.split(", ")[0:-1]])    
        line = f.readline()

    while line:   
        line = f.readline()

NodeSetIn = [item for sublist in NodeSetIn for item in sublist]
NodeSetOut = [item for sublist in NodeSetOut for item in sublist]

ElSetOut_0 = [ item for nd in NodeSetOut for item in NdCon[nd] ]

ElSetInOut = [ item for nd in NodeSetIn for item in NdCon[nd] ]

#ElmtOut = [el in Elmts3D.keys()  for el in ElSetOut_0 ]

NdCon2 = [ NdCon[key] for key in NdCon.keys() ]

# Separate the two volumes by removing all elements touching the inside boundary 

for el0 in Elmts3D.keys():
    ElmtCon[el0] = np.unique([el for nd in Elmts3D[el0] for el in NdCon[nd] if el!=el0])


ElmtsId = Elmts3D.keys();

ElmtsIdOk = Elmts3D;

for el in ElSetInOut:
    ElmtsIdOk[el] = []

#NdConOk[] = 

#[ el for el in ElmtsId if el not in ElSetInOut ]
print('End of file reading')




        