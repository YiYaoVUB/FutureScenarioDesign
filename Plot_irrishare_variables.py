from itertools import combinations
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

data_to_regression = read_csv_data('C:\Research2\Regression\Data_Regression_more_than_1000.csv')

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
TAS = data_to_regression[:, 13]
CFT_SUR = data_to_regression[:, 14]
CFT_SPR = data_to_regression[:, 15]
CFT_DRI = data_to_regression[:, 16]

IRR_FRA = data_to_regression[:, 17]
IRR_per_POP = data_to_regression[:, 18]
IRR_per_rural_POP = data_to_regression[:, 19]

CFT_MAX = data_to_regression[:, 20]
CFT_MORE = data_to_regression[:, 21]
CFT_NOR = data_to_regression[:, 22]
CFT_MIN = data_to_regression[:, 23]
CFT_MAXMORE = data_to_regression[:, 24]

def plot_all(X, str_var):
    f = plt.figure(figsize = (16, 4), dpi=100)
    ax = plt.subplot(1, 3, 1)
    plt.scatter(X,  SUR, color='red')
    plt.title('SUR', loc='left')
    plt.title(str_var, loc='right')

    ax = plt.subplot(1, 3, 2)
    plt.scatter(X,  SPR, color='blue')
    plt.title('SPR', loc='left')
    plt.title(str_var, loc='right')

    ax = plt.subplot(1, 3, 3)
    plt.scatter(X,  DRI, color='green')
    plt.title('DRI', loc='left')
    plt.title(str_var, loc='right')

    plt.show()

plot_all(GDP, 'GDP')
plot_all(GOV, 'GOV')
plot_all(URB, 'URB')
plot_all(GII, 'GII')

plot_all(APUSE, 'APUSE')
plot_all(APWW, 'APWW')
plot_all(PR, 'PR')
plot_all(PPET, 'PPET')

plot_all(TWS, 'TWS')
plot_all(TAS, 'TAS')
plot_all(CFT_SUR, 'CFT_SUR')
plot_all(CFT_SPR, 'CFT_SPR')
plot_all(CFT_DRI, 'CFT_DRI')

plot_all(IRR_FRA, 'IRR_FRA')
plot_all(IRR_per_POP, 'IRR_per_POP')
plot_all(IRR_per_rural_POP, 'IRR_per_rural_POP')

plot_all(CFT_MAX, 'CFT_MAX')
plot_all(CFT_MORE, 'CFT_MORE')
plot_all(CFT_NOR, 'CFT_NOR')
plot_all(CFT_MIN, 'CFT_MIN')
plot_all(CFT_MAXMORE, 'CFT_MAXMORE')