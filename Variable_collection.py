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
gdp_SSP3_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GDP_SSP3.csv')
gdp_SSP5_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GDP_SSP5.csv')
num_country = len(gdp_SSP1_raw)

gov_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GOV_SSP1.csv')
gov_SSP3_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GOV_SSP3.csv')
gov_SSP5_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GOV_SSP5.csv')

urb_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_URB_SSP1.csv')
urb_SSP3_raw = read_csv_data('C:\Research2\Socioeconomic\Data_URB_SSP3.csv')
urb_SSP5_raw = read_csv_data('C:\Research2\Socioeconomic\Data_URB_SSP5.csv')

pop_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_POP_SSP1.csv')
pop_SSP3_raw = read_csv_data('C:\Research2\Socioeconomic\Data_POP_SSP3.csv')
pop_SSP5_raw = read_csv_data('C:\Research2\Socioeconomic\Data_POP_SSP5.csv')

pet_SSP1 = read_csv_data('C:\Research2\ISIMIP3b_data\PET_result\\ssp126.csv')
pet_SSP3 = read_csv_data('C:\Research2\ISIMIP3b_data\PET_result\\ssp370.csv')
pet_SSP5 = read_csv_data('C:\Research2\ISIMIP3b_data\PET_result\\ssp585.csv')

p_SSP1 = read_csv_data('C:\Research2\ISIMIP3b_data\P_result\\ssp126.csv')
p_SSP3 = read_csv_data('C:\Research2\ISIMIP3b_data\P_result\\ssp370.csv')
p_SSP5 = read_csv_data('C:\Research2\ISIMIP3b_data\P_result\\ssp585.csv')

tws_SSP1 = read_csv_data('C:\Research2\ISIMIP3b_data\\TWS_result\\ssp126.csv')
tws_SSP3 = read_csv_data('C:\Research2\ISIMIP3b_data\\TWS_result\\ssp370.csv')
tws_SSP5 = read_csv_data('C:\Research2\ISIMIP3b_data\\TWS_result\\ssp585.csv')

len_cou = len(DRI_country)
country_code = list(Socioeco_code)

file_obj_GDP1 = open("C:\Research2\Results\Data_technique_GDP_SSP1.csv",'w')
file_obj_GDP3 = open("C:\Research2\Results\Data_technique_GDP_SSP3.csv",'w')
file_obj_GDP5 = open("C:\Research2\Results\Data_technique_GDP_SSP5.csv",'w')

file_obj_URB1 = open("C:\Research2\Results\Data_technique_URB_SSP1.csv",'w')
file_obj_URB3 = open("C:\Research2\Results\Data_technique_URB_SSP3.csv",'w')
file_obj_URB5 = open("C:\Research2\Results\Data_technique_URB_SSP5.csv",'w')

file_obj_GOV1 = open("C:\Research2\Results\Data_technique_GOV_SSP1.csv",'w')
file_obj_GOV3 = open("C:\Research2\Results\Data_technique_GOV_SSP3.csv",'w')
file_obj_GOV5 = open("C:\Research2\Results\Data_technique_GOV_SSP5.csv",'w')

file_obj_POP1 = open("C:\Research2\Results\Data_technique_POP_SSP1.csv",'w')
file_obj_POP3 = open("C:\Research2\Results\Data_technique_POP_SSP3.csv",'w')
file_obj_POP5 = open("C:\Research2\Results\Data_technique_POP_SSP5.csv",'w')

file_obj_PET1 = open("C:\Research2\Results\Data_technique_PET_SSP1.csv",'w')
file_obj_PET3 = open("C:\Research2\Results\Data_technique_PET_SSP3.csv",'w')
file_obj_PET5 = open("C:\Research2\Results\Data_technique_PET_SSP5.csv",'w')

file_obj_P1 = open("C:\Research2\Results\Data_technique_P_SSP1.csv",'w')
file_obj_P3 = open("C:\Research2\Results\Data_technique_P_SSP3.csv",'w')
file_obj_P5 = open("C:\Research2\Results\Data_technique_P_SSP5.csv",'w')

file_obj_TWS1 = open("C:\Research2\Results\Data_technique_TWS_SSP1.csv",'w')
file_obj_TWS3 = open("C:\Research2\Results\Data_technique_TWS_SSP3.csv",'w')
file_obj_TWS5 = open("C:\Research2\Results\Data_technique_TWS_SSP5.csv",'w')

def calculate_socioeconomic_ave(rawdata, row_num):  # calculate the average value of last 4 steps
    data = np.zeros(18)
    for st in range(1, 19):
        sum = 0
        ed = st + 3
        for temp in range(st, ed + 1):
            sum = sum + float(rawdata[row_num, temp])
        ave = sum / 4
        data[st - 1] = ave
    return data

def output_str_gene(str_start, num, data):  #generate the str to be outputed
    str_output = str_start
    for x in range(num):
        str_output = str_output + ',' + str(data[x])
    return str_output
for cou in range(1, len_cou):
    try:
        country_name = ISO_country[country_code[cou]]
        i_socio = int(Socioeco_code[country_code[cou]]) -1
        i_isimi = int(Isimip_code[country_code[cou]]) -1
        SUR = SUR_country[country_name]
        SPR = SPR_country[country_name]
        DRI = DRI_country[country_name]

        gdp1 = calculate_socioeconomic_ave(gdp_SSP1_raw, i_socio)
        gdp3 = calculate_socioeconomic_ave(gdp_SSP3_raw, i_socio)
        gdp5 = calculate_socioeconomic_ave(gdp_SSP5_raw, i_socio)

        urb1 = calculate_socioeconomic_ave(urb_SSP1_raw, i_socio)
        urb3 = calculate_socioeconomic_ave(urb_SSP3_raw, i_socio)
        urb5 = calculate_socioeconomic_ave(urb_SSP5_raw, i_socio)

        gov1 = calculate_socioeconomic_ave(gov_SSP1_raw, i_socio)
        gov3 = calculate_socioeconomic_ave(gov_SSP3_raw, i_socio)
        gov5 = calculate_socioeconomic_ave(gov_SSP5_raw, i_socio)

        pop1 = calculate_socioeconomic_ave(pop_SSP1_raw, i_socio)
        pop3 = calculate_socioeconomic_ave(pop_SSP3_raw, i_socio)
        pop5 = calculate_socioeconomic_ave(pop_SSP5_raw, i_socio)

        num = len(gdp1)

        pet1 = pet_SSP1[i_isimi, :]
        p1 = p_SSP1[i_isimi, :]
        tws1 = tws_SSP1[i_isimi, :]

        pet3 = pet_SSP3[i_isimi, :]
        p3 = p_SSP3[i_isimi, :]
        tws3 = tws_SSP3[i_isimi, :]

        pet5 = pet_SSP5[i_isimi, :]
        p5 = p_SSP5[i_isimi, :]
        tws5 = tws_SSP5[i_isimi, :]
    except KeyError:
        print('no data for ' + country_name)
    else:
         str_start = country_name + ',' + country_code[cou] + ',' + SUR + ',' + SPR + ',' + DRI
         str_GDP1 = output_str_gene(str_start, num, gdp1)
         str_GDP3 = output_str_gene(str_start, num, gdp3)
         str_GDP5 = output_str_gene(str_start, num, gdp5)

         str_URB1 = output_str_gene(str_start, num, urb1)
         str_URB3 = output_str_gene(str_start, num, urb3)
         str_URB5 = output_str_gene(str_start, num, urb5)

         str_GOV1 = output_str_gene(str_start, num, gov1)
         str_GOV3 = output_str_gene(str_start, num, gov3)
         str_GOV5 = output_str_gene(str_start, num, gov5)

         str_POP1 = output_str_gene(str_start, num, pop1)
         str_POP3 = output_str_gene(str_start, num, pop3)
         str_POP5 = output_str_gene(str_start, num, pop5)

         str_PET1 = output_str_gene(str_start, num, pet1)
         str_PET3 = output_str_gene(str_start, num, pet3)
         str_PET5 = output_str_gene(str_start, num, pet5)

         str_P1 = output_str_gene(str_start, num, p1)
         str_P3 = output_str_gene(str_start, num, p3)
         str_P5 = output_str_gene(str_start, num, p5)

         str_TWS1 = output_str_gene(str_start, num, tws1)
         str_TWS3 = output_str_gene(str_start, num, tws3)
         str_TWS5 = output_str_gene(str_start, num, tws5)

         file_obj_GDP1.write(str_GDP1 + '\n')
         file_obj_GDP3.write(str_GDP3 + '\n')
         file_obj_GDP5.write(str_GDP5 + '\n')

         file_obj_URB1.write(str_URB1 + '\n')
         file_obj_URB3.write(str_URB3 + '\n')
         file_obj_URB5.write(str_URB5 + '\n')

         file_obj_GOV1.write(str_GOV1 + '\n')
         file_obj_GOV3.write(str_GOV3 + '\n')
         file_obj_GOV5.write(str_GOV5 + '\n')

         file_obj_POP1.write(str_POP1 + '\n')
         file_obj_POP3.write(str_POP3 + '\n')
         file_obj_POP5.write(str_POP5 + '\n')

         file_obj_PET1.write(str_PET1 + '\n')
         file_obj_PET3.write(str_PET3 + '\n')
         file_obj_PET5.write(str_PET5 + '\n')

         file_obj_P1.write(str_P1 + '\n')
         file_obj_P3.write(str_P3 + '\n')
         file_obj_P5.write(str_P5 + '\n')

         file_obj_TWS1.write(str_TWS1 + '\n')
         file_obj_TWS3.write(str_TWS3 + '\n')
         file_obj_TWS5.write(str_TWS5 + '\n')

print('test')










