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


# OPTIONAL: filter zeros (e.g. oceans, etc.)
var = np.ma.where(var == 0, np.ma.masked, var)

cmap = matplotlib.colors.LinearSegmentedColormap("my_colormap", rainbow, 20)
cmap_dif = matplotlib.colors.ListedColormap(["#874773", "#a36996", "#be92ba", "#1963b0", "#528ac7", "#7aadde", "#EEEEEE", "#4db363", "#8fc987", "#c9dfab", "#f0912e", "#e8601c", "#db050d"])

# FIGURE
m = Basemap(projection='mill', llcrnrlat=-60.1, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
#cmap = plt.cm.seismic # for difference maps it's better to use 'plt.cm.seismic' (color map)
cmesh = m.pcolormesh(lons, lats, var.mean(axis=0), shading="flat", cmap=cmap, latlon=True, vmin = vmin, vmax = vmax)
cbar = m.colorbar(cmesh, pad = 0.08)
info = "Mean = %.3g\nMax = %.3g" % (var.mean(), var.max())
plt.annotate(info, xy=(0.05, 0.05), xycoords='axes fraction')
plt.title("Title")

plt.savefig("07_figure_title", dpi=600)
plt.show()
plt.clf() # clear command

