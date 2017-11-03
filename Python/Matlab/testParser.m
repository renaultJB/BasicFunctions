clearvars
XYZELMTS = py.parsers2matlab.read_meshGMSH('C:\Users\Jean-Baptiste\Documents\These\Methodes\BasicFunctions\Python\Matlab\Tibia_GUI_R.msh');
Pts2D = [cell2mat(cell(XYZELMTS{'X'}))' cell2mat(cell(XYZELMTS{'Y'}))' cell2mat(cell(XYZELMTS{'Z'}))'];
Elmts2D = [cell2mat(cell(XYZELMTS{'N1'}))' cell2mat(cell(XYZELMTS{'N2'}))' cell2mat(cell(XYZELMTS{'N3'}))'];