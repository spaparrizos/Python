#!/usr/bin/env python
#########################################################
# Spyros Paparrizos											       
# spipap@gmail.com    				           
# Earth area (for plots creation)							       
#########################################################

# Python libraries
import numpy as np

step = 0.5    # Running resolution

# Area calculation
area = 2 * 6.371229E6**2 * np.repeat(step, 360/step)[None,:] * np.pi/180 * np.sin(0.5 * np.repeat(step, 180/step)[:,None] * np.pi/180) * np.cos(np.arange(90 - step/2., -90, -step)[:,None] * np.pi/180)
