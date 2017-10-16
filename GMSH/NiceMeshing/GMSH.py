# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:08:03 2017

@author: Jean-Baptiste
"""
import numpy as np
from collections import defaultdict
import scipy.spatial as spatial


class Mesh:
    
    def __init__(self,fileAdress):
        self.fileAdress = fileAdress
        self.Name = fileAdress.split('//')[-1]
        self.LineList = defaultdict(list)
        self.Nodes = []
        self.Elements = []
        
#        self.Elements1D = []
#        self.Elements2D = []
#        self.Elements3D = []
        
        f = open(fileAdress,'r')
        A = [f.readline() for i in range(4)]
        line = f.readline()
        for i in range(int(line)):
            line = f.readline()
            A = line.split()
            Id = int(A[0])
            Coord = np.array([float(xi) for xi in A[1:]])
            self.Nodes.append(Node(Id,Coord))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        for i in range(int(line)):
            line = f.readline()
            self.Elements.append(Element(self.Nodes,line))
            
        self.computeElementCentroids()
        self.computeSurfaces()
        self.computeSurfacesCentroids()
        
                
    def computeElementCentroids(self):
        for el in self.Elements:
            el.computeCentroid()
    
    def computeSurfaces(self):
        self.SurfList = defaultdict(list)
        self.Surfaces=[]
        for el in self.Elements:
            # For Element Type see : http://gmsh.info/doc/texinfo/gmsh.html#MSH-ASCII-file-format
            if el.Type==2 : # [2,3,9,10,16,21,22,23,24,25] :
                self.SurfList[int(el.Surface)].append(el)
        for Id, Elmts in self.SurfList.iteritems():
            self.Surfaces.append(Surface(Id,Elmts))
    
    def computeSurfacesCentroids(self):
        for surf in self.Surfaces:
            surf.computeCentroid()
            
    def nearestNode(self,pt):
        NodesCoord = np.array([nd.Coord for nd in self.Nodes])
        if not hasattr(self, 'KDTreeNodes'):
            self.KDTreeNodes = spatial.KDTree(NodesCoord)
        distance,index = self.KDTreeNodes.query(pt)
        NearestNode = NodesCoord[index]
        return distance, NearestNode
        

class Node:
    
    def __init__(self,Id,Coord):
        self.Coord = Coord
        self.Id = Id

        
        
class Element:
#    Reprendre les nodes dans les elements
    def __init__(self, NodesList, *args):
        if len(args)==1 and isinstance(args[0], basestring) :
            self.Id, self.Type, self.Surface = [ int(args[0].split()[i]) for i in [0,1,4] ]
#            print(args[0].split()[5])
            self.Nodes = [NodesList[int(i)-1] for i in args[0].split()[5:]]
        elif  len(args)>1 :
            self.Id = args[0]
            self.Surface = args[2]
            self.Nodes = args[3]
            self.Area = None
            
    def computeCentroid(self):
        self.Centroid = np.mean([nd.Coord for nd in self.Nodes],axis=0)
    
    def computeArea(self):
        if self.Type==2 :
            nd1, nd2, nd3 = [nd.Coord for nd in self.Nodes[:3]]
            self.area = 0.5 * np.linalg.norm( np.cross( nd2-nd1, nd3-nd1 ))
        return self.area
#    
#class Element2D(Element):
#    
#    
#    
#    def area(self):
#        nd1, nd2, nd3 = [nd.Coord for nd in self.Nodes]
#        self.area = 0.5 * np.linalg.norm( np.cross( nd2-nd1, nd3-nd1 ))
#        
#        
        
class Surface:
    def __init__(self,Id,Elements):
        self.Id = Id
        self.Elements = Elements
        self.computeArea()
        self.computeCentroid()
        
    def computeArea(self):
        area = 0
        for el in self.Elements:
            area += el.computeArea()
        self.Area = area
    
    def computeCentroid(self):
        self.Centroid = 1/self.Area * np.sum([el.area*el.Centroid for el in self.Elements], axis = 0)
        
    
    
#def areas(a, b, c) :
#    
#    return 0.5 * np.linalg.norm( np.cross( b-a, c-a ))

        
    