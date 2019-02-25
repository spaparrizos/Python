#!/usr/bin/env python
#########################################################
# Spyros Paparrizos											       
# spipap@gmail.com      			             
# Correlation between 2 datasets						      
#########################################################

# Python libraries
import numpy as np, netCDF4, os, sys

# Generate random data (100 points)
var_x = np.random.rand(100)
var_y = np.random.rand(100)

# Correlation 
r2 = np.corrcoef(var_x.flatten(),  var_y.flatten())[1,0]
print "R-squared is: ", r2
