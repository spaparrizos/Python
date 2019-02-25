#!/usr/bin/env python
#########################################################
# Spyros Paparrizos											       
# spipap@gmail.com       				              
# Calculate percentile									       
#########################################################

# Python libraries
import numpy as np, netCDF4, os, sys

# Generate data
a = np.array([1,2,3,4,5])

# Calculate percentile
perc = np.percentile(a, 50) # return 50th percentile, e.g median.

print "Percentile is: ", perc
