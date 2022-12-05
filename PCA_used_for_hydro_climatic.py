import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import joblib
import netCDF4 as nc

def read_csv_data_SSP(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

def normalize_data_with_standard(data_array, data_standard):
    data_after = [(x-min(data_standard)) / (max(data_standard) - min(data_standard)) for x in data_array]
    return data_after

P_hist = read_csv_data_SSP('C:\Research2\ISIMIP3a\out_file_1991_2010\pr_1991_2010_for_PCA.csv')
TWS_hist = read_csv_data_SSP('C:\Research2\ISIMIP3a\out_file_1991_2010\\tws_1991_2010_for_PCA.csv')

# P_hist = np.array(P_hist)
# TWS_hist = np.array(TWS_hist)

P_hist_after = normalize_data_with_standard(P_hist, P_hist)
TWS_hist_after = normalize_data_with_standard(TWS_hist, TWS_hist)

ref_X = np.array([P_hist_after , TWS_hist_after])
ref_X = np.squeeze(ref_X, axis=2)
ref_X = ref_X.T
pca = PCA(n_components=2)
pca.fit(ref_X)
ref_X_after_PCA = pca.fit_transform(ref_X)
joblib.dump(pca, 'pca.m')
ref_X_after_PCA = ref_X_after_PCA[:, 0]
ref_X_after_PCA = normalize_data_with_standard(ref_X_after_PCA, ref_X_after_PCA)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)

year_list = ['1996_2015', '2001_2020', '2006_2025', '2011_2030', '2016_2035', '2021_2040',
             '2026_2045', '2031_2050', '2036_2055', '2041_2060', '2046_2065', '2051_2070',
             '2056_2075', '2061_2080', '2066_2085', '2071_2090', '2076_2095', '2081_2100']

str_P_begin = 'C:\Research2\ISIMIP3a\\P_data\ssp126\\'
str_TWS_begin = 'C:\Research2\ISIMIP3a\\TWS_data\ssp126\\ssp126_'

str_P_end = '_ensmean_ssp126_timmean.nc_remapcon.nc'
str_TWS_end = '_ensmean.nc_remapcon.nc'


for str_year in year_list:
    data_after_PCA = np.zeros([288, 192])

    str_P_file = str_P_begin + str_year + str_P_end
    str_TWS_file = str_TWS_begin + str_year + str_TWS_end

    file_obj_P = nc.Dataset(str_P_file)
    P_data = file_obj_P.variables['pr']
    var_P = np.array(P_data)

    file_obj_TWS = nc.Dataset(str_TWS_file)
    TWS_data = file_obj_TWS.variables['tws']
    var_TWS = np.array(TWS_data)

    for i in range(288):
        #for j in range(192):
        P_proj_after = normalize_data_with_standard(var_P[0, :, i], P_hist)
        TWS_proj_after = normalize_data_with_standard(var_TWS[0, :, i], TWS_hist)
        array_for_PCA = np.array([P_proj_after, TWS_proj_after])

        array_for_PCA = array_for_PCA.T
        hydro_climate = pca.transform(array_for_PCA[0,:,:])
        hydro_climate = hydro_climate[:, 0]
        data_after_PCA[i, :] = hydro_climate



    data_after_PCA = normalize_data_with_standard(data_after_PCA, ref_X_after_PCA)
    data_after_PCA = np.array(data_after_PCA)
    # np.savetxt("C:\Research2\Socioeconomic\Socio_data.csv", data_after_PCA, delimiter=',')
    print('test')






