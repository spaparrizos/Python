#!/usr/bin/env python
########################################################
# Spyros Paparrizos								       
# spyridon.paparrizos@lsce.ipsl.fr                     
########################################################

# The Kobayashi approach using Python on comparing simulated and observed values using mean squared deviation and its components
# Kobayashi K, Salam MU, 2001. Comparing Simulated and Measured Values Using Mean Squared Deviation and its Components, Journal 
#    of Agronomy, 92, 345-352. https://dl.sciencesocieties.org/publications/aj/abstracts/92/2/345?access=0&view=pdf  

import numpy as np

x = np.ma.array(np.random.random(100))			# 1st testing dataset
y = np.ma.array(np.random.random(100))			# 2nd testing dataset

# Kobayashi formula
def Kobayashi(x, y):
    xmean = x.mean(axis=0) 													
    ymean = y.mean(axis=0) 													
    SB = (xmean - ymean)**2
    SDs = ( ( (x - xmean)**2 ).mean(axis=0) )**0.5 							
    SDm = ( ( (y - ymean)**2 ).mean(axis=0) )**0.5 						
    r = ( (x - xmean)*(y - ymean) ).mean(axis=0) / (SDs*SDm) 				
    SDSD = (SDs - SDm)**2
    LCS = 2*SDs*SDm*(1 - r)
    if (1-r) < 0: print r; raw_input("NAN")
    return SB, SDSD, LCS

SB, SDSD, LCS = Kobayashi(x, y)
MSD = SB+SDSD+LCS

# Additional check whether the Kobayashi formula was correctly applied (MSD == RMSE**2)

def RMSE(x, y): 				# x and y need to have the same dimensions
    return ( ( (x - y)**2 ).mean(axis=0) )**0.5
    
RMSE = RMSE(x,y)
print "MSD (SB+SDSD+LCS) - RMSE**2 = 0, and here it is: ",(SB+SDSD+LCS - RMSE**2).sum()
