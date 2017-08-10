#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spyridon.paparrizos@lsce.ipsl.fr                     			       
########################################################
import netCDF4, numpy as np
from mpl_toolkits.basemap import maskoceans

step = 0.5	# current grid resolution
lat = np.arange(90 - step/2., -90, -step)
lon = np.arange(-180 + step/2., 180, step)
lons, lats = np.meshgrid(lon, lat)

# create mask of 0's/1's (0: oceans, 1: land) 
LSM = np.ma.ones((nlat, nlon))
LSM = maskoceans(lons, lats, LSM, inlands = False, resolution = "f", grid = 1.25) # inlands refers to the inland waters and whether the user desires to mask them (True or False)

# filter your data
filtered_data = maskoceans(lons, lats, data, inlands = False, resolution = "f", grid = 1.25)
