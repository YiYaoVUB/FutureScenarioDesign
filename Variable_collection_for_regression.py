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
Cropfrac_code = read_2col_csv_to_dict('C:\Research2\cft_calcu\irr_area_code.csv')
Cftwater_code = read_2col_csv_to_dict('C:\Research2\cft_calcu\cft_water_code.csv')

def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

def read_csv_data_2(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, :]

gdp_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GDP_SSP1.csv')
num_country = len(gdp_SSP1_raw)
gov_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GOV_SSP1.csv')
urb_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_URB_SSP1.csv')
pop_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_POP_SSP1.csv')
gii_SSP1_raw = read_csv_data('C:\Research2\Socioeconomic\Data_GII_SSP1.csv')

atotuse_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\atotuse_1991_2010.csv')
atotww_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\atotww_1991_2010.csv')
potevap_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\potevap_1991_2010.csv')
pr_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\\pr_1991_2010.csv')
ptotuse_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\ptotuse_1991_2010.csv')
ptotww_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\ptotww_1991_2010.csv')
tws_raw = read_csv_data_2('C:\Research2\ISIMIP3a\out_file_1991_2010\\tws_1991_2010.csv')
tas_raw = read_csv_data_2('C:\Research2\ISIMIP3a\\tas_1996_2015.csv')

cropfrac_raw = read_csv_data_2('C:\Research2\cft_calcu\\Irr_crop_frac.csv')
cftwater_raw = read_csv_data_2('C:\Research2\cft_calcu\\cft_water_frac.csv')

country_code = list(Socioeco_code)
len_cou = len(country_code)

file_obj_Regression = open("C:\Research2\Regression\Data_Regression.csv",'w')

for cou in range(len_cou):
    try:
        country_name = ISO_country[country_code[cou]]
        i_socio = int(Socioeco_code[country_code[cou]])
        i_isimi = int(Isimip_code[country_code[cou]])
        i_cftfrac = int(Cropfrac_code[country_code[cou]])
        i_cftwater = int(Cftwater_code[country_code[cou]])
        SUR = SUR_country[country_name]
        SPR = SPR_country[country_name]
        DRI = DRI_country[country_name]


        gdp_2010 = gdp_SSP1_raw[i_socio, 3]
        #   gdp_2010 = (gdp_SSP1_raw[i_socio, 3]+gdp_SSP1_raw[i_socio, 2]+gdp_SSP1_raw[i_socio, 1])/3

        gov_2010 = gov_SSP1_raw[i_socio, 3]
        #   gov_2010 = (gov_SSP1_raw[i_socio, 3]+gov_SSP1_raw[i_socio, 2]+gov_SSP1_raw[i_socio, 1])/3

        urb_2010 = urb_SSP1_raw[i_socio, 3]
        #   urb_2010 = (urb_SSP1_raw[i_socio, 3]+urb_SSP1_raw[i_socio, 2]+urb_SSP1_raw[i_socio, 1])/3

        gii_2010 = gii_SSP1_raw[i_socio, 3]
        #   gii_2010 = (gii_SSP1_raw[i_socio, 3]+gii_SSP1_raw[i_socio, 2]+gii_SSP1_raw[i_socio, 1])/3

        pop_2010 = pop_SSP1_raw[i_socio, 3]
        #   pop_2010 = (pop_SSP1_raw[i_socio, 3]+pop_SSP1_raw[i_socio, 2]+pop_SSP1_raw[i_socio, 1])/3

        atotuse = atotuse_raw[i_isimi, 1]
        ptotuse = ptotuse_raw[i_isimi, 1]
        atotww = atotww_raw[i_isimi, 1]
        ptotww = ptotww_raw[i_isimi, 1]
        pr = pr_raw[i_isimi, 1]
        potevap = potevap_raw[i_isimi, 1]
        tws = tws_raw[i_isimi, 1]
        tas = tas_raw[i_isimi, 1]

        sur_cft = cropfrac_raw[i_cftfrac, 1]
        spr_cft = cropfrac_raw[i_cftfrac, 2]
        dri_cft = cropfrac_raw[i_cftfrac, 3]

        irr_fra = cropfrac_raw[i_cftfrac, 4]
        irr_area = cropfrac_raw[i_cftfrac, 5]

        cft_max = cftwater_raw[i_cftwater, 1]
        cft_more = cftwater_raw[i_cftwater, 2]
        cft_nor = cftwater_raw[i_cftwater, 3]
        cft_min = cftwater_raw[i_cftwater, 4]
        cft_high = cftwater_raw[i_cftwater, 5]

    except KeyError:
        print('no data for ' + country_name)

    else:
        if float(ptotuse) == 0:
            apuse = 0
        else:
            apuse = float(atotuse)/float(ptotuse)
        if float(ptotww) == 0:
            apww = 0
        else:
            apww = float(atotww)/float(ptotww)
        str_start = country_name + ',' + country_code[cou] + ',' + SUR + ',' + SPR + ',' + DRI
        str_final = str_start + ',' + str(gdp_2010) + ',' + str(gov_2010) + ',' + str(urb_2010) + ',' + str(gii_2010)
        str_final = str_final + ',' + str(apuse) + ',' + str(apww) + ',' + str(pr) + ',' + str(float(pr)/float(potevap)) + ',' + str(tws) + ',' + str(tas)
        str_final = str_final + ',' + str(sur_cft) + ',' + str(spr_cft) + ',' + str(dri_cft) + ',' + str(irr_fra) + ',' + str(float(irr_area)/ float(pop_2010)) + ',' + str(float(irr_area)/ float(pop_2010) / (100-float(urb_2010)))
        str_final = str_final + ',' + str(cft_max) + ',' + str(cft_more) + ',' + str(cft_nor) + ',' + str(cft_min) + ',' + str(float(cft_max)+float(cft_more)) + ',' + str(cft_high)
        str_final = str_final + ',' + str(irr_area) + ',' + str(pop_2010)
        file_obj_Regression.write(str_final + '\n')
