import netCDF4 as nc
import numpy as np


ncfile = nc.Dataset('C:\Research2\ISIMIP3a_test\\atotuse_1996_2015_yearmean_timmean.nc', 'a', format='NETCDF4')

var = ncfile.variables['atotuse']
var_data = np.array(var)

target = np.zeros([1, 360, 720])
for i in range(360):
    for j in range(720):
        if j > 718:
            target[:,:,j] = var_data[:,:,719-j]
        else:
            target[:, :, j] = var_data[:, :, j+1]

ncfile.variables['atotuse'][:,:,:] =  target[:,:,:]
ncfile.close()
print('test')