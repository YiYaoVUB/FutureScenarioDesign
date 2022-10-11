import pandas as pd
import numpy as np


scenarios = ['ssp126', 'ssp370', 'ssp585']

years = ['1996_2015',
         '2001_2020',
         '2006_2025',
         '2011_2030',
         '2016_2035',
         '2021_2040',
         '2026_2045',
         '2031_2050',
         '2036_2055',
         '2041_2060',
         '2046_2065',
         '2051_2070',
         '2056_2075',
         '2061_2080',
         '2066_2085',
         '2071_2090',
         '2076_2095',
         '2081_2100']           # Data of different periods are stored in different files

str_beg = 'C:\Research2\ISIMIP3b_data\out_P\\'
str_end = '_ensmean.tif.csv_noblank.csv'

pd_reader = pd.read_csv('C:\Research2\ISIMIP3b_data\\code.csv') # get the size of the data
cod = np.array(pd_reader)
num = len(cod)


result = np.zeros([num, 18])
for scenario in scenarios:
    for time in range(len(years)):
        str_data = str_beg + scenario + '_' + years[time] + str_end
        pd_reader = pd.read_csv(str_data)   # get the data
        rawdata = np.array(pd_reader)
        data = rawdata[:, 1:]   # no need for the first column
        for i in range(num):
            result[i, time] = data[i]
    file_obj_sur = open("C:\Research2\ISIMIP3b_data\P_result\\" + scenario + ".csv", 'w')
    for i in range(num):
        str_out = cod[i, 0] + ','
        for j in range(len(years)):
            str_out = str_out + str(result[i, j]) + ','
        file_obj_sur.write(str_out + '\n')
