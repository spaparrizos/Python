#!/usr/bin/env python
#########################################################
# Spyros Paparrizos										       
# spipap@gmail.com                 
# Temperature transformation									       
#########################################################

# Python libraries
import numpy as np, netCDF4, os, sys

# Kelvin -> Celcius
Kelvin = float(input("Temperature in Kelvin (K) : "))
Celsius = Kelvin - 273.15
print "Temperature in Kelvin (K):", Kelvin,"(K)","\nTemperature is Celsius degrees: ", Celsius, "(oC)"


# Fahrenheit -> Celcius
Fahrenheit = int(raw_input("Temperature is oF (F) : "))
Celsius = (Fahrenheit - 32) * 5.0/9.0 
print "Temperature in Fahrenheit (F):", Fahrenheit,"(F)","\nTemperature is Celsius degrees: ", Celsius, "(oC)"
