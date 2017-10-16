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
Merge "Tibia_GUI_R_cutted_a0.0.step";

s = news;
Compound Surface(s)={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,95,96,97,98,99,100,101,102,103,104,105,106,107};

s = news;
Compound Surface(s)={123,124};



//SetOrder 2;

Mesh 2;
Mesh 3;

OptimizeMesh "Gmsh";
OptimizeMesh "Netgen";

SetOrder 2;

//Mesh.HighOrderOptimize = 1;


Save "Tibia_GUI_R.inp";

//Exit;