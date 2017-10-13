Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
// Mesh.CharacteristicLengthFactor = 2;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthMin=1;
Mesh.CharacteristicLengthMax=3;

// Changer le nom pour le fichier STL
//Merge "Cube20.step";

Merge "VC_Tibia_All_Smth_reduced_3.stp";
Surfl1 = Surface "*";

//Merge "Cube10.stl";
Merge "Inside.stp";

Surfl2 = Surface "*";

s = news;
sl = newsl;

Printf("Surface number = %g",#Surfl1[]);

Surface Loop(sl)={Surfl2[#Surfl1[],#Surfl2[]-1]};
Physical Surface (s)={sl};

Delete{ Surface{#Surfl1[]+1}; }

Surfl = Surface "*";
Printf("Last Surface number = %g",Surfl1[#Surfl1[]-1]);

Voll = Volume "*";
Printf("Last Volume number = %g",Voll[#Voll[]-1]);

Surface{sl} In Volume{Voll[#Voll[]-1]};
