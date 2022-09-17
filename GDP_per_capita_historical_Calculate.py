import pandas as pd
import csv
import numpy as np

ISO_country = {}
with open('C:\Research2\ISO3166-1_codes_and_country_names.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    ISO_country = {rows[0]: rows[1] for rows in reader}

GDP_country_2000 = {}
with open('C:\Research2\Data_for_calculation\GDP_historical_2000.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    GDP_country_2000 = {rows[0]: rows[1] for rows in reader}

GDP_country_2005 = {}
with open('C:\Research2\Data_for_calculation\GDP_historical_2005.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    GDP_country_2005 = {rows[0]: rows[1] for rows in reader}

GDP_country_2010 = {}
with open('C:\Research2\Data_for_calculation\GDP_historical_2010.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    GDP_country_2010 = {rows[0]: rows[1] for rows in reader}

POP_country_2000 = {}
with open('C:\Research2\Data_for_calculation\Population_historical_2000.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    POP_country_2000 = {rows[0]: rows[1] for rows in reader}

POP_country_2005 = {}
with open('C:\Research2\Data_for_calculation\Population_historical_2005.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    POP_country_2005 = {rows[0]: rows[1] for rows in reader}

POP_country_2010 = {}
with open('C:\Research2\Data_for_calculation\Population_historical_2010.csv', encoding='ANSI') as inp:    # read csv as a dictionary
    reader = csv.reader(inp)
    POP_country_2010 = {rows[0]: rows[1] for rows in reader}

len = len(GDP_country_2000)
result = list([len, 3])

#get the codes of countries
country_code = list(GDP_country_2000)
file_obj = open("C:\Research2\Data_for_calculation\Data_GDP_population.txt",'w')

for i in range(len):
    try:
        country_Code = country_code[i]
        GDP_2000 = GDP_country_2000[country_code[i]]
        GDP_2005 = GDP_country_2005[country_code[i]]
        GDP_2010 = GDP_country_2010[country_code[i]]

        POP_2000 = POP_country_2000[country_code[i]]
        POP_2005 = POP_country_2005[country_code[i]]
        POP_2010 = POP_country_2010[country_code[i]]

    except KeyError:
        print('no data for ' + country_Code)
    else:
        file_obj.write(country_Code + '/ ' + GDP_2000 + '/ ' + POP_2000 + '/ ' + GDP_2005 + '/ ' + POP_2005 + '/ ' + GDP_2010 + '/ ' + POP_2010 + '\n')


file_obj.close()
