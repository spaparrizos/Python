########################################################
# Spyros Paparrizos								      
# sipap@gmail.com                 
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
NORTH = 0									# northern latitude limit (on the top of the block - urcrnrlat)	-> Global analysis: 90 
SOUTH = -90									# southern latitude limit (on the bottom of the block - llcrnrlat) -> Global analysis: -90 (-60.05: excluding Antarctica)
WEST = 0									# western longitude limit (on the left side of the block - llcrnrlon) -> Global analysis: -180
EAST = 180									# eastern longitude limit (on the right side of the block - urcrnrlon)	-> Global analysis: 180
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


# Introduce mask
region_mask = np.zeros((nlat,nlon))
ilat = np.where((lat <= NORTH) & (lat >= SOUTH))
ilon = np.where((lon >= WEST) & (lon <= EAST))
ilon, ilat = np.meshgrid(ilon[0], ilat[0])
region_mask[ilat, ilon] = 1
#region_mask = region_mask[np.newaxis,:,:].repeat(nyears, axis=0)



# Function for drawing a specific polygon on a map
def draw_screen_poly( lats, lons, m):
    x, y = m( lons, lats )
    xy = zip(x,y)
    poly = Polygon( xy, facecolor='red', alpha=0.4 )
    plt.gca().add_patch(poly)


# FIGURE
# Example for 90N - 60N
lats = [ 90, 0, 0, 90 ]
lons = [ 0, 0, 180, 180 ]
m = Basemap(projection='mill', llcrnrlat=SOUTH, urcrnrlat=NORTH, llcrnrlon=WEST, urcrnrlon=EAST, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )

plt.savefig("Regions.png", dpi=150)
plt.clf() # clear command


# Rest examples
"""
# 60N - 30N
lats = [ 60, 30, 30, 60 ]
lons = [ -180, -180, 180, 180 ]
m = Basemap(projection='mill',llcrnrlat=-60.05, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )
#plt.title("%s for %s\n%s" % (label1, label4, label3))
plt.savefig("02_Poly60N-30N.png", dpi=600)
plt.clf() # clear command

# 30N - 00N
lats = [ 30, 0, 0, 30 ]
lons = [ -180, -180, 180, 180 ]
m = Basemap(projection='mill',llcrnrlat=-60.05, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )
#plt.title("Region 30N - 0N")
plt.savefig("Regions.png", dpi=150)
plt.clf() # clear command

# 00S - 30S
lats = [ 0, -30, -30, 0 ]
lons = [ -180, -180, 180, 180 ]
m = Basemap(projection='mill',llcrnrlat=-60.05, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )
#plt.title("Region 0S - 30S")
plt.savefig("Regions.png", dpi=150)
plt.clf() # clear command

# 30S - 60S
lats = [ -30, -60, -60, -30 ]
lons = [ -180, -180, 180, 180 ]
m = Basemap(projection='mill',llcrnrlat=-60.05, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )
#plt.title("Region 30S - 60S")
plt.savefig("Regions.png", dpi=150)
plt.clf() # clear command

# 60S - 90S
lats = [ -60, -90, -90, -60 ]
lons = [ -180, -180, 180, 180 ]
m = Basemap(projection='mill',llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines(linewidth=0.5)
m.drawparallels([-80,-60,-30,0,30,60,80], labels=[1, 0, 1, 1])
m.drawmeridians(np.arange(0., 420., 60.), labels=[0, 0, 0, 1])
m.drawmapboundary()
draw_screen_poly( lats, lons, m )
#plt.title("Region 60S - 90S")
plt.savefig("Regions.png", dpi=150)
plt.clf() # clear command
"""


