import pandas as pd
import numpy as np

csvframe_gdp = pd.read_csv("C:\Research2\Data_for_calculation\\GDP_projection_SSP5.csv")
array_gdp = np.array(csvframe_gdp)
dict_GDP_2015 = {}
dict_GDP_2020 = {}
dict_GDP_2025 = {}
dict_GDP_2030 = {}
dict_GDP_2035 = {}
dict_GDP_2040 = {}
dict_GDP_2045 = {}
dict_GDP_2050 = {}
dict_GDP_2055 = {}
dict_GDP_2060 = {}
dict_GDP_2065 = {}
dict_GDP_2070 = {}
dict_GDP_2075 = {}
dict_GDP_2080 = {}
dict_GDP_2085 = {}
dict_GDP_2090 = {}
dict_GDP_2095 = {}
dict_GDP_2100 = {}
key = array_gdp[:, 0]
value_2015 = array_gdp[:, 1]
value_2020 = array_gdp[:, 2]
value_2025 = array_gdp[:, 3]
value_2030 = array_gdp[:, 4]
value_2035 = array_gdp[:, 5]
value_2040 = array_gdp[:, 6]
value_2045 = array_gdp[:, 7]
value_2050 = array_gdp[:, 8]
value_2055 = array_gdp[:, 9]
value_2060 = array_gdp[:, 10]
value_2065 = array_gdp[:, 11]
value_2070 = array_gdp[:, 12]
value_2075 = array_gdp[:, 13]
value_2080 = array_gdp[:, 14]
value_2085 = array_gdp[:, 15]
value_2090 = array_gdp[:, 16]
value_2095 = array_gdp[:, 17]
value_2100 = array_gdp[:, 18]
for i in range(len(key)):
    dict_GDP_2015[key[i]] = value_2015[i]
    dict_GDP_2020[key[i]] = value_2020[i]
    dict_GDP_2025[key[i]] = value_2025[i]
    dict_GDP_2030[key[i]] = value_2030[i]
    dict_GDP_2035[key[i]] = value_2035[i]
    dict_GDP_2040[key[i]] = value_2040[i]
    dict_GDP_2045[key[i]] = value_2045[i]
    dict_GDP_2050[key[i]] = value_2050[i]
    dict_GDP_2055[key[i]] = value_2055[i]
    dict_GDP_2060[key[i]] = value_2060[i]
    dict_GDP_2065[key[i]] = value_2065[i]
    dict_GDP_2070[key[i]] = value_2070[i]
    dict_GDP_2075[key[i]] = value_2075[i]
    dict_GDP_2080[key[i]] = value_2080[i]
    dict_GDP_2085[key[i]] = value_2085[i]
    dict_GDP_2090[key[i]] = value_2090[i]
    dict_GDP_2095[key[i]] = value_2095[i]
    dict_GDP_2100[key[i]] = value_2100[i]

csvframe_pop = pd.read_csv("C:\Research2\Data_for_calculation\\population_projection_SSP5.csv")
array_pop = np.array(csvframe_pop)
dict_POP_2015 = {}
dict_POP_2020 = {}
dict_POP_2025 = {}
dict_POP_2030 = {}
dict_POP_2035 = {}
dict_POP_2040 = {}
dict_POP_2045 = {}
dict_POP_2050 = {}
dict_POP_2055 = {}
dict_POP_2060 = {}
dict_POP_2065 = {}
dict_POP_2070 = {}
dict_POP_2075 = {}
dict_POP_2080 = {}
dict_POP_2085 = {}
dict_POP_2090 = {}
dict_POP_2095 = {}
dict_POP_2100 = {}
key = array_pop[:, 0]
value_2015 = array_pop[:, 1]
value_2020 = array_pop[:, 2]
value_2025 = array_pop[:, 3]
value_2030 = array_pop[:, 4]
value_2035 = array_pop[:, 5]
value_2040 = array_pop[:, 6]
value_2045 = array_pop[:, 7]
value_2050 = array_pop[:, 8]
value_2055 = array_pop[:, 9]
value_2060 = array_pop[:, 10]
value_2065 = array_pop[:, 11]
value_2070 = array_pop[:, 12]
value_2075 = array_pop[:, 13]
value_2080 = array_pop[:, 14]
value_2085 = array_pop[:, 15]
value_2090 = array_pop[:, 16]
value_2095 = array_pop[:, 17]
value_2100 = array_pop[:, 18]
for i in range(len(key)):
    dict_POP_2015[key[i]] = value_2015[i]
    dict_POP_2020[key[i]] = value_2020[i]
    dict_POP_2025[key[i]] = value_2025[i]
    dict_POP_2030[key[i]] = value_2030[i]
    dict_POP_2035[key[i]] = value_2035[i]
    dict_POP_2040[key[i]] = value_2040[i]
    dict_POP_2045[key[i]] = value_2045[i]
    dict_POP_2050[key[i]] = value_2050[i]
    dict_POP_2055[key[i]] = value_2055[i]
    dict_POP_2060[key[i]] = value_2060[i]
    dict_POP_2065[key[i]] = value_2065[i]
    dict_POP_2070[key[i]] = value_2070[i]
    dict_POP_2075[key[i]] = value_2075[i]
    dict_POP_2080[key[i]] = value_2080[i]
    dict_POP_2085[key[i]] = value_2085[i]
    dict_POP_2090[key[i]] = value_2090[i]
    dict_POP_2095[key[i]] = value_2095[i]
    dict_POP_2100[key[i]] = value_2100[i]

len = len(array_gdp[:, 1])
result = list([len, 3])

#get the codes of countries
country_code = list(dict_GDP_2015)
file_obj = open("C:\Research2\Data_for_calculation\Data_GDP_population_projection_SSP5.txt",'w')

for i in range(len):
    try:
        country_Code = country_code[i]
        GDP_2015 = dict_GDP_2015[country_code[i]]
        GDP_2020 = dict_GDP_2020[country_code[i]]
        GDP_2025 = dict_GDP_2025[country_code[i]]
        GDP_2030 = dict_GDP_2030[country_code[i]]
        GDP_2035 = dict_GDP_2035[country_code[i]]
        GDP_2040 = dict_GDP_2040[country_code[i]]
        GDP_2045 = dict_GDP_2045[country_code[i]]
        GDP_2050 = dict_GDP_2050[country_code[i]]
        GDP_2055 = dict_GDP_2055[country_code[i]]
        GDP_2060 = dict_GDP_2060[country_code[i]]
        GDP_2065 = dict_GDP_2065[country_code[i]]
        GDP_2070 = dict_GDP_2070[country_code[i]]
        GDP_2075 = dict_GDP_2075[country_code[i]]
        GDP_2080 = dict_GDP_2080[country_code[i]]
        GDP_2085 = dict_GDP_2085[country_code[i]]
        GDP_2090 = dict_GDP_2090[country_code[i]]
        GDP_2095 = dict_GDP_2095[country_code[i]]
        GDP_2100 = dict_GDP_2100[country_code[i]]

        POP_2015 = dict_POP_2015[country_code[i]]
        POP_2020 = dict_POP_2020[country_code[i]]
        POP_2025 = dict_POP_2025[country_code[i]]
        POP_2030 = dict_POP_2030[country_code[i]]
        POP_2035 = dict_POP_2035[country_code[i]]
        POP_2040 = dict_POP_2040[country_code[i]]
        POP_2045 = dict_POP_2045[country_code[i]]
        POP_2050 = dict_POP_2050[country_code[i]]
        POP_2055 = dict_POP_2055[country_code[i]]
        POP_2060 = dict_POP_2060[country_code[i]]
        POP_2065 = dict_POP_2065[country_code[i]]
        POP_2070 = dict_POP_2070[country_code[i]]
        POP_2075 = dict_POP_2075[country_code[i]]
        POP_2080 = dict_POP_2080[country_code[i]]
        POP_2085 = dict_POP_2085[country_code[i]]
        POP_2090 = dict_POP_2090[country_code[i]]
        POP_2095 = dict_POP_2095[country_code[i]]
        POP_2100 = dict_POP_2100[country_code[i]]

        GPP_2015 = str(GDP_2015 / POP_2015 * 1000)
        GPP_2020 = str(GDP_2020 / POP_2020 * 1000)
        GPP_2025 = str(GDP_2025 / POP_2025 * 1000)
        GPP_2030 = str(GDP_2030 / POP_2030 * 1000)
        GPP_2035 = str(GDP_2035 / POP_2035 * 1000)
        GPP_2040 = str(GDP_2040 / POP_2040 * 1000)
        GPP_2045 = str(GDP_2045 / POP_2045 * 1000)
        GPP_2050 = str(GDP_2050 / POP_2050 * 1000)
        GPP_2055 = str(GDP_2055 / POP_2055 * 1000)
        GPP_2060 = str(GDP_2060 / POP_2060 * 1000)
        GPP_2065 = str(GDP_2065 / POP_2065 * 1000)
        GPP_2070 = str(GDP_2070 / POP_2070 * 1000)
        GPP_2075 = str(GDP_2075 / POP_2075 * 1000)
        GPP_2080 = str(GDP_2080 / POP_2080 * 1000)
        GPP_2085 = str(GDP_2085 / POP_2085 * 1000)
        GPP_2090 = str(GDP_2090 / POP_2090 * 1000)
        GPP_2095 = str(GDP_2095 / POP_2095 * 1000)
        GPP_2100 = str(GDP_2100 / POP_2100 * 1000)
    except KeyError:
        print('no data for ' + country_Code)
    else:
        file_obj.write(country_Code + '/ ' + GPP_2015 + '/ ' + GPP_2020 + '/ ' + GPP_2025 + '/ ' + GPP_2030 + '/ ' + GPP_2035 + '/ ' + GPP_2040 + '/ ' + GPP_2045 + '/ ' + GPP_2050 + '/ ' + GPP_2055 + '/ ' + GPP_2060 + '/ ' + GPP_2065 + '/ ' + GPP_2070 + '/ ' + GPP_2075 + '/ ' + GPP_2080 + '/ ' + GPP_2085 + '/ ' + GPP_2090 + '/ ' + GPP_2095 + '/ ' + GPP_2100 + '\n')


file_obj.close()

print('test')