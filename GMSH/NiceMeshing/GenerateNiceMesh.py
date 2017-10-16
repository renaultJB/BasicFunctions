# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:16:08 2017

@author: Jean-Baptiste RENAULT

The goal of this script is to generate a nice 3D mesh of a Bone step CAD Files. 
When the original Bone CAD file is generated, it's made of nurbs surfaces
patches. When cutted it may generate very small surfaces that are difficult to 
mesh and results in bad elements. 
"""

import os 
import subprocess
import GMSH as gmsh
from collections import defaultdict

CWD = os.getcwd()

# =============================================================================
# Selection of the files to be meshed
# =============================================================================

OriginalCAD_Name = 'Tibia_GUI_R.stp'
CuttedCAD_Name = 'Tibia_GUI_R_cutted_a0.0.step'


# =============================================================================
# Grossly mesh the original file and the cutted one
# =============================================================================

subprocess.call(["cd", CWD], shell=True)
subprocess.call(["gmsh", OriginalCAD_Name, '-2','-clmax','2'], shell=True)
subprocess.call(["gmsh", CuttedCAD_Name, '-2','-clmax','2'], shell=True)

# =============================================================================
#  Import the recently created mesh
# =============================================================================
  
Mesh0 = gmsh.Mesh('.'.join(OriginalCAD_Name.split('.')[:-1])+'.msh')
MeshC = gmsh.Mesh('.'.join(CuttedCAD_Name.split('.')[:-1])+'.msh')

# =============================================================================
# Check if the surfaces centroids of the cutted object belongs to the original
# =============================================================================

OkSurf = defaultdict(list)

for surf in MeshC.Surfaces:
    d, Nd = Mesh0.nearestNode(surf.Centroid)
    if d < 3:
        OkSurf[0].append(str(surf.Id))
        
for surf in MeshC.Surfaces:
    if str(surf.Id) not in OkSurf[0] :
        Areas = [s.Area for s in MeshC.Surfaces]
        Areas.sort()
        if surf.Area < Areas[-4]:
            OkSurf[1].append(str(surf.Id))
            

f = open('Compound.geo','r')
filedata = f.read()

Lc = 's = news;\nCompound Surface(s)={{{}}};'

newdata = filedata.replace("Tibia.step" , CuttedCAD_Name)
newdata = newdata.replace("LINE1" , Lc.format(','.join(OkSurf[0])))
#newdata = newdata.replace("LINE2" , Lc.format(','.join(OkSurf[1])))
newdata = newdata.replace("LINE2" , '')
newdata = newdata.replace("LINE3" , '')
finaldata = newdata.replace("Tibia.inp" , '.'.join(OriginalCAD_Name.split('.')[:-1]) + ".inp")
f.close()

f = open('Temp_inp.geo','w')
f.write(finaldata)
f.close()

subprocess.call(["gmsh", 'Temp_inp.geo'], shell=True)
