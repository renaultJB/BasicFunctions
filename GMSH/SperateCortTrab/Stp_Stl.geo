Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
// Mesh.CharacteristicLengthFactor = 2;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthMin=1;
Mesh.CharacteristicLengthMax=3;

// Changer le nom pour le fichier STL
//Merge "Cube20.step";

Merge "VC_Tibia_All_Smth_reduced_3.stp";
Surfl = Surface "*";

//Merge "Cube10.stl";
Merge "VC_inside_Redc.stl";
s = news;
sl = newsl;

Printf("Surface number = %g",#Surfl[]);

Compound Surface(s)={#Surfl[]+1};
Surface Loop(sl)={s};
Physical Surface (s)={s};

Delete{ Surface{#Surfl[]+1}; }

Surfl = Surface "*";
Printf("Last Surface number = %g",Surfl[#Surfl[]-1]);

Voll = Volume "*";
Printf("Last Volume number = %g",Voll[#Voll[]-1]);

Surface{s} In Volume{Voll[#Voll[]-1]};
