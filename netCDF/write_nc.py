#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spipap@gmail.com                   
# Write elements to netCDF						       
########################################################

# Python libraries
import numpy as np, netCDF4, os, sys
from netCDF4 import Dataset


step = 0.5									# in degrees
nlat = int(180 / step)
nlon = int(360 / step)
nmonths = 12
ndays = 365
nhours = 24 * ndays
years = range(Ybegin,Yend+1)
nyears=len(years)


# Write netCDF  
pathout = "./new_path_nc.nc"                 # Desired path (and name) where the netCDF file will be saved in your local disks

# Open and start writting... 
ncout = netCDF4.Dataset(pathout, "w")

# create dimensions
ncout.createDimension("tstep", None)
ncout.createDimension("lat", nlat)
ncout.createDimension("lon", nlon)

# create variables
ncout.createVariable("lat", "f8", ("lat"))
ncout.createVariable("lon", "f8", ("lon"))
ncout.createVariable("time", "f4", ("tstep",))
ncout.createVariable(varname, "f8", ("tstep", "lat", "lon"))

# write data
lat = np.arange(90 - step/2., -90, -step)
lon = np.arange(-180 + step/2., 180, step)
ncout.variables["lat"][:] = lat
ncout.variables["lon"][:] = lon

# write data atributes
ncout.variables["time"].setncatts(dict(title = "Time", units = "seconds since %s-01-01 00:00:00" % year, calendar = "noleap", tstep_sec = 60.*60.))
ncout.variables[varname][:] = var # name of the variable (for example as it was read from the netCDF we want to extract it)
ncout.close()
