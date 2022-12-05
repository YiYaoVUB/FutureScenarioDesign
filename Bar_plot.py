import pandas as pd
import numpy as np
import statsmodels.api as sm
from itertools import combinations
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr


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

IRR_AREA = data_to_regression[:, 25]
POP = data_to_regression[:, 26]

def plot_sort(data, num, name):
    data_to_regression = data[data[:, num].argsort()]
    x1 = [0, 14, 28, 41, 54, 67, 80, 93, 106, 119]
    x2 = [14, 28, 41, 54, 67, 80, 93, 106, 119, 132]

    IRR_ALL = np.zeros(len(x1))
    IRR_SUR = np.zeros(len(x1))
    IRR_SPR = np.zeros(len(x1))
    IRR_DRI = np.zeros(len(x1))
    GDP_ALL = np.zeros(len(x1))
    POP_ALL = np.zeros(len(x1))
    for i in range(len(x1)):
        for x in range(x1[i], x2[i]):
            IRR_ALL[i] = IRR_ALL[i] + float(data_to_regression[x, 25])
            IRR_SUR[i] = IRR_SUR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 1])
            IRR_SPR[i] = IRR_SPR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 2])
            IRR_DRI[i] = IRR_DRI[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 3])
            GDP_ALL[i] = GDP_ALL[i] + float(data_to_regression[x, num]) * float(data_to_regression[x, 26])
            POP_ALL[i] = POP_ALL[i] + float(data_to_regression[x, 26])
    FRA_SUR = IRR_SUR / IRR_ALL
    FRA_SPR = IRR_SPR / IRR_ALL
    FRA_DRI = IRR_DRI / IRR_ALL
    GDP_CAP = GDP_ALL / POP_ALL

    fig = plt.figure(figsize=(16,9))
    plt.scatter(GDP_CAP, FRA_SUR, color='red')
    plt.scatter(GDP_CAP, FRA_SPR, color='blue')
    plt.scatter(GDP_CAP, FRA_DRI, color='green')
    plt.title(name)
    plt.show()

def plot_sort_ISIMIP(data, num, name):
    data_to_regression = data[data[:, num].argsort()]
    x1 = [0, 14, 28, 41, 54, 67, 80, 93, 106, 119]
    x2 = [14, 28, 41, 54, 67, 80, 93, 106, 119, 132]
    IRR_ALL = np.zeros(len(x1))
    IRR_SUR = np.zeros(len(x1))
    IRR_SPR = np.zeros(len(x1))
    IRR_DRI = np.zeros(len(x1))
    GDP_ALL = []
    GDP_CAP = np.zeros(len(x1))
    num_cou = np.zeros(len(x1))
    for i in range(len(x1)):
        for x in range(x1[i], x2[i]):
            IRR_ALL[i] = IRR_ALL[i] + float(data_to_regression[x, 25])
            IRR_SUR[i] = IRR_SUR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 1])
            IRR_SPR[i] = IRR_SPR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 2])
            IRR_DRI[i] = IRR_DRI[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 3])
            GDP_ALL.append(float(data_to_regression[x, num]) * float(data_to_regression[x, 26]))
            num_cou = num_cou + 1
        GDP_CAP[i] = np.median(GDP_ALL)
    FRA_SUR = IRR_SUR / IRR_ALL
    FRA_SPR = IRR_SPR / IRR_ALL
    FRA_DRI = IRR_DRI / IRR_ALL

    fig = plt.figure(figsize=(16,9))
    plt.scatter(GDP_CAP, FRA_SUR, color='red')
    plt.scatter(GDP_CAP, FRA_SPR, color='blue')
    plt.scatter(GDP_CAP, FRA_DRI, color='green')
    plt.title(name)
    plt.show()

def plot_sort_SURF(data, num, name):
    data_to_regression = data[data[:, num].argsort()]
    x1 = [0, 14, 28, 41, 54, 67, 80, 93, 106, 119]
    x2 = [14, 28, 41, 54, 67, 80, 93, 106, 119, 132]
    IRR_ALL = np.zeros(len(x1))
    IRR_SUR = np.zeros(len(x1))
    IRR_SPR = np.zeros(len(x1))
    IRR_DRI = np.zeros(len(x1))
    ARE_SUR = np.zeros(len(x1))
    num_cou = np.zeros(len(x1))
    for i in range(len(x1)):
        for x in range(x1[i], x2[i]):
            IRR_ALL[i] = IRR_ALL[i] + float(data_to_regression[x, 25])
            IRR_SUR[i] = IRR_SUR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 1])
            IRR_SPR[i] = IRR_SPR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 2])
            IRR_DRI[i] = IRR_DRI[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 3])
            ARE_SUR[i] = ARE_SUR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, num])
    FRA_SUR = IRR_SUR / IRR_ALL
    FRA_SPR = IRR_SPR / IRR_ALL
    FRA_DRI = IRR_DRI / IRR_ALL
    FRA_CFT = ARE_SUR / IRR_ALL

    fig = plt.figure(figsize=(16,9))
    plt.scatter(FRA_CFT, FRA_SUR, color='red')
    plt.scatter(FRA_CFT, FRA_SPR, color='blue')
    plt.scatter(FRA_CFT, FRA_DRI, color='green')
    plt.title(name)
    plt.show()

plot_sort(data_to_regression, 4, 'GDP')
plot_sort(data_to_regression, 5, 'GOV')
plot_sort(data_to_regression, 6, 'URB')
plot_sort(data_to_regression, 7, 'GII')

plot_sort_ISIMIP(data_to_regression, 8, 'APUSE')
plot_sort_ISIMIP(data_to_regression, 9, 'APWW')
plot_sort_ISIMIP(data_to_regression, 10, 'PR')
plot_sort_ISIMIP(data_to_regression, 11, 'PPET')
plot_sort_ISIMIP(data_to_regression, 12, 'TWS')
plot_sort_ISIMIP(data_to_regression, 13, 'TAS')

plot_sort_SURF(data_to_regression, 14, 'CFT_SUR')
plot_sort_SURF(data_to_regression, 15, 'CFT_SPR')
plot_sort_SURF(data_to_regression, 16, 'CFT_DRI')

plot_sort_SURF(data_to_regression, 20, 'CFT_MAX')
plot_sort_SURF(data_to_regression, 21, 'CFT_MORE')
plot_sort_SURF(data_to_regression, 22, 'CFT_NOR')
plot_sort_SURF(data_to_regression, 23, 'CFT_MIN')
plot_sort_SURF(data_to_regression, 24, 'CFT_MAXMORE')
plot_sort_SURF(data_to_regression, 17, 'IRR_FRA')
plot_sort(data_to_regression, 18, 'IRR_per_POP')

data_to_regression = data_to_regression[data_to_regression[:, 18].argsort()]
x1 = [0, 14, 28, 41, 54, 67, 80, 93, 106, 119]
x2 = [14, 28, 41, 54, 67, 80, 93, 106, 119, 132]
IRR_ALL = np.zeros(len(x1))
IRR_SUR = np.zeros(len(x1))
IRR_SPR = np.zeros(len(x1))
IRR_DRI = np.zeros(len(x1))
ARE_TOT = np.zeros(len(x1))
POP_TOT = np.zeros(len(x1))
for i in range(len(x1)):
    for x in range(x1[i], x2[i]):
        IRR_ALL[i] = IRR_ALL[i] + float(data_to_regression[x, 25])
        IRR_SUR[i] = IRR_SUR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 1])
        IRR_SPR[i] = IRR_SPR[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 2])
        IRR_DRI[i] = IRR_DRI[i] + float(data_to_regression[x, 25]) * float(data_to_regression[x, 3])
        ARE_TOT[i] = ARE_TOT[i] + float(data_to_regression[x, 26]) * float(data_to_regression[x, 18])
        POP_TOT[i] = POP_TOT[i] + float(data_to_regression[x, 26]) * (100 - float(data_to_regression[x, 6])) / 100
FRA_SUR = IRR_SUR / IRR_ALL
FRA_SPR = IRR_SPR / IRR_ALL
FRA_DRI = IRR_DRI / IRR_ALL
FRA_CFT = ARE_TOT / POP_TOT

fig = plt.figure(figsize=(16,9))
plt.scatter(FRA_CFT, FRA_SUR, color='red')
plt.scatter(FRA_CFT, FRA_SPR, color='blue')
plt.scatter(FRA_CFT, FRA_DRI, color='green')
plt.title('IRR_per_rural_POP')
plt.show()