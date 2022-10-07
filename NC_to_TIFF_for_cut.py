# -*- coding: utf-8 -*-
import numpy as np
import netCDF4 as nc
from osgeo import gdal, osr, ogr
import glob
import os
import shutil
import rasterio


def NC_to_tiffs(data, out_path):
    coord = 4326  # coordination, ["EPSG","4326"]
    nc_data_obj = nc.Dataset(data)

    key = list(nc_data_obj.variables.keys())  # get the information of longitude, latitude and other information
    print('the features: ', key)
    lon_size = [i for i, x in enumerate(key) if (x.find('lon'.upper()) != -1 or x.find('lon'.lower()) != -1)][
        0]  # get the longitude name
    lat_size = [i for i, x in enumerate(key) if (x.find('lat'.upper()) != -1 or x.find('lat'.lower()) != -1)][
        0]  # get the latitude name
    key_band = key[len(key) - 1]  # the band name
    key_lon = key[lon_size]
    key_lat = key[lat_size]
    Lon = nc_data_obj.variables[key_lon][:]
    Lat = nc_data_obj.variables[key_lat][:]
    Band = np.asarray(nc_data_obj.variables[key_band])

    LonMin, LatMax, LonMax, LatMin = [Lon.min(), Lat.max(), Lon.max(), Lat.min()]

    # calculate the resolution
    N_Lat = len(Lat)
    N_Lon = len(Lon)
    Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
    Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)

    # create .tif file
    driver = gdal.GetDriverByName('GTiff')
    out_tif_name = out_path + os.sep + data.split('\\')[-1][:-3] + '.tif'
    out_tif = driver.Create(out_tif_name, N_Lon, N_Lat, 1, gdal.GDT_Float32)

    # set the limitation of the image

    geotransform = (LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res)
    out_tif.SetGeoTransform(geotransform)

    # get the coordination
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(coord)  # AUTHORITY["EPSG","4326"]
    out_tif.SetProjection(srs.ExportToWkt())

    # for missing value
    Band[Band[:, :] > 100000] = -999

    # write the data
    if Band.ndim == 2:  # if it is two-dimension, no change
        a = Band[:, :]
    else:  # transfer three dimension to two dimension
        a = Band[0, :, :]

    reversed_arr = a
    out_tif.GetRasterBand(1).WriteArray(reversed_arr)
    out_tif.GetRasterBand(1).SetNoDataValue(-999)
    out_tif.FlushCache()
    del out_tif


def nc_to_tif(Input_folder):
    Output_folder = os.path.split(Input_folder)[0] + os.sep + 'out_' + os.path.split(Input_folder)[1]
    # read all nc data
    data_list = glob.glob(Input_folder + os.sep + '*.nc')
    print("input folder is: ", Input_folder)
    print("the file read：", data_list)
    #     if not os.path.isdir(Output_folder):
    if os.path.exists(Output_folder):
        shutil.rmtree(Output_folder)  # if exist, remove the folder
    os.makedirs(Output_folder)  # recreate it
    for i in range(len(data_list)):
        dat = data_list[i]
        NC_to_tiffs(data=dat, out_path=Output_folder)
        print(dat + '-----successfully')
    print(f"input folder: {Input_folder}")
    print("--------------------------")
    print(f'output folder: {Output_folder}')


'''you need to fill in the directory where you store the nc file'''

nc_to_tif(Input_folder=r'C:\Research2\ISIMIP3b_data\TWS')