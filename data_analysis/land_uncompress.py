#!/usr/bin/env python
########################################################
# Spyros Paparrizos								     
# spipap@gmail.com
# Line customization: 11 (all Preconditions)	      
########################################################

# Python libraries
import numpy as np, netCDF4

# Preconditions
Ybegin = 2010
Yend = 2016
step = 0.5									# in degrees
mf = 1E20									# missing value
nlat = int(180 / step)
nlon = int(360 / step)
nmonths = 12
ndays = 365
nhours = 24 * ndays
ntime = (nyears * nmonths)
years = range(Ybegin,Yend+1)
nyears=len(years)
 

# Input compressed file
pathin_nc = "/yourinfilename.nc"

# Output uncompressed file
pathout_nc = "/yourinfilename_uncompressed.nc"


# Compressed variables included in the input compressed netCDF file and need to be uncompressed
atmvars = ["Tair", "PSurf", "Qair", "LWdown", "SWdown", "Wind_E", "Wind_N", "Snowf", "Rainf"]


# netCDF file creation and filling with the uncompressed variables
for year in years:
    print year
    
    # Read 'land' elements in compressed file
    nc = netCDF4.Dataset(pathin_nc % dict(year = year))
    nlon = len(nc.dimensions["x"])
    nlat = len(nc.dimensions["y"])
    ntime = len(nc.dimensions["tstep"])
    land = nc.variables["land"][:] - 1
    
    # Creation of nc dimensions
    ncout = netCDF4.Dataset(pathout_nc % dict(year = year), "w")
    ncout.createDimension("tstep", None)
    ncout.createDimension("lon", nlon)
    ncout.createDimension("lat", nlat)
    
    # Creation of nc variables
    ncout.createVariable("lon", "f4", ("lon",))
    ncout.createVariable("lat", "f4", ("lat",))
    ncout.variables["lon"][:] = nc.variables["nav_lon"][0,:]
    ncout.variables["lat"][:] = nc.variables["nav_lat"][:,0]

    ncout.createVariable("time", "f8", ("tstep",))
    ncout.variables["time"].setncatts(nc.variables["time"].__dict__)
    ncout.variables["time"][:] = nc.variables["time"][:]

    for var in atmvars:
        print var
        ncout.createVariable(var, nc.variables[var].dtype, ("tstep", "lat", "lon"), fill_value = mf)
        readdata = nc.variables[var][:]
        vardata = np.ma.masked_all((ntime, nlat*nlon))
        vardata[:, land] = readdata
        ncout.variables[var][:] = vardata.reshape((ntime, nlat, nlon))

    nc.close()
    ncout.close()

    © 2019 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

