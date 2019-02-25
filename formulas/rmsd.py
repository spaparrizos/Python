#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spipap@gmail.com                     
# RMSD function for Python					       
########################################################
import numpy as np

def RMSD(x, y, axis = None):
    return ( ( (x - y)**2 ).mean() )**0.5
    
# EXAMPLE
dataset1 = np.random.random((2,3,5))
dataset2 = np.random.random((2,3,5))

print "RMSD of dataset1 Vs dataset2 is:", RMSD(dataset1.mean(axis=0),dataset2.mean(axis=0))
