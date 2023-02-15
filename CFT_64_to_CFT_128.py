import netCDF4 as nc

file_PCT_CFT_old = nc.Dataset('C:\Research2\PCT_CFT_AREA\landuse.timeseries_0.9x1.25_SSP1-2.6_78pfts_CMIP6_simyr1850-2100_c181220_PCT_CFT.nc')
PCT_CFT_old = file_PCT_CFT_old.variables['PCT_CFT']





print('test')