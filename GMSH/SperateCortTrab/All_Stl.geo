Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
// Mesh.CharacteristicLengthFactor = 2;
Mesh.CharacteristicLengthFromPoints = 0;
Mesh.CharacteristicLengthMin=1;
Mesh.CharacteristicLengthMax=3;

// Changer le nom pour le fichier STL
Merge "VC_Tibia.stl";
s0 = news;
sl0 = newsl;
vol0 = newv;

Compound Surface(s0)={1};
Surface Loop(sl0)={s0};
Volume (vol0) = {sl0};

Surfl = Surface "*";

Merge "VC_inside.stl";
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

Surface{s} In Volume{vol0};
