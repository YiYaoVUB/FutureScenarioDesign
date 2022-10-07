import pandas as pd
import numpy as np


str_pr_hist = 'C:\out_PPET\P\pr_ensmean_2010_2014_yearsum_timmean.tif.csv_noblank.csv'
str_potevap_hist = 'C:\out_PPET\PET\potevap_ensmean_2010_2014_yearsum_timmean.tif.csv_noblank.csv'

df_pr_hist = pd.read_csv(str_pr_hist)
df_potevap_hist = pd.read_csv(str_potevap_hist)

nparray_pr_hist = np.array(df_pr_hist)
nparray_potevap_hist = np.array(df_potevap_hist)

nparray_ppet_hist = nparray_pr_hist[:,1] / nparray_potevap_hist[:,1]
nparray_ppet_hist = nparray_ppet_hist / 365 * 12
str_begin_pr = 'C:\out_PPET\P\pr_ensmean_ssp126_'
str_begin_potevap = 'C:\out_PPET\PET\potevap_ensmean_ssp126_'
str_end = '_yearsum_timmean.tif.csv_noblank.csv'

data = np.zeros([len(nparray_ppet_hist), 18])
data[:, 0] = nparray_ppet_hist

x = 1
str_year_list = ['2015_2019', '2020_2024', '2025_2029', '2030_2034', '2035_2039', '2040_2044', '2045_2049', '2050_2054', '2055_2059', '2060_2064', '2065_2069', '2070_2074', '2075_2079', '2080_2084', '2085_2089', '2090_2094', '2095_2099']
for str_year in str_year_list:
    str_pr_future = str_begin_pr + str_year + str_end
    str_potevap_future = str_begin_potevap + str_year + str_end

    df_pr_future = pd.read_csv(str_pr_future)
    df_potevap_future = pd.read_csv(str_potevap_future)

    nparray_pr_future = np.array(df_pr_future)
    nparray_potevap_future = np.array(df_potevap_future)

    nparray_ppet_future = nparray_pr_future[:, 1] / nparray_potevap_hist[:, 1]
    nparray_ppet_future = nparray_ppet_future / 365 * 12

    data[:, x] = nparray_ppet_future
    x = x + 1

print('test')
np.savetxt("C:\out_PPET\ssp126.csv", data, delimiter=',')
