import pandas as pd
import csv
import numpy as np

scenarios = ['SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5']
ISO_country = {}
with open('C:\Research2\ISO3166-1_codes_and_country_names.csv', encoding='ANSI') as inp:     # read the csv file (Three-Letter-Code: Country-Name)
    reader = csv.reader(inp)
    ISO_country = {rows[0]: rows[1] for rows in reader}     # read the csv file as a dict: {"Three-Letter-Code": "Country-Name"}

country_code = list(ISO_country)    # get the list of the Three-Letter-Code
len_country = len(country_code)



DRI_country = {}
with open('C:\Research2\DRI_country.csv', encoding='ANSI') as inp:    # read the csv file (Country-Name: Drip-Fraction)
    reader = csv.reader(inp)
    DRI_country = {rows[0]: rows[1] for rows in reader}     # read the csv file as a dict: {"Country-Name": "Drip-Fraction"}

SPR_country = {}
with open('C:\Research2\SPR_country.csv', encoding='ANSI') as inp:    # read the csv file (Country-Name: Sprinkler-Fraction)
    reader = csv.reader(inp)
    SPR_country = {rows[0]: rows[1] for rows in reader}     # read the csv file as a dict: {"Country-Name": "Sprinkler-Fraction"}

SUR_country = {}
with open('C:\Research2\SUR_country.csv', encoding='ANSI') as inp:    # read the csv file (Country-Name: Flood-Fraction)
    reader = csv.reader(inp)
    SUR_country = {rows[0]: rows[1] for rows in reader}     # read the csv file as a dict: {"Country-Name": "Flood-Fraction"}




GDP_code_hist = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\GDP_hist_codes.csv', encoding='ANSI') as inp:    # The number of the countries in different data is different, so we read this file to get the dict {"Three-Letter-Code": "Line"}. The code is used for linking different data
    reader = csv.reader(inp)
    GDP_code_hist = {rows[0]: rows[1] for rows in reader}

GDP_code_proj = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\GDP_proj_codes.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    GDP_code_proj = {rows[0]: rows[1] for rows in reader}

GOV_code_hist = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\gov_hist_codes.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    GOV_code_hist = {rows[0]: rows[1] for rows in reader}

GOV_code_proj = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\gov_proj_codes.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    GOV_code_proj = {rows[0]: rows[1] for rows in reader}

URB_code_hist = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\\urb_hist_codes.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    URB_code_hist = {rows[0]: rows[1] for rows in reader}

URB_code_proj = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\\urb_proj_codes.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    URB_code_proj = {rows[0]: rows[1] for rows in reader}

POP_code_hist = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\\pop_hist_code.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    POP_code_hist = {rows[0]: rows[1] for rows in reader}

POP_code_proj = {}
with open('C:\Research2\Data_for_calculation\Final_calculation\\pop_proj_code.csv', encoding='ANSI') as inp:    # The same
    reader = csv.reader(inp)
    POP_code_proj = {rows[0]: rows[1] for rows in reader}


pd_reader = pd.read_csv( 'C:\Research2\Data_for_calculation\Final_calculation\GDP_per_capita_historical.csv')   # Historical GDP_per_capita data
data = np.array(pd_reader)
gdp_2000_2010 = data[:, 1:]

pd_reader = pd.read_csv('C:\Research2\Data_for_calculation\Final_calculation\goverance_historical.csv')         # Historical goverance data
data = np.array(pd_reader)
gov_2000_2010 = data[:, 1:]

pd_reader = pd.read_csv('C:\Research2\Data_for_calculation\Final_calculation\\urbanization_historical.csv')     # Historical urbanization data
data = np.array(pd_reader)
urb_2000_2010 = data[:, 1:]

pd_reader = pd.read_csv('C:\Research2\Data_for_calculation\Final_calculation\\Population_historical.csv')     # Historical urbanization data
data = np.array(pd_reader)
pop_2000_2010 = data[:, 1:]


for scenario in scenarios:
    pd_reader = pd.read_csv(
        'C:\Research2\Data_for_calculation\Final_calculation\Data_GDP_population_projection_' + scenario + '.csv')     # Projected GDP_per_capita data
    data = np.array(pd_reader)
    gdp_2015_2100 = data[:, 1:]

    pd_reader = pd.read_csv(
        'C:\Research2\Data_for_calculation\Final_calculation\goverance_projection_' + scenario + '.csv')        # Projected goverance data
    data = np.array(pd_reader)
    gov_2015_2100 = data[:, 1:]

    pd_reader = pd.read_csv(
        'C:\Research2\Data_for_calculation\Final_calculation\\urbanization_projection_' + scenario + '.csv')    # Projected urbanization data
    data = np.array(pd_reader)
    urb_2015_2100 = data[:, 1:]

    pd_reader = pd.read_csv(
        'C:\Research2\Data_for_calculation\Final_calculation\\population_projection_' + scenario + '.csv')  # Projected urbanization data
    data = np.array(pd_reader)
    pop_2015_2100 = data[:, 1:]

    file_obj_GDP = open("C:\Research2\Socioeconomic\Data_GDP_" + scenario + ".csv", 'w')
    file_obj_GOV = open("C:\Research2\Socioeconomic\Data_GOV_" + scenario + ".csv", 'w')
    file_obj_URB = open("C:\Research2\Socioeconomic\Data_URB_" + scenario + ".csv", 'w')
    file_obj_POP = open("C:\Research2\Socioeconomic\Data_POP_" + scenario + ".csv", 'w')

    for cou in range(len_country):
        try:
            country_name = ISO_country[country_code[cou]]

            gdp_hist_code = int(GDP_code_hist[country_code[cou]]) - 1
            gov_hist_code = int(GOV_code_hist[country_code[cou]]) - 1
            urb_hist_code = int(URB_code_hist[country_code[cou]]) - 1
            pop_hist_code = int(POP_code_hist[country_code[cou]]) - 1

            gdp_proj_code = int(GDP_code_proj[country_code[cou]]) - 1
            gov_proj_code = int(GOV_code_proj[country_code[cou]]) - 1
            urb_proj_code = int(URB_code_proj[country_code[cou]]) - 1
            pop_proj_code = int(POP_code_proj[country_code[cou]]) - 1


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


            file_obj_GDP.write(str_out_gdp + '\n')
            file_obj_GOV.write(str_out_gov + '\n')
            file_obj_URB.write(str_out_urb + '\n')
            file_obj_POP.write(str_out_pop + '\n')

    file_obj_GDP.close()
    file_obj_GOV.close()
    file_obj_URB.close()
    file_obj_POP.close()
