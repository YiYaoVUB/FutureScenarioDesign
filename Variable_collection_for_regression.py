import pandas as pd
import csv
import numpy as np

def read_2col_csv_to_dict(filename, encode='ANSI'):
    with open(filename,
              encoding=encode) as inp:  # get the dictionary
        reader = csv.reader(inp)
        dict_result = {rows[0]: rows[1] for rows in reader}
        return dict_result

ISO_country = read_2col_csv_to_dict('C:\Research2\ISO3166-1_codes_and_country_names.csv')   #   Dict {ISO : country name}
DRI_country = read_2col_csv_to_dict('C:\Research2\Irrig_tech_distri\DRI_country.csv')   #   Dict {country name : drip irrigation}
SPR_country = read_2col_csv_to_dict('C:\Research2\Irrig_tech_distri\SPR_country.csv')   #   Dict {country name : sprinkler irrigation}
SUR_country = read_2col_csv_to_dict('C:\Research2\Irrig_tech_distri\SUR_country.csv')   #   Dict {country name : surface irrigation}
Socioeco_code = read_2col_csv_to_dict('C:\Research2\Socioeconomic\Socioeconomic_codes.csv')     #   Dict {ISO : row number for socioeconomic variables}
Isimip_code = read_2col_csv_to_dict('C:\Research2\ISIMIP3b_data\ISIMIP_code.csv')   #   Dict {ISO : row number for ISIMIP variables}


def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

gdp_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GDP_SSP1.csv')

num_country = len(gdp_SSP1_raw)

gov_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GOV_SSP1.csv')


urb_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_URB_SSP1.csv')


pop_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_POP_SSP1.csv')


len_cou = len(DRI_country)
country_code = list(Socioeco_code)

file_obj_Regression = open("C:\Research2\Regression\Data_Regression.csv",'w')

for cou in range(1, len_cou):
    try:
        country_name = ISO_country[country_code[cou]]
        i_socio = int(Socioeco_code[country_code[cou]]) -1
        i_isimi = int(Isimip_code[country_code[cou]]) -1
        SUR = SUR_country[country_name]
        SPR = SPR_country[country_name]
        DRI = DRI_country[country_name]

        gdp_2010 = gdp_SSP1_raw[i_socio, 2]
        gov_2010 = gov_SSP1_raw[i_socio, 2]
        urb_2010 = urb_SSP1_raw[i_socio, 2]


    except KeyError:
        print('no data for ' + country_name)

    else:
        str_start = country_name + ',' + country_code[cou] + ',' + SUR + ',' + SPR + ',' + DRI
        str_final = str_start + ',' + str(gdp_2010) + ',' + str(gov_2010) + ',' + str(urb_2010)

        file_obj_Regression.write(str_final + '\n')
