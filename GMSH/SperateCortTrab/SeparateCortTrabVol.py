# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:01:59 2017

@author: Jean-Baptiste RENAULT
"""


import os
import numpy as np

os.chdir('C:\Users\Jean-Baptiste\Documents\These\Methodes\BasicFunctions\Python\GMSH')


from script_checks import matlab_module_exists
matlab_module_exists('matlab.engine')
import matlab

Nodes = []
Elmts3D = dict()
Elmts3DCentroid = dict()
Elmts2D = dict()

SurfInElmts = []

Output = ''

SurfacesCounter = 0

fileIn = 'All_Stl.inp'  


# =============================================================================
# Read the abaqus input file and find the surface (a 2D elements set) delimiting both volumes
# =============================================================================

with open(fileIn, "r") as f:
    line = f.readline()
    Output += line
    while '*NODE' not in line:
        line = f.readline()
        Output += line
        #print(line)
        
    line = f.readline()
    Output += line
    while '***' not in line:
        previousline = line
        Nodes.append([float(j) for j in previousline.split(", ")[1:]])
        line = f.readline()
        Output += line

    
    NdCon = dict((key, []) for key in range(1,1+len(Nodes)))
    while '*ELEMENT, type=CPS' not in line:
        line = f.readline()
    
    
    while line[0:18] != '*ELEMENT, type=C3D':
        line = f.readline()
        while '*ELEMENT' not in line and '*ELSET' not in line:
            previousline = line
            Elmts2D[int(previousline.split(", ")[0])] = [int(j) for j in line.split(", ")[1:]]
            line = f.readline()
        SurfacesCounter +=1
    
    Output += line
    line = f.readline()
    while 'PhysicalSurface' not in line:
        previousline = line
        ElmtId = int(previousline.split(", ")[0])
        Elmts3D[ElmtId] = [int(j) for j in previousline.split(", ")[1:]]
        Elmts3DCentroid[ElmtId] = np.mean([np.asarray(Nodes[nd-1])  for nd in Elmts3D[ElmtId]],axis=0)
        for ElmtNd in [int(j) for j in previousline.split(", ")][1:]:
            NdCon[ElmtNd].append(int(previousline.split(", ")[0]))
        Output += line
        line = f.readline()
        
    
    while 'ELSET=PhysicalSurface' not in line:
        line = f.readline()
    
    
    line = f.readline()
    while '*' not in line and line:
        previousline = line
        SurfInElmts.append([int(j) for j in previousline.split(", ")[0:-1]])
        line = f.readline()

    while line:   
        line = f.readline()

Elmts3DCentroid_Id = Elmts3DCentroid.keys()

# =============================================================================
# Convert the PhyscialSurface ElSet to a face Vertex structure
# =============================================================================
SurfInElmts = [item for sublist in SurfInElmts for item in sublist]
Faces = matlab.int32([Elmts2D[el] for el in SurfInElmts])
Vertices = matlab.double(Nodes)
Points = matlab.double([list(Elmts3DCentroid[el]) for el in Elmts3DCentroid_Id])


# =============================================================================
# Launch the matlab engine and function
# =============================================================================
eng = matlab.engine.start_matlab()

In = eng.inpolyhedron(Faces,Vertices,Points,'FLIPNORMALS',True)
In2 = np.array(In)

ElmtIn = []
ElmtOut = []
i=0
for el in Elmts3DCentroid_Id:
   if In2[i][0]:
       ElmtIn.append(el)
   else:
       ElmtOut.append(el)
       
   i+=1
# =============================================================================
# Write the new Abaqus inp file with both volumes delimited
# =============================================================================

fileOut = fileIn.split('.inp')[0]+'_CortTrab.inp'
with open(fileOut,'w') as f:
    f.write(Output)
    f.write('*ELSET,ELSET=TrabVol\n')
    i=0
    for el in ElmtIn:
        if i<10 :
            f.write(str(el)+', ')
            i+=1
        else:
            f.write(str(el)+'\n')
            i=0
    
    if i!=10:
        f.write('\n')
    
    f.write('*ELSET,ELSET=CortVol\n')
    i=1
    for el in ElmtOut:
        if i<10 :
            f.write(str(el)+', ')
            i+=1
        else:
            f.write(str(el)+'\n')
            i=0
        
print('  ')




        