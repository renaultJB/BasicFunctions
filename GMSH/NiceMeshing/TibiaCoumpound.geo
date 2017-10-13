Geometry.HideCompounds = 1; // show underlying STL

Mesh.RemeshAlgorithm=1; //(0) nosplit (1) automatic (2) splitmetis
//Mesh.CharacteristicLengthFactor=0.5;
//Mesh.CharacteristicLengthFromPoints=0;
//Mesh.CharacteristicLengthMin=0.5;
//Mesh.CharacteristicLengthMax=1;

// Changer le nom pour le fichier STL
//Merge "Tibia_GUI_R_cut_a0.0.step";
Merge "Tibia_GUI_R.stp";

Surfl = Surface "*";

s = news;
//Compound Surface(s)={1,2,4,9,10,11,12,13,14};
Compound Surface(s)={Surfl[]};