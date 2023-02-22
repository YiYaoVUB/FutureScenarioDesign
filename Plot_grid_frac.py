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

def get_data_from_mat(file, variable):
    var_dict = scio.loadmat(file)
    var = var_dict[variable]
    var1 = var[:,29:,0,2].T
    var2 = var[:,29:,5,2].T
    var3 = var[:,29:,12,2].T
    var4 = var[:,29:,18,2].T
    var5 = var[:,29:,0,1].T
    var6 = var[:,29:,5,1].T
    var7 = var[:,29:,12,1].T
    var8 = var[:,29:,18,1].T
    return var1, var2, var3, var4, var5, var6, var7, var8

ssp126_2010_drip, ssp126_2035_drip, ssp126_2070_drip, ssp126_2100_drip, ssp126_2010_spri, ssp126_2035_spri, ssp126_2070_spri, ssp126_2100_spri = get_data_from_mat(
'C:\Research2\Output_data\\grid_frac_ssp126.mat', 'grid_frac')

ssp370_2010_drip, ssp370_2035_drip, ssp370_2070_drip, ssp370_2100_drip, ssp370_2010_spri, ssp370_2035_spri, ssp370_2070_spri, ssp370_2100_spri = get_data_from_mat(
'C:\Research2\Output_data\\grid_frac_ssp370.mat', 'grid_frac')

ssp585_2010_drip, ssp585_2035_drip, ssp585_2070_drip, ssp585_2100_drip, ssp585_2010_spri, ssp585_2035_spri, ssp585_2070_spri, ssp585_2100_spri = get_data_from_mat(
'C:\Research2\Output_data\\grid_frac_ssp585.mat', 'grid_frac')


f = plt.figure(figsize = (15, 10), dpi=100)  # initiate the figure
f.subplots_adjust(hspace=0.05, wspace=0.05, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

#cbar.set_label('$\Delta$ LHF ($\mathregular{W/m^2}$)',fontsize = 12)
#ticklabs = cbar.ax.get_xticklabels()
#cbar.ax.set_xticklabels(ticklabs, fontsize=12)
#plt.title('Latent heat flux (IRR - CTL)')




def plot_map(ax, index, data, title, title1):
    ax.text(0.01,0.92,index,color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
    ax.coastlines(linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
    ax.add_feature(cfeature.OCEAN, color='lightgrey')
    cmap = 'BrBG'
    bwr = mpl.cm.get_cmap('YlGn')
    colors = ['white', bwr(0.2), bwr(0.3), bwr(0.4), bwr(0.5), bwr(0.6), bwr(0.7), bwr(0.8), bwr(0.9)]
    cmap_bias1 = mpl.colors.ListedColormap(colors)
    bounds = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    norm_bias1 = mpl.colors.BoundaryNorm(bounds, cmap_bias1.N, extend='both')

    h = ax.pcolormesh(data_lon, data_lat, data, cmap=cmap_bias1, rasterized=True,
                       norm=norm_bias1)
    plt.title(title, loc= 'right')
    plt.title(title1, loc='left')
    return h, cmap



data_surface = Data_from_nc('C:\Research1\Final_data\\surfdata_irrigation_method.nc')   #load the data
data_irrigation_method = data_surface.load_variable('irrigation_method')
data_lon = data_surface.load_variable('LONGXY')
data_lon = data_lon[0,:]
data_lat = data_surface.load_variable('LATIXY')
data_lat = data_lat[:,0]
data_lat = data_lat[29:]

ax1 = plt.subplot(4, 3, 2, projection=ccrs.PlateCarree())
h, cmap = plot_map(ax1, 'a', ssp126_2010_drip, '2010', 'drip')

cbar = f.colorbar(h, ax=ax1, cmap=cmap,
                      spacing='uniform',
                      orientation='horizontal',
                      extend='both', shrink=1, pad=0.02, aspect=50, alpha=0)

ax1 = plt.subplot(4, 3, 4, projection=ccrs.PlateCarree())
plot_map(ax1, 'b', ssp126_2035_drip, 'ssp126_2035', 'drip')

ax1 = plt.subplot(4, 3, 7, projection=ccrs.PlateCarree())
plot_map(ax1, 'c', ssp126_2070_drip, 'ssp126_2070', 'drip')

ax1 = plt.subplot(4, 3, 10, projection=ccrs.PlateCarree())
plot_map(ax1, 'd', ssp126_2100_drip, 'ssp126_2100', 'drip')

ax1 = plt.subplot(4, 3, 5, projection=ccrs.PlateCarree())
plot_map(ax1, 'e', ssp370_2035_drip, 'ssp370_2035', 'drip')

ax1 = plt.subplot(4, 3, 8, projection=ccrs.PlateCarree())
plot_map(ax1, 'f', ssp370_2070_drip, 'ssp370_2070', 'drip')

ax1 = plt.subplot(4, 3, 11, projection=ccrs.PlateCarree())
plot_map(ax1, 'g', ssp370_2100_drip, 'ssp370_2100', 'drip')

ax1 = plt.subplot(4, 3, 6, projection=ccrs.PlateCarree())
plot_map(ax1, 'h', ssp585_2035_drip, 'ssp585_2035', 'drip')

ax1 = plt.subplot(4, 3, 9, projection=ccrs.PlateCarree())
plot_map(ax1, 'j', ssp585_2070_drip, 'ssp585_2070', 'drip')

ax1 = plt.subplot(4, 3, 12, projection=ccrs.PlateCarree())
plot_map(ax1, 'k', ssp585_2100_drip, 'ssp585_2100', 'drip')


plt.show()