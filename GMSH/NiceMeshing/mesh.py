# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:08:03 2017

@author: Jean-Baptiste
"""

class Mesh:
    
    def __init__(self,fileAdress):
        self.fileAdress = fileAdress
        self.Name = fileAdress.split('//')[-1]
        self.SurfList = dict()
        self.LineList = dict()
        self.Elements1D = []
        self.Elements2D = []
        self.Elements3D = []
        
    def computeElement2DCentroid(self):
        self.CentroidElement2D = dict()
        for el in Elements2D:
            el.ComputeCentroid()
            self.CentroidElements2D[el.id] = el.Centroid()

class Node:
    
    def __init__(self,Id,Coord):
        self.Coord = Coord
        self.Id = Id
        
class Element:
#    Reprendre les nodes dans les elements
    def __init__(self, Nodes, *args):
        if len(args)==1 and isinstance(args[0], basestring) :
            self.Id, self.Type, self.Surface = [  args[0].split()[i] for i in [0,1,4]]
            self.Nodes = [ Nodes[i] for i in args[0].split()[i][5:] ]
        elif  len(args)>1 :
            self.Id = args[0]
            self.Surface = args[2]
            self.NodesId = args[3]
            
    def ComputeCentroid():
        self.Centroid = np.sum([nd.coord for nd in self.Nodes)
        
        
        
    