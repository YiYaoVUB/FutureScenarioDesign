import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import joblib

def read_csv_data_SSP(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 2:]

def normalize_data_with_standard(data_array, data_standard):
    data_after = [(x-min(data_standard)) / (max(data_standard) - min(data_standard)) for x in data_array]
    return data_after

GDP_SSP1 = read_csv_data_SSP('C:\Research2\Socioeconomic\Data_GDP_SSP5.csv')
GOV_SSP1 = read_csv_data_SSP('C:\Research2\Socioeconomic\Data_GOV_SSP5.csv')
URB_SSP1 = read_csv_data_SSP('C:\Research2\Socioeconomic\Data_URB_SSP5.csv')
GII_SSP1 = read_csv_data_SSP('C:\Research2\Socioeconomic\Data_GII_SSP5.csv')

GDP_SSP1_after = np.zeros([151, 21])
GOV_SSP1_after = np.zeros([151, 21])
URB_SSP1_after = np.zeros([151, 21])
GII_SSP1_after = np.zeros([151, 21])

for year in range(21):
    GDP_SSP1_after[:, year] = normalize_data_with_standard(GDP_SSP1[:, year], GDP_SSP1[:, 2])   #use the data of year 2010
    GOV_SSP1_after[:, year] = normalize_data_with_standard(GOV_SSP1[:, year], GOV_SSP1[:, 2])
    URB_SSP1_after[:, year] = normalize_data_with_standard(URB_SSP1[:, year], URB_SSP1[:, 2])
    GII_SSP1_after[:, year] = normalize_data_with_standard(GII_SSP1[:, year], GII_SSP1[:, 2])

ref_X = np.array([GDP_SSP1_after[:, 2], GOV_SSP1_after[:, 2], URB_SSP1_after[:, 2], 1-GII_SSP1_after[:, 2]])
ref_X = ref_X.T
pca = PCA(n_components=4)
pca.fit(ref_X)
ref_X_after_PCA = pca.fit_transform(ref_X)
joblib.dump(pca, 'pca.m')
ref_X_after_PCA = ref_X_after_PCA[:, 0]
print(pca.explained_variance_ratio_)
print(pca.singular_values_)
#   ref_X_after_PCA_after_NOR = np.array(normalize_data(ref_X_after_PCA[:,0]))

var_after_PCA_after_NOR = np.zeros([151, 21])
var_after_PCA = np.zeros([151, 21])
for year in range(21):
    X = np.array([GDP_SSP1_after[:, year], GOV_SSP1_after[:, year], URB_SSP1_after[:, year], 1-GII_SSP1_after[:, year]])
    X = X.T
    X_after_PCA = pca.transform(X)
    X_after_PCA = X_after_PCA[:, 0]
    var_after_PCA[:, year] = X_after_PCA
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)
    X_after_PCA_after_NOR = normalize_data_with_standard(X_after_PCA, ref_X_after_PCA)
    var_after_PCA_after_NOR[:, year] = X_after_PCA_after_NOR
print('test')

np.savetxt("C:\Research2\Socioeconomic\Socio_data_SSP5.csv", var_after_PCA_after_NOR, delimiter=',')
