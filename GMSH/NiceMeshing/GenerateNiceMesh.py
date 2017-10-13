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

CWD = os.getcwd()

# =============================================================================
# Selection of the files to be meshed
# =============================================================================

OriginalCAD_Name = 'Tibia_GUI_R.stp'
CuttedCAD_Name = 'Tibia_GUI_R_cut_a0.0.step'

# =============================================================================
# Grossly mesh the original file and the cutted one
# =============================================================================

subprocess.call(["cd", CWD], shell=True)
subprocess.call(["gmsh", OriginalCAD_Name, '-2','-clmax','2'], shell=True)
subprocess.call(["gmsh", CuttedCAD_Name, '-2','-clmax','2'], shell=True)

# =============================================================================
# 
# =============================================================================
