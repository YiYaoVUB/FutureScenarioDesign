import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import matplotlib as mpl

def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

data_to_regression = read_csv_data('C:\Research2\Regression\Data_Regression.csv')

SUR = data_to_regression[:, 1]
SPR = data_to_regression[:, 2]
DRI = data_to_regression[:, 3]
GDP = data_to_regression[:, 4]
GOV = data_to_regression[:, 5]
URB = data_to_regression[:, 6]
GII = data_to_regression[:, 7]
APUSE = data_to_regression[:, 8]
APWW = data_to_regression[:, 9]
PR = data_to_regression[:, 10]
PPET = data_to_regression[:, 11]
TWS = data_to_regression[:, 12]

X = np.array((GDP, GOV, URB, GII, APUSE, APWW, PR, PPET, TWS))
str_X = ['GDP', 'GOV', 'URB', 'GII', 'APUSE', 'APWW', 'PR', 'PPET', 'TWS']

spearmanr_X = np.zeros([9, 9])
spearmanp_X = np.zeros([9, 9])
pearsonr_X = np.zeros([9, 9])
pearsonp_X = np.zeros([9, 9])
for i in range (9):
    for j in range(9):
        r, p = spearmanr(X[i, :], X[j, :])
        spearmanr_X[i, j] = r
        spearmanp_X[i, j] = p
        r, p = pearsonr(X[i, :], X[j, :])
        pearsonr_X[i, j] = r
        pearsonp_X[i, j] = p
spearmanr_X_y = np.zeros([9, 3])
spearmanp_X_y = np.zeros([9, 3])

pearsonr_X_y = np.zeros([9, 3])
pearsonp_X_y = np.zeros([9, 3])

for i in range(9):
    r, p = spearmanr(X[i, :], SUR)
    spearmanr_X_y[i, 0] = r
    spearmanp_X_y[i, 0] = p
    r, p = spearmanr(X[i, :], SPR)
    spearmanr_X_y[i, 1] = r
    spearmanp_X_y[i, 1] = p
    r, p = spearmanr(X[i, :], DRI)
    spearmanr_X_y[i, 2] = r
    spearmanp_X_y[i, 2] = p

    r, p = pearsonr(X[i, :], SUR)
    pearsonr_X_y[i, 0] = r
    pearsonp_X_y[i, 0] = p
    r, p = pearsonr(X[i, :], SPR)
    pearsonr_X_y[i, 1] = r
    pearsonp_X_y[i, 1] = p
    r, p = pearsonr(X[i, :], DRI)
    pearsonr_X_y[i, 2] = r
    pearsonp_X_y[i, 2] = p

file_obj_pearson_Xx = open('C:\Research2\Regression\pearson_Xx.csv', 'w')
file_obj_pearson_Xx.write('pearson R')
for i in range(9):
    file_obj_pearson_Xx.write(',' + str_X[i])
file_obj_pearson_Xx.write('\n')
for i in range(9):
    file_obj_pearson_Xx.write(str_X[i] + ',')
    for j in range(9):
        if pearsonp_X[i, j] < 0.01:
            file_obj_pearson_Xx.write(str(round(pearsonr_X[i, j], 4)) + '***,')
        elif pearsonp_X[i, j] < 0.05:
            file_obj_pearson_Xx.write(str(round(pearsonr_X[i, j], 4)) + '**,')
        elif pearsonp_X[i, j] < 0.1:
            file_obj_pearson_Xx.write(str(round(pearsonr_X[i, j], 4)) + '*,')
        else:
            file_obj_pearson_Xx.write(str(round(pearsonr_X[i, j], 4)) + ',')
    file_obj_pearson_Xx.write('\n')
file_obj_pearson_Xx.close()

file_obj_spearman_Xx = open('C:\Research2\Regression\spearman_Xx.csv', 'w')
file_obj_spearman_Xx.write('spearman R')
for i in range(9):
    file_obj_spearman_Xx.write(',' + str_X[i])
file_obj_spearman_Xx.write('\n')
for i in range(9):
    file_obj_spearman_Xx.write(str_X[i] + ',')
    for j in range(9):
        if spearmanp_X[i, j] < 0.01:
            file_obj_spearman_Xx.write(str(round(spearmanr_X[i, j], 4)) + '***,')
        elif pearsonp_X[i, j] < 0.05:
            file_obj_spearman_Xx.write(str(round(spearmanr_X[i, j], 4)) + '**,')
        elif pearsonp_X[i, j] < 0.1:
            file_obj_spearman_Xx.write(str(round(spearmanr_X[i, j], 4)) + '*,')
        else:
            file_obj_spearman_Xx.write(str(round(spearmanr_X[i, j], 4)) + ',')
    file_obj_spearman_Xx.write('\n')
file_obj_spearman_Xx.close()


str_Y = ['SUR', 'SPR', 'DRI']

file_obj_pearson_X_y = open('C:\Research2\Regression\pearson_X_y.csv', 'w')
file_obj_pearson_X_y.write('pearson R')
for i in range(3):
    file_obj_pearson_X_y.write(',' + str_Y[i])
file_obj_pearson_X_y.write('\n')
for i in range(9):
    file_obj_pearson_X_y.write(str_X[i] + ',')
    for j in range(3):
        if pearsonp_X_y[i, j] < 0.01:
            file_obj_pearson_X_y.write(str(round(pearsonr_X_y[i, j], 4)) + '***,')
        elif pearsonp_X_y[i, j] < 0.05:
            file_obj_pearson_X_y.write(str(round(pearsonr_X_y[i, j], 4)) + '**,')
        elif pearsonp_X_y[i, j] < 0.1:
            file_obj_pearson_X_y.write(str(round(pearsonr_X_y[i, j], 4)) + '*,')
        else:
            file_obj_pearson_X_y.write(str(round(pearsonr_X_y[i, j], 4)) + ',')
    file_obj_pearson_X_y.write('\n')
file_obj_pearson_X_y.close()

file_obj_spearman_X_y = open('C:\Research2\Regression\spearman_X_y.csv', 'w')
file_obj_spearman_X_y.write('spearman R')
for i in range(3):
    file_obj_spearman_X_y.write(',' + str_Y[i])
file_obj_spearman_X_y.write('\n')
for i in range(9):
    file_obj_spearman_X_y.write(str_X[i] + ',')
    for j in range(3):
        if spearmanp_X_y[i, j] < 0.01:
            file_obj_spearman_X_y.write(str(round(spearmanr_X_y[i, j], 4)) + '***,')
        elif pearsonp_X_y[i, j] < 0.05:
            file_obj_spearman_X_y.write(str(round(spearmanr_X_y[i, j], 4)) + '**,')
        elif pearsonp_X_y[i, j] < 0.1:
            file_obj_spearman_X_y.write(str(round(spearmanr_X_y[i, j], 4)) + '*,')
        else:
            file_obj_spearman_X_y.write(str(round(spearmanr_X_y[i, j], 4)) + ',')
    file_obj_spearman_X_y.write('\n')
file_obj_spearman_X_y.close()
print('test')