#!/usr/bin/env python
#########################################################
# Spyros Paparrizos											       
# spipap@gmail.com       				          
# Multi-Linear Regression (MLR)									       
#########################################################

# Python libraries
import numpy as np, netCDF4, os, sys
import statsmodels.api as sm
from sklearn import linear_model

##############
# Method 1
# Install statsmodels first on obelix for example:
# pip install --target=/home/orchidee04/vnaipal/ statsmodels-0.8.0.tar.gz
# You can download statsmodels-0.8.0.tar.gz at https://github.com/statsmodels/statsmodels/tags
##############

# Generate data
y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]

ys = np.array([1,4,5,2,8,5,10,2])
xs = np.array([5,6,7,8,10,11,13,5])


def reg_m(y, x):
    #ones = np.ones(len(x[0]))
    #X = sm.add_constant(np.column_stack((x[0], ones))) #add constant
    #for ele in x[1:]:
        #X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

print reg_m(y, x).summary() #print coefficients and all stats param


#################
# Method 2 
# (has no standard error, you will need to compare the predicted & original Y values to calculate the error)
################

# Generate data
y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]

# MLR
x=np.asarray(x)
y=np.asarray(y)
ones = np.ones(len(x[0]))
#add constant
X = np.column_stack((x[0], ones))
for ele in x[1:]:
  X = np.column_stack((ele, X))
#calculate coefficients
clf=linear_model.LinearRegression(fit_intercept=True)
clf.fit([X[i] for i in range(23)],[y[i] for i in range(23)])
clf.coef_ #print coefficients: x3,x2,x1
