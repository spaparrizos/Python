#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spyridon.paparrizos@lsce.ipsl.fr                     
# Line customization: 14						       
########################################################
import numpy as np
import netCDF4

path = "/path.nc"                  # Desired path where the netCDF file is located in your local disks

nc = netCDF4.Dataset(path, "r")
lon = nc.variables["lon"][:]      # Will obtain the longitude dimension
lat = nc.variables["lat"][:]      # Will obtain the latitude dimension
var = nc.variables["var"][:]      # Name of the variable as it is named within the netCDF file
ts = nc.variables["time"][:]
nc.close()
