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
from GMSH import Mesh
import numpy as np

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
subprocess.call(["gmsh", OriginalCAD_Name, '-2','-clmax','3'], shell=True)
subprocess.call(["gmsh", CuttedCAD_Name, '-2','-clmax','3'], shell=True)

# =============================================================================
#  Import the recently created mesh
# =============================================================================
  
Mesh0 = Mesh('.'.join(OriginalCAD_Name.split('.')[:-1])+'.msh')
MeshC = Mesh('.'.join(CuttedCAD_Name.split('.')[:-1])+'.msh')

# =============================================================================
# Check if the surfaces centroids of the cutted object belongs to the original
# bone surfaces
# =============================================================================
small_surf_patch = []
surf_areas = np.array([s.Area for s in MeshC.Surfaces])
surf_cut = []

for surf in MeshC.Surfaces:
    d, Nd = Mesh0.nearestNode(surf.Centroid)
    
    if d < 3 and surf.Area < 0.1*np.median(surf_areas):
        small_surf_patch.append(surf.connected_surfaces(MeshC.Surfaces))
    
    elif d > 5:
        surf_cut.append(surf.Id)
        
# remove surfaces belonging to the cut surfaces
small_patch_Ok = [p-set(surf_cut) for p in small_surf_patch]          


# Merge set that intersect
sets = list(small_patch_Ok)
merged = True
while merged:
    merged = False
    results = []
    while sets:
        common, rest = sets[0], sets[1:]
        sets = []
        for x in rest:
            if x.isdisjoint(common):
                sets.append(x)
            else: 
                merged = True
                common |= x
        results.append(common)
    sets = results

# =============================================================================
# Write found surface patches to .geo file to compound those surfaces
# =============================================================================
with open('Compound.geo','w') as f :
    f.write('Mesh.RemeshAlgorithm=1;\n'
            'Mesh.CharacteristicLengthExtendFromBoundary = 0;\n'
            'Mesh.CharacteristicLengthFromPoints = 0;\n'
            'Mesh.CharacteristicLengthFromCurvature = 0;\n'
            'Mesh.CharacteristicLengthMin=1.05;\n'
            'Mesh.CharacteristicLengthMax=2.25;\n'
            )
    
    f.write('Merge "{}";'.format(CuttedCAD_Name))
    
    Lc = 's = news;\nCompound Surface(s)={{{}}};\n'
    for s in sets :
        s_str = [str(i) for i in s]
        f.write(Lc.format(','.join(s_str)))
    
    
    f.write('Mesh 2;\nMesh 3;\nOptimizeMesh "Gmsh";\nOptimizeMesh "Netgen";\n'
            'SetOrder 2;\nSave "Tibia.inp";\nExit;')
    


# =============================================================================
# Launch the the meshing of the coumpound surface
# =============================================================================
subprocess.call(["gmsh", 'Compound.geo'], shell=True)

os.remove('Compound.geo')


