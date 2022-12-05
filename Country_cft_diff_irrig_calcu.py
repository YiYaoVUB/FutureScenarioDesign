import pandas as pd
import csv
import numpy as np
import scipy.io as scio
import netCDF4 as nc

sprinkler_list = [4,6,8,12,14,16,18,32,36,38,46,50,52,54,58,60,62]
drip_list = [10,20,22,24,26,28,30,34,40,42,44,56,64]
flood_list = [48]

sprinkler_area = np.zeros([288, 192, 100])
for cft in sprinkler_list:
    data_PCT_CFT_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP370\AREA_CFT_' + str(cft) + '.mat')
    data_PCT_CFT = data_PCT_CFT_dict['area_cft']
    sprinkler_area = sprinkler_area + data_PCT_CFT

drip_area = np.zeros([288, 192, 100])
for cft in drip_list:
    data_PCT_CFT_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP370\AREA_CFT_' + str(cft) + '.mat')
    data_PCT_CFT = data_PCT_CFT_dict['area_cft']
    drip_area = drip_area + data_PCT_CFT

flood_area = np.zeros([288, 192, 100])
for cft in flood_list:
    data_PCT_CFT_dict = scio.loadmat('C:\Research2\PCT_CFT_AREA\SSP370\AREA_CFT_' + str(cft) + '.mat')
    data_PCT_CFT = data_PCT_CFT_dict['area_cft']
    flood_area = flood_area + data_PCT_CFT

all_area = sprinkler_area + drip_area + flood_area
sprinkler_frac = sprinkler_area / all_area
drip_frac = drip_area / all_area
flood_frac = flood_area / all_area
print('test')