import pandas as pd
import csv
import numpy as np
import statsmodels.tools
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import preprocessing

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



def normalize_data(data_array):
    data_after = [(x-min(data_array)) / (max(data_array) - min(data_array)) for x in data_array]
    return data_after


def LinearRegre(y, X):
    X = sm.add_constant(X)
    regression = sm.OLS(y, X)
    model = regression.fit()
    print(model.summary())
    return model.params, model.rsquared_adj, model.pvalues
SUR_after = np.array(normalize_data(SUR))
SPR_after = np.array(normalize_data(SPR))
DRI_after = np.array(normalize_data(DRI))
GDP_after = np.array(normalize_data(GDP))
GOV_after = np.array(normalize_data(GOV))
URB_after = np.array(normalize_data(URB))



X = np.c_[GDP_after, GOV_after, URB_after]
params, rsquared, pvalues = LinearRegre(SUR_after, X)



print('test')