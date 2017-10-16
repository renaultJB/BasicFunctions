Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
Mesh.CharacteristicLengthExtendFromBoundary = 0;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthFromCurvature = 0;
Mesh.CharacteristicLengthMin=1.05;
Mesh.CharacteristicLengthMax=2.25;
// Mesh.Optimize = 1;
// Mesh.HighOrderOptimize = 1;

// Changer le nom pour le fichier STL
Merge "Tibia.step";

LINE1

LINE2

LINE3

//SetOrder 2;

Mesh 2;
Mesh 3;

OptimizeMesh "Gmsh";
OptimizeMesh "Netgen";

SetOrder 2;

//Mesh.HighOrderOptimize = 1;


Save "Tibia.inp";

//Exit;