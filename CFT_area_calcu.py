import scipy.io as scio
import netCDF4 as nc
import numpy as np

def read_mat(file, var):
    data = scio.loadmat(file)
    vara = data[var]
    return vara

# def ncfile_create(file, varname, var):
#     ncfile = nc.Dataset(file, 'w', format='NETCDF4')
#     ncfile.createDimension('longitude', size=720)
#     ncfile.createDimension('latitude', size=360)
#     lon = ncfile.createVariable('lon', 'f4', dimensions='longitude')
#     lat = ncfile.createVariable('lat', 'f4', dimensions='latitude')
#     vara = ncfile.createVariable(varname, 'f4', dimensions=( 'latitude', 'longitude'))
#     lon[:] = LON[:]
#     lat[:] = LAT[:]
#     var
#     for i in range(360):
#         for j in range(720):
#             if j <= 359:
#                 vara[i, j+360] = var[j, 359 - i]
#             else:
#                 vara[i, j - 360] = var[j, 359 - i]
#     ncfile.close()

def ncfile_create(file, var):
    ncfile = nc.Dataset(file, 'a', format='NETCDF4')
    target = np.zeros([360, 720])
    for i in range(360):
        for j in range(720):
            if j <= 359:    # There are some mismatches between the raster and shapefile so we move all array # -1 to left (Japan)
                target[i, j + 360] = var[j, 359 - i]
            else:
                target[i, j - 360] = var[j, 359 - i]
    ncfile.variables['atotuse'][:,:] =  target[:,:]
    ncfile.close()

AREA_ALL_IRR = read_mat('C:\Research2\cft_calcu\\area_all_irr.mat', 'area_all_irr') # used the ISIMIP3a netcdf file, didn't know why the nc files I created do not work
AREA_SUR_IRR = read_mat('C:\Research2\cft_calcu\\area_sur_irr.mat', 'area_sur_irr')
AREA_SPR_IRR = read_mat('C:\Research2\cft_calcu\\area_spr_irr.mat', 'area_spr_irr')
AREA_DRI_IRR = read_mat('C:\Research2\cft_calcu\\area_dri_irr.mat', 'area_dri_irr')
LON = read_mat('C:\Research2\cft_calcu\\lon.mat', 'lon')
LAT = read_mat('C:\Research2\cft_calcu\\lat.mat', 'lat')

ncfile_create('C:\Research2\cft_calcu\\nc_files\\area_all_irr.nc', AREA_ALL_IRR)
print('area_all_irr.nc finished')
ncfile_create('C:\Research2\cft_calcu\\nc_files\\area_sur_irr.nc', AREA_SUR_IRR)
print('area_sur_irr.nc finished')
ncfile_create('C:\Research2\cft_calcu\\nc_files\\area_spr_irr.nc', AREA_SPR_IRR)
print('area_spr_irr.nc finished')
ncfile_create('C:\Research2\cft_calcu\\nc_files\\area_dri_irr.nc', AREA_DRI_IRR)
print('area_dri_irr.nc finished')






print('test')