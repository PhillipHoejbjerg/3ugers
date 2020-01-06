#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:01:05 2019

@author: AlbertoK
"""

import numpy as np
import math

def calc_errors(Mtrue, Mobs):
    
    rows = len(Mtrue[:,0])
    col = len(Mtrue[0,:])
    MSE = []
    
    
    for i in range(rows):
        for j in range(col):
            err = abs(Mtrue[i,j]-Mobs[i,j])
        
        a = (Mtrue[i,0]-Mobs[i,0])**2
        MSE.append(a)
    
    MSE = 1/rows * np.sum(MSE)
    
    
    return MSE