# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:29:49 2017

@author: Jean-Baptiste RENAULT
"""

import os

cwd = os.getcwd()
files = os.listdir(cwd)

for f in files :
    if f.endswith('.txt') :
        os.rename(f,'_'.join(f.split("_")[0:4])+'.txt')
