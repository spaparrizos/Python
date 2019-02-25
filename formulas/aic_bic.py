#!/usr/bin/env python
#########################################################
# Spyros Paparrizos											       
# spyridon.paparrizos@lsce.ipsl.fr       				           
# AIC / BIC functions for Python							       
#########################################################
# HELP source: https://www.reddit.com/r/statistics/comments/5h2rbw/does_python_have_a_package_for_aicbic/

# Python libraries
import numpy as np
from scipy.optimize import curve_fit

# Generate data
n=10 								# number of observations
k= 2 								#number of variables (var_y, var_x1)
var_x1 = np.random.rand(10)
var_y = np.random.rand(10)

# Calculate AIC + BIC elements
resid = var_y - var_x1
sse = (resid**2).sum()
s2 = sse / n
L = ( 1.0/np.sqrt(2*np.pi*s2) ) ** n * np.exp( -sse/(s2*2.0) )

# AIC
AIC= 2*k - 2*np.log(L)
print "AIC", AIC

# BIC
BIC = k*np.log(n) - 2*np.log(L)
print "BIC", BIC
