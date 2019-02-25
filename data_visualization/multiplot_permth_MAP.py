########################################################
# Spyros Paparrizos								      
# spipap@gmail.com                 
# Line customization: 21 (all Preconditions)	      
########################################################

# Python libraries
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import netCDF4, warnings

rainbow = {"red"   : ((0., 0.53, 0.53), (0.077, 0.69, 0.69), (0.154, 0.84, 0.84), (0.231, 0.1,  0.1),  (0.308, 0.32, 0.32), (0.385, 0.48, 0.48), (0.462, 0.3,  0.3),  (0.539, 0.56, 0.56), (0.616, 0.79,  0.79),  (0.693, 0.965, 0.965), (0.77, 0.96, 0.96), (0.847, 0.94, 0.94), (0.924, 0.91,  0.91),  (1., 0.86, 0.86)),
           "green" : ((0., 0.18, 0.28), (0.077, 0.47, 0.47), (0.154, 0.75, 0.75), (0.231, 0.39, 0.39), (0.308, 0.54, 0.54), (0.385, 0.68, 0.68), (0.462, 0.7,  0.7),  (0.539, 0.79, 0.79), (0.616, 0.875, 0.875), (0.693, 0.93,  0.93),  (0.77, 0.75, 0.75), (0.847, 0.57, 0.57), (0.924, 0.375, 0.375), (1., 0.02, 0.02)),
           "blue"  : ((0., 0.45, 0.45), (0.077, 0.65, 0.65), (0.154, 0.87, 0.87), (0.231, 0.69, 0.69), (0.308, 0.78, 0.78), (0.385, 0.87, 0.87), (0.462, 0.39, 0.39), (0.539, 0.53, 0.53), (0.616, 0.67,  0.67),  (0.693, 0.33,  0.33),  (0.77, 0.25, 0.25), (0.847, 0.18, 0.18), (0.924, 0.11,  0.11),  (1., 0.05, 0.05))}
cmap = matplotlib.colors.LinearSegmentedColormap("my_colormap", rainbow, 20)
mnths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Preconditions
path_nc = "/yourfilename.nc"
Ybegin = 2010
Yend = 2016
step = 0.5									# in degrees
vmin = 0 									# Minimun extend of map barplot
vmax = 3									# Maximum extend of map barplot
nlat = int(180 / step)
nlon = int(360 / step)
nmonths = 12
ndays = 365
nhours = 24 * ndays
years = range(Ybegin,Yend+1)
nyears=len(years)


# Read netCDF file
nc = netCDF4.Dataset(path_nc, "r")
lon = nc.variables["lon"][:]
lat = nc.variables["lat"][:]
var = nc.variables["CH4_e"][:]    # variable as it is in the netCDF file
ts1 = nc.variables["time"][:]
nc.close()
lons, lats = np.meshgrid(lon, lat)


# pythonic way to calculate monthly means
var_mth = var.reshape((nyears,nmonths,nlat,nlon)).mean(axis=0)
print "2. var_mth.shape is:",var_mth.shape

# FIGURE
fig = plt.figure()															# Introduce the figure
ax = plt.axes()   															# Introduce the axes
fig, ax = plt.subplots() 													# Introduce the subplots
ax.axis('off')    															# Necessary in order to remove the frame that is given by default in the figure
plt.text(0.5, 1.02, "Title", horizontalalignment = 'center', fontsize = 10)	# Title text + customizations

# Monthly mean maps
for mth in range(12):
    ax1 = fig.add_subplot(4,3,mth+1) 										# Introducing the subplot routine: (nrows, ncolumns, ncount[mth])
    ax1.axis('off')															# Removes the internal frames (optional - can be changed to 'on')
    fig.subplots_adjust(hspace = 0.3, wspace = 0.0001, left = 0.01)			# Adjust the subplots position (height - Width)
    
    # Eckert IV Projection
    m = Basemap(projection='eck4', lon_0 = 0,resolution = "c")
    
    m.drawcoastlines(linewidth=0.1)
    #m.drawparallels([-80,-60,-30,0,30,60,80])#, labels=[1, 0, 1, 1])		# Draws parallels on each map - (optional)
    #m.drawmeridians(np.arange(0., 420., 60.))#, labels=[0, 0, 0, 1])		# Draws meridians in each map - (optional)
    cmesh = m.pcolormesh(lons, lats, var_mth[mth], shading="flat", cmap="Reds", latlon=True, vmin = vmin, vmax = vmax) 
    info = "Mean = %.2g\nMax = %.2g" % (var_mth[mth].mean(axis=0).mean(), var_mth[mth].max())
    plt.annotate(info, xy=(0.005, 0.05), xycoords='axes fraction', fontsize = 4)
    plt.title("%s" % mnths[mth].upper(), x=0.08, y = 0.2, fontsize = 6) 	# Subplots customization
    
cbar = plt.colorbar(ax=ax, pad = 0.08, orientation = 'vertical', fraction = 0.04)	# Introducing + customizing colorbar  
plt.savefig("figure_title.png", dpi=300)
plt.clf() 


