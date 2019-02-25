#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spyridon.paparrizos@lsce.ipsl.fr                     
# Line customization: Paths files + nc.variables       
########################################################

# Python libraries
import numpy as np, netCDF4, os, sys
from netCDF4 import Dataset

# Paths files
path_nc_1 = "/yourfilename_1.nc"
path_nc_2 = "/yourfilename_2.nc"


# Read file 1
nc = netCDF4.Dataset(path_nc_1, "r")
var1 = nc.variables["CH4"][:]
nc.close()

# Read file 2
nc = netCDF4.Dataset(path_nc_2, "r")
var2 = nc.variables["CH4"][:]
nc.close()


###  Check equality  ###
SUM = var1 - var2
print "SUM (must be different than 0), and here is: ", SUM.mean()
print "For year ", year, "var1 sum is: ", var1.sum(), "    var2 sum is: ", var2.sum()
