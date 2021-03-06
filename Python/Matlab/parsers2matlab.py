# parsers2matlab.py
"""Python module to pass MATLAB types to Python functions for parsing with
MATLAB """
def read_nodesGMSH(file_name):
    if '\\' not in file_name:
        file_name = '\\' + file_name   
    f = open(file_name,'r')
    N_elmts=int(f.readlines()[4])
    XYZ={'X':[],'Y':[],'Z':[]}
    f.close()
    f = open(file_name,'r')
    for line in f.readlines()[5:N_elmts+5]:
        linesplit=line.split(' ')
        XYZ['X'].append(float(linesplit[1]))
        XYZ['Y'].append(float(linesplit[2]))
        XYZ['Z'].append(float(linesplit[3]))
    f.close()
    return XYZ

def read_meshGMSH(file_name):
    if '\\' not in file_name:
        file_name = '\\' + file_name  
    import os
    cwd = os.getcwd()
    if file_name[1] != ':':
        fname = cwd + file_name
    else :
        fname = file_name
    f = open(fname,'r')
    N_nodes=int(f.readlines()[4])
    f.close()
    f = open(fname,'r')
    N_lines = len(f.readlines())
    XYZELMTS={'X':[],'Y':[],'Z':[],'N1':[],'N2':[],'N3':[]}
    f.close()
    f = open(fname,'r')
    for line in f.readlines()[5:N_nodes+5]:
        linesplit=line.split(' ')
        XYZELMTS['X'].append(float(linesplit[1]))
        XYZELMTS['Y'].append(float(linesplit[2]))
        XYZELMTS['Z'].append(float(linesplit[3]))
    f.close()
    f = open(fname,'r')
    for line in f.readlines()[N_nodes+8:N_lines-1]:
        linesplit=line.split(' ')
        if linesplit[1]=='2' :
            XYZELMTS['N1'].append(float(linesplit[5]))
            XYZELMTS['N2'].append(float(linesplit[6]))
            XYZELMTS['N3'].append(float(linesplit[7]))
    f.close()
    return XYZELMTS

def read_maskMIMICS(file_name):
    if '\\' not in file_name:
        file_name = '\\' + file_name  
    XYZ={'X':[],'Y':[],'Z':[]}
    f = open(file_name,'r')
    for line in f:
        linesplit=line.split(', ')
        XYZ['X'].append(float(linesplit[0]))
        XYZ['Y'].append(float(linesplit[1]))
        XYZ['Z'].append(float(linesplit[2]))
    f.close()
    return XYZ

def read_exportGVMIMICS(file_name):
    if '\\' not in file_name:
        file_name = '\\' + file_name  
    XYZI={'X':[],'Y':[],'Z':[],'I':[]}
    f = open(file_name,'r')
    for line in f:
        linesplit=line.split(', ')
        XYZI['X'].append(float(linesplit[0]))
        XYZI['Y'].append(float(linesplit[1]))
        XYZI['Z'].append(float(linesplit[2]))
        XYZI['I'].append(float(max(0,float(linesplit[3]))))
    f.close()
    return XYZI

def find_ProsthFile(directory,Pname,Ptype):
    import os
    Ptype = int(Ptype)
    os.chdir(directory)
    directory = os.getcwd()
    os.chdir(directory)
    
    files_list = []
    prosthType = 'Prosthesis'+str(Ptype)
    Pname = 'Implant' + str(Ptype) + '_'+ Pname + '.msh'
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files_list.append(os.path.join(path, name))
    A = [fdir for fdir in files_list  if prosthType in fdir and Pname in fdir]
    mshFile = str(A[0])
    return mshFile

def find_ProsthFile_read_meshGMSH(directory,Pname,Ptype):
    
    mshFile = find_ProsthFile(directory,Pname,Ptype)
    
    XYZElmts = read_meshGMSH(mshFile)
    
    return XYZElmts

def read_CSfromOutput(file_name):
    if '\\' not in file_name:
        file_name = '\\' + file_name  
    f = open(file_name,'r')
    XYZ={'X':[],'Y':[],'Z':[]}
    GoodLine = False
    for line in f:
        if GoodLine :
            linesplit=line.split(' ')
            XYZ['X'].append(float(linesplit[0]))
            XYZ['Y'].append(float(linesplit[1]))
            XYZ['Z'].append(float(linesplit[2]))
            GoodLine = False
            
        if ~GoodLine and 'Axe ' in line:
            GoodLine = True
    f.close()
    return XYZ
