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
CFT_SUR = data_to_regression[:, 13]
CFT_SPR = data_to_regression[:, 14]
CFT_DRI = data_to_regression[:, 15]

def normalize_data(data_array):
    data_after = [(x-min(data_array)) / (max(data_array) - min(data_array)) for x in data_array]
    return data_after

def LinearRegre(y, X):
    X = sm.add_constant(X)
    regression = sm.OLS(y, X)
    model = regression.fit()
    print(model.summary())
    return model.params, model.rsquared, model.pvalues

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
CFT_SUR_after = np.array(normalize_data(CFT_SUR))
CFT_SUR_after_reshape = CFT_SUR_after.reshape(-1, 1)
CFT_SPR_after = np.array(normalize_data(CFT_SPR))
CFT_SPR_after_reshape = CFT_SPR_after.reshape(-1, 1)
CFT_DRI_after = np.array(normalize_data(CFT_DRI))
CFT_DRI_after_reshape = CFT_DRI_after.reshape(-1, 1)



X_candid = np.array((GDP_after, GOV_after, URB_after, GII_after, APUSE_after, APWW_after, PR_after, PPET_after, TWS_after, CFT_SUR_after, CFT_SPR_after, CFT_DRI_after))
X_candid_reshape = np.array((GDP_after_reshape, GOV_after_reshape, URB_after_reshape, GII_after_reshape, APUSE_after_reshape, APWW_after_reshape, PR_after_reshape, PPET_after_reshape, TWS_after_reshape, CFT_SUR_after_reshape, CFT_SPR_after_reshape, CFT_DRI_after_reshape))
str_candid = ["GDP", "GOV", "URB", "GII", "APUSE", "APWW", "PR", "PPET", "TWS", "CFT_SUR", "CFT_SPR", "CFT_DRI"]
y_class = np.array((SUR_after, SPR_after, DRI_after))
print('test')

def multi_var_regression(var_number, output_SUR, output_SPR, output_DRI):
    var_combi = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], var_number))
    combi_number = len(var_combi)
    param_var_SUR = np.zeros([combi_number, var_number + 1])
    rsquared_var_SUR = np.zeros([combi_number])
    pvalues_var_SUR = np.zeros([combi_number, var_number + 1])
    param_var_SPR = np.zeros([combi_number, var_number + 1])
    rsquared_var_SPR = np.zeros([combi_number])
    pvalues_var_SPR = np.zeros([combi_number, var_number + 1])
    param_var_DRI = np.zeros([combi_number, var_number + 1])
    rsquared_var_DRI = np.zeros([combi_number])
    pvalues_var_DRI = np.zeros([combi_number, var_number + 1])
    for row in range(combi_number):
        combination = var_combi[row]
        for_X = []
        for var_index in range(var_number):
            for_X.append(X_candid[combination[var_index], :])
        X = np.c_[for_X]
        X = X.T
        param_var_SUR[row, :], rsquared_var_SUR[row], pvalues_var_SUR[row, :] = LinearRegre(SUR_after, X)
        param_var_SPR[row, :], rsquared_var_SPR[row], pvalues_var_SPR[row, :] = LinearRegre(SPR_after, X)
        param_var_DRI[row, :], rsquared_var_DRI[row], pvalues_var_DRI[row, :] = LinearRegre(DRI_after, X)
    file_obj_SUR = open(output_SUR, 'w')
    file_obj_SPR = open(output_SPR, 'w')
    file_obj_DRI = open(output_DRI, 'w')
    for var_id in range(combi_number):
        combination = var_combi[var_id]
        str_SUR = ''
        str_SPR = ''
        str_DRI = ''
        for var_num in range(var_number):
            str_SUR = str_SUR + str(str_candid[combination[var_num]]) + ','
            str_SPR = str_SPR + str(str_candid[combination[var_num]]) + ','
            str_DRI = str_DRI + str(str_candid[combination[var_num]]) + ','
        for coef_index in range(var_number + 1):
            if pvalues_var_SUR[var_id, coef_index] < 0.01:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.05:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.1:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '*,'
            else:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + ','

            if pvalues_var_SPR[var_id, coef_index] < 0.01:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.05:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.1:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '*,'
            else:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + ','

            if pvalues_var_DRI[var_id, coef_index] < 0.01:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.05:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.1:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '*,'
            else:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + ','
        str_SUR = str_SUR + str(rsquared_var_SUR[var_id])
        str_SPR = str_SPR + str(rsquared_var_SPR[var_id])
        str_DRI = str_DRI + str(rsquared_var_DRI[var_id])
        file_obj_SUR.write(str_SUR + '\n')
        file_obj_SPR.write(str_SPR + '\n')
        file_obj_DRI.write(str_DRI + '\n')

#   test_model = LogisticRegression().fit(X=X_candid.T, y=SUR_after)

#   print(test_model.score(X_candid.T, SPR_after))




#   ONE-VAR regression
multi_var_regression(1, "C:\Research2\Regression\SUR_one.csv", "C:\Research2\Regression\SPR_one.csv", "C:\Research2\Regression\DRI_one.csv")
#   TWO-VAR regression
multi_var_regression(2, "C:\Research2\Regression\SUR_two.csv", "C:\Research2\Regression\SPR_two.csv", "C:\Research2\Regression\DRI_two.csv")
#   THREE-VAR regression
multi_var_regression(3, "C:\Research2\Regression\SUR_three.csv", "C:\Research2\Regression\SPR_three.csv", "C:\Research2\Regression\DRI_three.csv")
#   FOUR-VAR regression
multi_var_regression(4, "C:\Research2\Regression\SUR_four.csv", "C:\Research2\Regression\SPR_four.csv", "C:\Research2\Regression\DRI_four.csv")
#   FIVE-VAR regression
multi_var_regression(5, "C:\Research2\Regression\SUR_five.csv", "C:\Research2\Regression\SPR_five.csv", "C:\Research2\Regression\DRI_five.csv")
#   SIX-VAR regression
multi_var_regression(6, "C:\Research2\Regression\SUR_six.csv", "C:\Research2\Regression\SPR_six.csv", "C:\Research2\Regression\DRI_six.csv")
#   SEVEN-VAR regression
multi_var_regression(7, "C:\Research2\Regression\SUR_seven.csv", "C:\Research2\Regression\SPR_seven.csv", "C:\Research2\Regression\DRI_seven.csv")
#   EIGHT-VAR regression
multi_var_regression(8, "C:\Research2\Regression\SUR_eight.csv", "C:\Research2\Regression\SPR_eight.csv", "C:\Research2\Regression\DRI_eight.csv")
#   NINE-VAR regression
multi_var_regression(9, "C:\Research2\Regression\SUR_nine.csv", "C:\Research2\Regression\SPR_nine.csv", "C:\Research2\Regression\DRI_nine.csv")

multi_var_regression(10, "C:\Research2\Regression\SUR_ten.csv", "C:\Research2\Regression\SPR_ten.csv", "C:\Research2\Regression\DRI_ten.csv")

multi_var_regression(11, "C:\Research2\Regression\SUR_eleven.csv", "C:\Research2\Regression\SPR_eleven.csv", "C:\Research2\Regression\DRI_eleven.csv")

multi_var_regression(12, "C:\Research2\Regression\SUR_twelve.csv", "C:\Research2\Regression\SPR_twelve.csv", "C:\Research2\Regression\DRI_twelve.csv")

def one_var_poly_reg(output_SUR, output_SPR, output_DRI):
    param_var_SUR = np.zeros([9, 3])
    param_var_SPR = np.zeros([9, 3])
    param_var_DRI = np.zeros([9, 3])

    pvalues_var_SUR = np.zeros([9, 3])
    pvalues_var_SPR = np.zeros([9, 3])
    pvalues_var_DRI = np.zeros([9, 3])

    rsquared_var_SUR = np.zeros([9])
    rsquared_var_SPR = np.zeros([9])
    rsquared_var_DRI = np.zeros([9])

    file_obj_SUR = open(output_SUR, 'w')
    file_obj_SPR = open(output_SPR, 'w')
    file_obj_DRI = open(output_DRI, 'w')
    for var_id in range(9):
        x_data = X_candid[var_id, :]
        poly_reg = PolynomialFeatures(degree=2)
        X_poly = poly_reg.fit_transform(x_data.reshape(-1,1))
        X = np.c_[X_poly]
        param_var_SUR[var_id, :], rsquared_var_SUR[var_id], pvalues_var_SUR[var_id, :] = LinearRegre(SUR_after, X)
        param_var_SPR[var_id, :], rsquared_var_SPR[var_id], pvalues_var_SPR[var_id, :] = LinearRegre(SPR_after, X)
        param_var_DRI[var_id, :], rsquared_var_DRI[var_id], pvalues_var_DRI[var_id, :] = LinearRegre(DRI_after, X)


    for var_id in range(9):
        str_SUR = ''
        str_SPR = ''
        str_DRI = ''

        str_SUR = str_SUR + str(str_candid[var_id]) + ','
        str_SPR = str_SPR + str(str_candid[var_id]) + ','
        str_DRI = str_DRI + str(str_candid[var_id]) + ','

        for coef_index in range(3):
            if pvalues_var_SUR[var_id, coef_index] < 0.01:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index],4)) + '***,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.05:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index],4)) + '**,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.1:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index],4)) + '*,'
            else:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index],4)) + ','

            if pvalues_var_SPR[var_id, coef_index] < 0.01:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index],4)) + '***,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.05:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index],4)) + '**,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.1:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index],4)) + '*,'
            else:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index],4)) + ','

            if pvalues_var_DRI[var_id, coef_index] < 0.01:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index],4)) + '***,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.05:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index],4)) + '**,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.1:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index],4)) + '*,'
            else:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index],4)) + ','


        str_SUR = str_SUR + str(rsquared_var_SUR[var_id])
        str_SPR = str_SPR + str(rsquared_var_SPR[var_id])
        str_DRI = str_DRI + str(rsquared_var_DRI[var_id])
        file_obj_SUR.write(str_SUR + '\n')
        file_obj_SPR.write(str_SPR + '\n')
        file_obj_DRI.write(str_DRI + '\n')


#one_var_poly_reg('C:\Research2\Regression\SUR_one_square.csv', 'C:\Research2\Regression\SPR_one_square.csv', 'C:\Research2\Regression\DRI_one_square.csv')



def two_var_poly_reg(output_SUR, output_SPR, output_DRI):
    var_combi = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))
    combi_number = len(var_combi)

    param_var_SUR = np.zeros([combi_number, 6])
    param_var_SPR = np.zeros([combi_number, 6])
    param_var_DRI = np.zeros([combi_number, 6])

    pvalues_var_SUR = np.zeros([combi_number, 6])
    pvalues_var_SPR = np.zeros([combi_number, 6])
    pvalues_var_DRI = np.zeros([combi_number, 6])

    rsquared_var_SUR = np.zeros([combi_number])
    rsquared_var_SPR = np.zeros([combi_number])
    rsquared_var_DRI = np.zeros([combi_number])

    file_obj_SUR = open(output_SUR, 'w')
    file_obj_SPR = open(output_SPR, 'w')
    file_obj_DRI = open(output_DRI, 'w')

    for row in range(combi_number):
        combination = var_combi[row]
        var1 = combination[0]
        var2 = combination[1]
        poly_reg = PolynomialFeatures(degree=2)
        X_poly = poly_reg.fit_transform(np.hstack((X_candid_reshape[var1, :], X_candid_reshape[var2, :])))

        X = np.c_[X_poly]
        param_var_SUR[row, :], rsquared_var_SUR[row], pvalues_var_SUR[row, :] = LinearRegre(SUR_after, X)
        param_var_SPR[row, :], rsquared_var_SPR[row], pvalues_var_SPR[row, :] = LinearRegre(SPR_after, X)
        param_var_DRI[row, :], rsquared_var_DRI[row], pvalues_var_DRI[row, :] = LinearRegre(DRI_after, X)

    for var_id in range(combi_number):
        combination = var_combi[var_id]
        var1 = combination[0]
        var2 = combination[1]

        str_SUR = ''
        str_SPR = ''
        str_DRI = ''

        str_SUR = str_SUR + str(str_candid[var1]) + ',' + str(str_candid[var2]) + ','
        str_SPR = str_SPR + str(str_candid[var1]) + ',' + str(str_candid[var2]) + ','
        str_DRI = str_DRI + str(str_candid[var1]) + ',' + str(str_candid[var2]) + ','

        for coef_index in range(6):
            if pvalues_var_SUR[var_id, coef_index] < 0.01:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.05:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_SUR[var_id, coef_index] < 0.1:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + '*,'
            else:
                str_SUR = str_SUR + str(round(param_var_SUR[var_id, coef_index], 4)) + ','

            if pvalues_var_SPR[var_id, coef_index] < 0.01:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.05:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_SPR[var_id, coef_index] < 0.1:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + '*,'
            else:
                str_SPR = str_SPR + str(round(param_var_SPR[var_id, coef_index], 4)) + ','

            if pvalues_var_DRI[var_id, coef_index] < 0.01:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '***,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.05:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '**,'
            elif pvalues_var_DRI[var_id, coef_index] < 0.1:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + '*,'
            else:
                str_DRI = str_DRI + str(round(param_var_DRI[var_id, coef_index], 4)) + ','

        str_SUR = str_SUR + str(rsquared_var_SUR[var_id])
        str_SPR = str_SPR + str(rsquared_var_SPR[var_id])
        str_DRI = str_DRI + str(rsquared_var_DRI[var_id])
        file_obj_SUR.write(str_SUR + '\n')
        file_obj_SPR.write(str_SPR + '\n')
        file_obj_DRI.write(str_DRI + '\n')

# two_var_poly_reg('C:\Research2\Regression\SUR_two_square.csv', 'C:\Research2\Regression\SPR_two_square.csv', 'C:\Research2\Regression\DRI_two_square.csv')



