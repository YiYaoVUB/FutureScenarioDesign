import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
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
CFT_HIGH = data_to_regression[:, 25]

def normalize_data(data_array):
    data_after = [(x-min(data_array)) / (max(data_array) - min(data_array)) for x in data_array]
    return data_after

GDP_after = np.array(normalize_data(GDP))
GOV_after = np.array(normalize_data(GOV))
URB_after = np.array(normalize_data(URB))
GII_after = np.array(normalize_data(GII))
GII_after = 1 - GII_after

PR_after = np.array(normalize_data(PR))
TWS_after = np.array(normalize_data(TWS))

X = np.array([GDP_after, GOV_after, URB_after, GII_after])
#   X = np.array([PR_after, TWS_after])
X = X.T
pca = PCA(n_components=2)
pca.fit(X)
var = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)
#print(pca.components_)

var_after = np.array(normalize_data(var[:,0]))
np.savetxt("C:\Research2\Regression\PCA_res.txt", var[:,0])
np.savetxt("C:\Research2\Regression\PCA_res_after_normalization1.txt", var_after)
print('test')