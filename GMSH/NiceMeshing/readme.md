# Nice Meshing goals :

The goal of these code is to identify the surface composing a *.step* file from an anatomical structure (this is also valid for retro-engineered curvly shaped I guess), then:  
1. Identify the small surfaces and their neighbours  
2. Create list of those surfaces and their neighbours  
3. In the GMSH script merge them to get connected surface patch  
4. Generate the mesh with GMSH  
5. If you want to delete the 2D elements you can use the [*Inp2InpVol.py*](https://github.com/renaultJB/BasicFunctions/blob/master/Python/Abaqus/Inp2InpVol.py) tool.
