# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:08:03 2017

@author: Jean-Baptiste RENAULT
"""
import numpy as np
from collections import defaultdict
import scipy.spatial as spatial
import re
import os


class Mesh:
    
    def __init__(self,file_adress):
        # adapt to relative or absolute path 
        adress_pattern = r'^(?:[\w]\:|\\&)'
        match = re.match(adress_pattern,file_adress)
        if not match :
            file_adress = os.getcwd() + '\\' + file_adress
        self.file_adress = file_adress
        self.name = file_adress.split('\\')[-1]
        self.line_list = defaultdict(list)
        self.nodes = []
        self.elements = []
        
#        self.elements1D = []
#        self.elements2D = []
#        self.elements3D = []
        
        f = open(file_adress,'r')
        starting_lines = [f.readline() for i in range(4)]
        line = f.readline()
        for i in range(int(line)):
            line = f.readline()
            starting_lines= line.split()
            Id = int(starting_lines[0])
            Coord = np.array([float(xi) for xi in starting_lines[1:]])
            self.nodes.append(Node(Id,Coord))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        for i in range(int(line)):
            line = f.readline()
            self.elements.append(Element(self.nodes,line))
        self.computeElementCentroids()
        self.computeSurfaces()
        self.computeSurfacesCentroids()
        
                
    def computeElementCentroids(self):
        for el in self.elements:
            el.computeCentroid()
    
    def computeSurfaces(self):
        self.SurfList = defaultdict(list)
        self.Surfaces=[]
        for el in self.elements:
            # For Element Type see : http://gmsh.info/doc/texinfo/gmsh.html#MSH-ASCII-file-format
            if el.Type==2 : # [2,3,9,10,16,21,22,23,24,25] :
                self.SurfList[int(el.Surface)].append(el)
        for Id, Elmts in self.SurfList.iteritems():
            self.Surfaces.append(Surface(Id,Elmts))
    
    def computeSurfacesCentroids(self):
        for surf in self.Surfaces:
            surf.computeCentroid()
            
    def nearestNode(self,pt):
        NodesCoord = np.array([nd.Coord for nd in self.nodes])
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
            self.nodes = [NodesList[int(i)-1] for i in args[0].split()[5:]]
        elif  len(args)>1 :
            self.Id = args[0]
            self.Surface = args[2]
            self.nodes = args[3]
            self.Area = None
            
    def computeCentroid(self):
        self.Centroid = np.mean([nd.Coord for nd in self.nodes],axis=0)
    
    def computeArea(self):
        if self.Type==2 :
            nd1, nd2, nd3 = [nd.Coord for nd in self.nodes[:3]]
            self.area = 0.5 * np.linalg.norm( np.cross( nd2-nd1, nd3-nd1 ))
        return self.area

        
class Surface:
    def __init__(self,Id,elements):
        self.Id = Id
        self.elements = elements
        self.computeArea()
        self.computeCentroid()
        
    def computeArea(self):
        area = 0
        for el in self.elements:
            area += el.computeArea()
        self.Area = area
    
    def computeCentroid(self):
        self.Centroid = 1/self.Area * np.sum([el.area*el.Centroid for el in self.elements], axis = 0)
        
    def connected_surfaces(self,surfaces_list):
        # find the neighbour, get the surface nodes and check if they also are
        # in the others 
        neighbour_surfaces = [self.Id]
        surface_node_IDs = set([nd for el in self.elements for nd in el.nodes])
        for surf in surfaces_list :
            surf_node_IDs = set([nd for el in surf.elements for nd in el.nodes])
            intersect_node_list = surface_node_IDs & surf_node_IDs
            if intersect_node_list :
                neighbour_surfaces.append(surf.Id)        
        return set(neighbour_surfaces)
    

        
    