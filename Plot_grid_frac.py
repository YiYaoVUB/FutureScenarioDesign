import csv
import numpy as np
import scipy.io as scio
import matplotlib.pyplot as plt
import matplotlib as mpl
from Load_data import Data_from_nc
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import numpy as np
import time
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import colors as cls

grid_frac_ssp126_dict = scio.loadmat('C:\Research2\Output_data\\grid_frac_ssp126.mat')
grid_frac_ssp126 = grid_frac_ssp126_dict['grid_frac']
grid_frac_ssp126_2010_drip = grid_frac_ssp126 [:,29:,0,2]
grid_frac_ssp126_2035_drip = grid_frac_ssp126 [:,29:,5,2]
grid_frac_ssp126_2070_drip = grid_frac_ssp126 [:,29:,12,2]
grid_frac_ssp126_2100_drip = grid_frac_ssp126 [:,29:,18,2]

grid_frac_ssp126_2010_spri = grid_frac_ssp126 [:,29:,0,1]
grid_frac_ssp126_2035_spri = grid_frac_ssp126 [:,29:,5,1]
grid_frac_ssp126_2070_spri = grid_frac_ssp126 [:,29:,12,1]
grid_frac_ssp126_2100_spri = grid_frac_ssp126 [:,29:,18,1]

grid_frac_ssp370_dict = scio.loadmat('C:\Research2\Output_data\\grid_frac_ssp370.mat')
grid_frac_ssp370 = grid_frac_ssp370_dict['grid_frac']
grid_frac_ssp370_2010_drip = grid_frac_ssp370 [:,29:,0,2]
grid_frac_ssp370_2035_drip = grid_frac_ssp370 [:,29:,5,2]
grid_frac_ssp370_2070_drip = grid_frac_ssp370 [:,29:,12,2]
grid_frac_ssp370_2100_drip = grid_frac_ssp370 [:,29:,18,2]

grid_frac_ssp370_2010_spri = grid_frac_ssp370 [:,29:,0,1]
grid_frac_ssp370_2035_spri = grid_frac_ssp370 [:,29:,5,1]
grid_frac_ssp370_2070_spri = grid_frac_ssp370 [:,29:,12,1]
grid_frac_ssp370_2100_spri = grid_frac_ssp370 [:,29:,18,1]

grid_frac_ssp585_dict = scio.loadmat('C:\Research2\Output_data\\grid_frac_ssp585.mat')
grid_frac_ssp585 = grid_frac_ssp585_dict['grid_frac']
grid_frac_ssp585_2010_drip = grid_frac_ssp585 [:,29:,0,2]
grid_frac_ssp585_2035_drip = grid_frac_ssp585 [:,29:,5,2]
grid_frac_ssp585_2070_drip = grid_frac_ssp585 [:,29:,12,2]
grid_frac_ssp585_2100_drip = grid_frac_ssp585 [:,29:,18,2]

grid_frac_ssp585_2010_spri = grid_frac_ssp585 [:,29:,0,1]
grid_frac_ssp585_2035_spri = grid_frac_ssp585 [:,29:,5,1]
grid_frac_ssp585_2070_spri = grid_frac_ssp585 [:,29:,12,1]
grid_frac_ssp585_2100_spri = grid_frac_ssp585 [:,29:,18,1]

grid_frac_ssp126_2010_drip = grid_frac_ssp126_2010_drip.T
grid_frac_ssp370_2010_drip = grid_frac_ssp370_2010_drip.T
grid_frac_ssp585_2010_drip = grid_frac_ssp585_2010_drip.T
grid_frac_ssp126_2035_drip = grid_frac_ssp126_2035_drip.T
grid_frac_ssp126_2070_drip = grid_frac_ssp126_2070_drip.T
grid_frac_ssp126_2100_drip = grid_frac_ssp126_2100_drip.T
grid_frac_ssp370_2035_drip = grid_frac_ssp370_2035_drip.T
grid_frac_ssp370_2070_drip = grid_frac_ssp370_2070_drip.T
grid_frac_ssp370_2100_drip = grid_frac_ssp370_2100_drip.T
grid_frac_ssp585_2035_drip = grid_frac_ssp585_2035_drip.T
grid_frac_ssp585_2070_drip = grid_frac_ssp585_2070_drip.T
grid_frac_ssp585_2100_drip = grid_frac_ssp585_2100_drip.T

grid_frac_ssp126_2010_spri = grid_frac_ssp126_2010_spri.T
grid_frac_ssp370_2010_spri = grid_frac_ssp370_2010_spri.T
grid_frac_ssp585_2010_spri = grid_frac_ssp585_2010_spri.T
grid_frac_ssp126_2035_spri = grid_frac_ssp126_2035_spri.T
grid_frac_ssp126_2070_spri = grid_frac_ssp126_2070_spri.T
grid_frac_ssp126_2100_spri = grid_frac_ssp126_2100_spri.T
grid_frac_ssp370_2035_spri = grid_frac_ssp370_2035_spri.T
grid_frac_ssp370_2070_spri = grid_frac_ssp370_2070_spri.T
grid_frac_ssp370_2100_spri = grid_frac_ssp370_2100_spri.T
grid_frac_ssp585_2035_spri = grid_frac_ssp585_2035_spri.T
grid_frac_ssp585_2070_spri = grid_frac_ssp585_2070_spri.T
grid_frac_ssp585_2100_spri = grid_frac_ssp585_2100_spri.T



f = plt.figure(figsize = (6, 12), dpi=100)  # initiate the figure
#f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax1 = plt.subplot(3, 1, 1, projection=ccrs.PlateCarree())
#ax1 = plt.subplot(1, 1, 1)
#ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
ax1.add_feature(cfeature.OCEAN, color='lightgrey')

cmap='BrBG'
bwr = mpl.cm.get_cmap('YlGn')
colors = ['white',bwr(0.2),bwr(0.3),bwr(0.4),bwr(0.5),bwr(0.6),bwr(0.7),bwr(0.8),bwr(0.9)]
cmap_bias1 = mpl.colors.ListedColormap(colors)
bounds = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
norm_bias1 = mpl.colors.BoundaryNorm(bounds,cmap_bias1.N,extend='both')
#divider = make_axes_locatable(ax1)

data_surface = Data_from_nc('C:\Research1\Final_data\\surfdata_irrigation_method.nc')   #load the data
data_irrigation_method = data_surface.load_variable('irrigation_method')


data_lon = data_surface.load_variable('LONGXY')
data_lon = data_lon[0,:]
data_lat = data_surface.load_variable('LATIXY')
data_lat = data_lat[:,0]
data_lat = data_lat[29:]

h = ax1.pcolormesh(data_lon,data_lat,grid_frac_ssp126_2035_spri, cmap=cmap_bias1, rasterized=True, norm=norm_bias1)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
#cbar.set_label('$\Delta$ LHF ($\mathregular{W/m^2}$)',fontsize = 12)
#ticklabs = cbar.ax.get_xticklabels()
#cbar.ax.set_xticklabels(ticklabs, fontsize=12)
#plt.title('Latent heat flux (IRR - CTL)')

ax1 = plt.subplot(3, 1, 2, projection=ccrs.PlateCarree())
#ax1 = plt.subplot(1, 1, 1)
#ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
ax1.add_feature(cfeature.OCEAN, color='lightgrey')

cmap='BrBG'
bwr = mpl.cm.get_cmap('YlGn')
colors = ['white',bwr(0.2),bwr(0.3),bwr(0.4),bwr(0.5),bwr(0.6),bwr(0.7),bwr(0.8),bwr(0.9)]
cmap_bias1 = mpl.colors.ListedColormap(colors)
bounds = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
norm_bias1 = mpl.colors.BoundaryNorm(bounds,cmap_bias1.N,extend='both')
#divider = make_axes_locatable(ax1)

data_surface = Data_from_nc('C:\Research1\Final_data\\surfdata_irrigation_method.nc')   #load the data
data_irrigation_method = data_surface.load_variable('irrigation_method')


data_lon = data_surface.load_variable('LONGXY')
data_lon = data_lon[0,:]
data_lat = data_surface.load_variable('LATIXY')
data_lat = data_lat[:,0]
data_lat = data_lat[29:]

h = ax1.pcolormesh(data_lon,data_lat,grid_frac_ssp370_2035_spri, cmap=cmap_bias1, rasterized=True, norm=norm_bias1)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)

ax1 = plt.subplot(3, 1, 3, projection=ccrs.PlateCarree())
#ax1 = plt.subplot(1, 1, 1)
#ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
ax1.add_feature(cfeature.OCEAN, color='lightgrey')

cmap='BrBG'
bwr = mpl.cm.get_cmap('YlGn')
colors = ['white',bwr(0.2),bwr(0.3),bwr(0.4),bwr(0.5),bwr(0.6),bwr(0.7),bwr(0.8),bwr(0.9)]
cmap_bias1 = mpl.colors.ListedColormap(colors)
bounds = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
norm_bias1 = mpl.colors.BoundaryNorm(bounds,cmap_bias1.N,extend='both')
#divider = make_axes_locatable(ax1)

data_surface = Data_from_nc('C:\Research1\Final_data\\surfdata_irrigation_method.nc')   #load the data
data_irrigation_method = data_surface.load_variable('irrigation_method')


data_lon = data_surface.load_variable('LONGXY')
data_lon = data_lon[0,:]
data_lat = data_surface.load_variable('LATIXY')
data_lat = data_lat[:,0]
data_lat = data_lat[29:]

h = ax1.pcolormesh(data_lon,data_lat,grid_frac_ssp585_2035_spri, cmap=cmap_bias1, rasterized=True, norm=norm_bias1)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)

plt.show()