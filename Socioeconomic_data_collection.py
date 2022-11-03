import pandas as pd
import csv
import numpy as np

scenarios = ['SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5']

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

country_code = list(ISO_country)    # get the list of the Three-Letter-Code
len_country = len(country_code)

GDP_code_hist = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\GDP_hist_codes.csv')     # The number of the countries in different data is different, so we read this file to get the dict {"Three-Letter-Code": "Line"}. The code is used for linking different data
GDP_code_proj = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\GDP_proj_codes.csv')     # The number of the countries in different data is different, so we read this file to get the dict {"Three-Letter-Code": "Line"}. The code is used for linking different data

GOV_code_hist = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\gov_hist_codes.csv')
GOV_code_proj = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\gov_proj_codes.csv')

URB_code_hist = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\urb_hist_codes.csv')
URB_code_proj = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\urb_proj_codes.csv')

POP_code_hist = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\pop_hist_code.csv')
POP_code_proj = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\pop_proj_code.csv')

GII_code_hist = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\gii_historical_code.csv')
GII_code_proj = read_2col_csv_to_dict('C:\Research2\Data_for_calculation\Final_calculation\\gii_projection_code.csv')


def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

gdp_2000_2010 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\GDP_per_capita_historical.csv')
gov_2000_2010 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\goverance_historical.csv')
urb_2000_2010 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\urbanization_historical.csv')
pop_2000_2010 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\Population_historical.csv')
gii_2000_2010 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\gender_inequa_historical.csv')

for scenario in scenarios:

    gdp_2015_2100 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\Data_GDP_population_projection_' + scenario + '.csv')
    gov_2015_2100 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\goverance_projection_' + scenario + '.csv')
    urb_2015_2100 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\urbanization_projection_' + scenario + '.csv')
    pop_2015_2100 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\population_projection_' + scenario + '.csv')
    gii_2015_2100 = read_csv_data('C:\Research2\Data_for_calculation\Final_calculation\\gii_' + scenario + '.csv')


    file_obj_GDP = open("C:\Research2\Socioeconomic\Data_GDP_" + scenario + ".csv", 'w')
    file_obj_GOV = open("C:\Research2\Socioeconomic\Data_GOV_" + scenario + ".csv", 'w')
    file_obj_URB = open("C:\Research2\Socioeconomic\Data_URB_" + scenario + ".csv", 'w')
    file_obj_POP = open("C:\Research2\Socioeconomic\Data_POP_" + scenario + ".csv", 'w')
    file_obj_GII = open("C:\Research2\Socioeconomic\Data_GII_" + scenario + ".csv", 'w')

    for cou in range(len_country):
        try:
            country_name = ISO_country[country_code[cou]]

            gdp_hist_code = int(GDP_code_hist[country_code[cou]])
            gov_hist_code = int(GOV_code_hist[country_code[cou]])
            urb_hist_code = int(URB_code_hist[country_code[cou]])
            pop_hist_code = int(POP_code_hist[country_code[cou]])
            gii_hist_code = int(GII_code_hist[country_code[cou]])

            gdp_proj_code = int(GDP_code_proj[country_code[cou]])
            gov_proj_code = int(GOV_code_proj[country_code[cou]])
            urb_proj_code = int(URB_code_proj[country_code[cou]])
            pop_proj_code = int(POP_code_proj[country_code[cou]])
            gii_proj_code = int(GII_code_proj[country_code[cou]])

            print('test')

        except KeyError:
            print('no data for ' + country_name)
        else:
            str_out_gdp = country_name + ',' + country_code[cou]
            for i in range(3):
                str_out_gdp = str_out_gdp +  ',' + str(gdp_2000_2010[gdp_hist_code, i])
            for i in range(18):
                str_out_gdp = str_out_gdp + ',' + str(gdp_2015_2100[gdp_proj_code, i])

            str_out_gov = country_name + ',' + country_code[cou]
            for i in range(3):
                str_out_gov = str_out_gov + ',' + str(gov_2000_2010[gov_hist_code, i])
            for i in range(18):
                str_out_gov = str_out_gov + ',' + str(gov_2015_2100[gov_proj_code, i])

            str_out_urb = country_name + ',' + country_code[cou]
            for i in range(3):
                str_out_urb = str_out_urb + ',' + str(urb_2000_2010[urb_hist_code, i])
            for i in range(18):
                str_out_urb = str_out_urb + ',' + str(urb_2015_2100[urb_proj_code, i])

            str_out_pop = country_name + ',' + country_code[cou]
            for i in range(3):
                str_out_pop = str_out_pop + ',' + str(pop_2000_2010[pop_hist_code, i])
            for i in range(18):
                str_out_pop = str_out_pop + ',' + str(pop_2015_2100[pop_proj_code, i])

            str_out_gii = country_name + ',' + country_code[cou]
            for i in range(3):
                str_out_gii = str_out_gii + ',' + str(gii_2000_2010[gii_hist_code, i])
            for i in range(18):
                str_out_gii = str_out_gii + ',' + str(gii_2015_2100[gii_proj_code, i])

            file_obj_GDP.write(str_out_gdp + '\n')
            file_obj_GOV.write(str_out_gov + '\n')
            file_obj_URB.write(str_out_urb + '\n')
            file_obj_POP.write(str_out_pop + '\n')
            file_obj_GII.write(str_out_gii + '\n')

    file_obj_GDP.close()
    file_obj_GOV.close()
    file_obj_URB.close()
    file_obj_POP.close()
    file_obj_GII.close()
