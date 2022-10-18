import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import matplotlib as mpl

def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 2:]

def set_plot_param():
    """Set my own customized plotting parameters"""

    mpl.rc('axes', edgecolor='dimgrey')
    mpl.rc('axes', labelcolor='dimgrey')
    mpl.rc('xtick', color='dimgrey')
    mpl.rc('ytick', color='dimgrey')
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

GDP_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_GDP_SSP1.csv')
GDP_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_GDP_SSP3.csv')
GDP_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_GDP_SSP5.csv')

GOV_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_GOV_SSP1.csv')
GOV_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_GOV_SSP3.csv')
GOV_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_GOV_SSP5.csv')

POP_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_POP_SSP1.csv')
POP_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_POP_SSP3.csv')
POP_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_POP_SSP5.csv')

PET_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_PET_SSP1.csv')
PET_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_PET_SSP3.csv')
PET_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_PET_SSP5.csv')

P_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_P_SSP1.csv')
P_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_P_SSP3.csv')
P_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_P_SSP5.csv')

URB_SSP1 = read_csv_data('C:\Research2\Results\Data_technique_URB_SSP1.csv')
URB_SSP3 = read_csv_data('C:\Research2\Results\Data_technique_URB_SSP3.csv')
URB_SSP5 = read_csv_data('C:\Research2\Results\Data_technique_URB_SSP5.csv')

SUR_hist = GDP_SSP1[:, 0]
SPR_hist = GDP_SSP1[:, 1]
DRI_hist = GDP_SSP1[:, 2]
GDP_hist = (GDP_SSP1[:, 3] + GDP_SSP3[:, 3] + GDP_SSP5[:, 3]) / 3
GOV_hist = (GOV_SSP1[:, 3] + GOV_SSP3[:, 3] + GOV_SSP5[:, 3]) / 3
POP_hist = (POP_SSP1[:, 3] + POP_SSP3[:, 3] + POP_SSP5[:, 3]) / 3
PET_hist = (PET_SSP1[:, 3] + PET_SSP3[:, 3] + PET_SSP5[:, 3]) / 3
P_hist   = (P_SSP1[:, 3]   + P_SSP3[:, 3]   + P_SSP5[:, 3]) / 3
URB_hist = (URB_SSP1[:, 3] + URB_SSP3[:, 3] + URB_SSP5[:, 3]) / 3

list_final = np.zeros((8, 144))
list_final[0, :] = SUR_hist
list_final[1, :] = SPR_hist
list_final[2, :] = DRI_hist
list_final[3, :] = GDP_hist
list_final[4, :] = GOV_hist
list_final[5, :] = POP_hist
list_final[6, :] = P_hist/ PET_hist
list_final[7, :] = URB_hist

pcc_coef_GDP_GOV = spearmanr(GOV_hist, GDP_hist)
pcc_coef_GDP_URB = spearmanr(URB_hist, GDP_hist)
pcc_coef_GOV_URB = spearmanr(URB_hist, GOV_hist)


pcc_coef_GDP_SUR = spearmanr(SUR_hist, GDP_hist)
pcc_coef_GOV_SUR = spearmanr(SUR_hist, GOV_hist)
pcc_coef_URB_SUR = spearmanr(SUR_hist, URB_hist)
pcc_coef_PPET_SUR = spearmanr(SUR_hist, P_hist/ PET_hist)

pcc_coef_GDP_SPR = spearmanr(SPR_hist, GDP_hist)
pcc_coef_GOV_SPR = spearmanr(SPR_hist, GOV_hist)
pcc_coef_URB_SPR = spearmanr(SPR_hist, URB_hist)
pcc_coef_PPET_SPR = spearmanr(SPR_hist, P_hist/ PET_hist)

pcc_coef_GDP_DRI = spearmanr(DRI_hist, GDP_hist)
pcc_coef_GOV_DRI = spearmanr(DRI_hist, GOV_hist)
pcc_coef_URB_DRI = spearmanr(DRI_hist, URB_hist)
pcc_coef_PPET_DRI = spearmanr(DRI_hist, P_hist/ PET_hist)


pcc_coef_GDP_GOV = pearsonr(GOV_hist, GDP_hist)
pcc_coef_GDP_URB = pearsonr(URB_hist, GDP_hist)
pcc_coef_GOV_URB = pearsonr(URB_hist, GOV_hist)

pcc_coef_GDP_SUR = pearsonr(SUR_hist, GDP_hist)
pcc_coef_GOV_SUR = pearsonr(SUR_hist, GOV_hist)
pcc_coef_URB_SUR = pearsonr(SUR_hist, URB_hist)
pcc_coef_PPET_SUR = pearsonr(SUR_hist, P_hist/ PET_hist)

pcc_coef_GDP_SPR = pearsonr(SPR_hist, GDP_hist)
pcc_coef_GOV_SPR = pearsonr(SPR_hist, GOV_hist)
pcc_coef_URB_SPR = pearsonr(SPR_hist, URB_hist)
pcc_coef_PPET_SPR = pearsonr(SPR_hist, P_hist/ PET_hist)

pcc_coef_GDP_DRI = pearsonr(DRI_hist, GDP_hist)
pcc_coef_GOV_DRI = pearsonr(DRI_hist, GOV_hist)
pcc_coef_URB_DRI = pearsonr(DRI_hist, URB_hist)
pcc_coef_PPET_DRI = pearsonr(DRI_hist, P_hist/ PET_hist)


arg_sort = np.argsort(SUR_hist)
SUR_afterSort = SUR_hist[arg_sort]
SPR_afterSort = SPR_hist[arg_sort]
DRI_afterSort = DRI_hist[arg_sort]
GDP_afterSort = GDP_hist[arg_sort]
GOV_afterSort = GOV_hist[arg_sort]
POP_afterSort = POP_hist[arg_sort]
PPET_afterSort = P_hist[arg_sort]/PET_hist[arg_sort]
URB_afterSort = URB_hist[arg_sort]

def median_calcu(np_array):
    median_1 = np.median(np_array[:11])
    median_2 = np.median(np_array[11:22])
    median_3 = np.median(np_array[22:33])
    median_4 = np.median(np_array[33:44])
    median_5 = np.median(np_array[44:54])
    median_6 = np.median(np_array[54:64])
    median_7 = np.median(np_array[64:74])
    median_8 = np.median(np_array[74:84])
    median_9 = np.median(np_array[84:94])
    median_10 = np.median(np_array[94:104])
    median_11 = np.median(np_array[104:114])
    median_12 = np.median(np_array[114:124])
    median_13 = np.median(np_array[124:134])
    median_14 = np.median(np_array[134:144])
    return np.array([median_1, median_2, median_3, median_4, median_5, median_6, median_7, median_8, median_9, median_10, median_11, median_12, median_13, median_14])

SUR_median = median_calcu(SUR_afterSort)
SPR_median = median_calcu(SPR_afterSort)
DRI_median = median_calcu(DRI_afterSort)
GDP_median = median_calcu(GDP_afterSort)
GOV_median = median_calcu(GOV_afterSort)
POP_median = median_calcu(POP_afterSort)
PPET_median = median_calcu(PPET_afterSort)
URB_median = median_calcu(URB_afterSort)

f = plt.figure(figsize = (15, 4), dpi=100)
set_plot_param()
plt.subplots_adjust(top = 0.9, bottom = 0.15, left = 0.07, right = 0.95, wspace = 0.3)
ax1 = plt.subplot(1,3,1)
plt.scatter(GDP_hist, SUR_hist, color='red', marker='o',s=10)

plt.xlabel('GDP per capita (10000$)', fontsize=12)
plt.xticks([0, 10000, 20000, 30000, 40000, 50000], ['0', '1', '2', '3', '4', '5'], fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Surface', fontsize=15)
ax1 = plt.subplot(1,3,2)

plt.scatter(GDP_hist, SPR_hist, color='blue', marker='o',s=10)

plt.xlabel('GDP per capita (10000$)', fontsize=12)
plt.xticks([0, 10000, 20000, 30000, 40000, 50000], ['0', '1', '2', '3', '4', '5'], fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Sprinkler', fontsize=15)

ax1 = plt.subplot(1,3,3)

plt.scatter(GDP_hist, DRI_hist, color='green', marker='o',s=10)
plt.xlabel('GDP per capita (10000$)', fontsize=12)
plt.xticks([0, 10000, 20000, 30000, 40000, 50000], ['0', '1', '2', '3', '4', '5'], fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Drip', fontsize=15)

plt.show()



f = plt.figure(figsize = (15, 4), dpi=100)
set_plot_param()
plt.subplots_adjust(top = 0.9, bottom = 0.15, left = 0.07, right = 0.95, wspace = 0.3)
ax1 = plt.subplot(1,3,1)
plt.scatter(GOV_hist, SUR_hist, color='red', marker='o',s=10)

plt.xlabel('Governance', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Surface', fontsize=15)
ax1 = plt.subplot(1,3,2)

plt.scatter(GOV_hist, SPR_hist, color='blue', marker='o',s=10)

plt.xlabel('Governance', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Sprinkler', fontsize=15)

ax1 = plt.subplot(1,3,3)

plt.scatter(GOV_hist, DRI_hist, color='green', marker='o',s=10)
plt.xlabel('Governance', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Drip', fontsize=15)

plt.show()


f = plt.figure(figsize = (15, 4), dpi=100)
set_plot_param()
plt.subplots_adjust(top = 0.9, bottom = 0.15, left = 0.07, right = 0.95, wspace = 0.3)
ax1 = plt.subplot(1,3,1)
plt.scatter(URB_hist, SUR_hist, color='red', marker='o',s=10)

plt.xlabel('Urbanalisation', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Surface', fontsize=15)
ax1 = plt.subplot(1,3,2)

plt.scatter(URB_hist, SPR_hist, color='blue', marker='o',s=10)

plt.xlabel('Urbanalisation', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Sprinkler', fontsize=15)

ax1 = plt.subplot(1,3,3)

plt.scatter(URB_hist, DRI_hist, color='green', marker='o',s=10)
plt.xlabel('Urbanalisation', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Drip', fontsize=15)

plt.show()




f = plt.figure(figsize = (15, 4), dpi=100)
set_plot_param()
plt.subplots_adjust(top = 0.9, bottom = 0.15, left = 0.07, right = 0.95, wspace = 0.3)
ax1 = plt.subplot(1,3,1)
plt.scatter(P_hist/PET_hist, SUR_hist, color='red', marker='o',s=10)

plt.xlabel('PPET', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Surface', fontsize=15)
ax1 = plt.subplot(1,3,2)

plt.scatter(P_hist/PET_hist, SPR_hist, color='blue', marker='o',s=10)

plt.xlabel('PPET', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Sprinkler', fontsize=15)

ax1 = plt.subplot(1,3,3)

plt.scatter(P_hist/PET_hist, DRI_hist, color='green', marker='o',s=10)
plt.xlabel('PPET', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.title('Drip', fontsize=15)

plt.show()


f = plt.figure(figsize = (10, 10), dpi=100)
set_plot_param()
plt.subplots_adjust(top = 0.9, bottom = 0.15, left = 0.07, right = 0.95, wspace = 0.3, hspace = 0.3)
ax1 = plt.subplot(2,2,1)
plt.scatter(GDP_median, SUR_median, color='red', marker='o',s=10)

plt.xlabel('GDP per capita ($)', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)

ax1 = plt.subplot(2,2,2)

plt.scatter(GOV_median, SUR_median, color='blue', marker='o',s=10)

plt.xlabel('Governance', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)

ax1 = plt.subplot(2,2,3)


plt.scatter(URB_median, SUR_median, color='green', marker='o',s=10)
plt.xlabel('Urbanalisation', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)

ax1 = plt.subplot(2,2,4)


plt.scatter(PPET_median, SUR_median, color='green', marker='o',s=10)
plt.xlabel('P/PET ratio', fontsize=12)
plt.xticks(fontsize=12)
plt.ylabel('Fraction', fontsize=12)
plt.yticks(fontsize=12)
plt.show()

print('test')