Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
//Mesh.CharacteristicLengthFactor=0.5;
//Mesh.CharacteristicLengthFromPoints=0;
//Mesh.CharacteristicLengthMin=0.5;
//Mesh.CharacteristicLengthMax=1;

// Changer le nom pour le fichier STL
Merge "VC_inside.stl";

//s = news;
//sl = newsl;
//vol = newv;

//Printf("New Surface number = %g",s);
//Printf("New Surface loop number = %g",sl);
//Printf("New Volume number = %g",vol);

Compound Surface(2)={1};
//Surface Loop(sl)={s};
//Volume(vol)={sl};
Physical Surface (1)={1};
//Physical Volume (1)={ vol };
//Delete{ Volume{vol}; }


// READ BONE MESH
Merge "VC_Tib.stl";

s = news;
sl = newsl;
vol = newv;

//Printf("New Surface number = %g",s2);
//Printf("New Surface loop number = %g",sl2);
//Printf("New Volume number = %g",vol2);

Compound Surface(s)={s-1};
Surface Loop(sl)={s};
Volume(vol)={sl};
//Physical Surface (s2)={s2};
//Physical Volume (vol2)={vol2};


// EMBED INSIDE MESH WITHIN BONE MESH
Surface{2} In Volume{vol};
