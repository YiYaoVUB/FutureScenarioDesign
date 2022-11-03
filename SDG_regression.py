import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
import statsmodels.api as sm
from itertools import combinations
from sklearn.preprocessing import PolynomialFeatures

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

def normalize_data(data_array):
    data_after = [(x-min(data_array)) / (max(data_array) - min(data_array)) for x in data_array]
    return data_after

SUR_after = np.array(normalize_data(SUR))
SPR_after = np.array(normalize_data(SPR))
DRI_after = np.array(normalize_data(DRI))
GDP_after = np.array(normalize_data(GDP))
GDP_after_reshape = GDP_after.reshape(-1, 1)
GOV_after = np.array(normalize_data(GOV))
GOV_after_reshape = GOV_after.reshape(-1, 1)
URB_after = np.array(normalize_data(URB))
URB_after_reshape = URB_after.reshape(-1, 1)
GII_after = np.array(normalize_data(GII))
GII_after_reshape = GII_after.reshape(-1, 1)
APUSE_after = np.array(normalize_data(APUSE))
APUSE_after_reshape = APUSE_after.reshape(-1, 1)
APWW_after = np.array(normalize_data(APWW))
APWW_after_reshape = APWW_after.reshape(-1, 1)
PR_after = np.array(normalize_data(PR))
PR_after_reshape = PR_after.reshape(-1, 1)
PPET_after = np.array(normalize_data(PPET))
PPET_after_reshape = PPET_after.reshape(-1, 1)
TWS_after = np.array(normalize_data(TWS))
TWS_after_reshape = TWS_after.reshape(-1, 1)

X_candid = np.array((GDP_after, GOV_after, URB_after, GII_after, APUSE_after, APWW_after, PR_after, PPET_after, TWS_after))
X_candid_reshape = np.array((GDP_after_reshape, GOV_after_reshape, URB_after_reshape, GII_after_reshape, APUSE_after_reshape, APWW_after_reshape, PR_after_reshape, PPET_after_reshape, TWS_after_reshape))

y_class = np.array((SUR_after, SPR_after, DRI_after))


#   X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
#   Y = np.array([1, 1, 2, 2])
# Always scale the input. The most convenient way is to use a pipeline.
clf = make_pipeline(StandardScaler(),
                   SGDClassifier(max_iter=1000, tol=1e-3))

clf.fit(X_candid_reshape, y_class)
#   print(clf.predict([[-0.8, -1]]))