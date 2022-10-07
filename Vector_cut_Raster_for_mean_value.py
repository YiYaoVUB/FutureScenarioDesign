import csv
import os
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import rasterstats
from rasterio.plot import show
# show() can plot the raster file
from rasterio.plot import show_hist

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


# geopandas read the shape file
districts = gpd.read_file('C:\Shapefile\world-administrative-boundaries\world-administrative-boundaries.shp')

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.tif'):
                fullname = os.path.join(root, f)
                yield fullname

base = 'C:\Research2\ISIMIP3b_data\out_TWS\\'
for name in findAllFile(base):
    # read the raster file
    output = name + '.csv'
    raster = rasterio.open(name)

    # plot them on one figure
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 20

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    show(raster, ax=ax1, title='Rainfall')
    # plot()
    districts.plot(ax=ax1, facecolor='None', edgecolor='red')
    show_hist(raster, ax=ax2, title='hist')

    #plt.show()

    rainfall_data = raster.read(1)

    # for coordination
    affine = raster.transform


    # First parameter is raster region, second is raster file, third is the coordination and the fourth is the statistic (you can also choose min or max)
    avg_rallrain = rasterstats.zonal_stats(districts, rainfall_data, affine=affine, stats=['mean'], geojson_out=True)
    # avg_rallrain
    #print(avg_rallrain)_
    result = []
    for i in range(len(avg_rallrain)):
        result.append(avg_rallrain[i]['properties'])
    labels = ['color_code', 'continent', 'french_shor', 'iso3', 'iso_3166_1_', 'name', 'region', 'status', 'mean']
    try:
        with open(output, 'w', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writeheader()
            for elem in result:
                writer.writerow(elem)
    except IOError:
        print("I/O error")

