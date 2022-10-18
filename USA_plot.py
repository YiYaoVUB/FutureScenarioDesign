import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

pd_reader = pd.read_csv('C:\Research2\\usa_data\For_plotting.csv', encoding='ANSI')
data = np.array(pd_reader)

gdp = data[:,1]
spr = data[:,2]
dri = data[:,3]
sur = data[:,4]

pcc_coef = pearsonr(gdp, sur)
pcc_coef2 = pearsonr(gdp, spr)
pcc_coef3 = pearsonr(gdp, dri)

f = plt.figure(figsize = (10, 10), dpi=100)
plt.xlabel('GDP per capita ($)', fontsize=12)
plt.ylabel('Fraction (%)', fontsize=12)
ax1 = plt.subplot(1,1,1)
plt.scatter(gdp, spr, c='blue', label = 'sprinkler')
plt.scatter(gdp, dri, c='green', label = 'drip')
plt.scatter(gdp, sur, c='red', label = 'surface')
plt.legend(fontsize=12)

gdp_train = np.array(gdp).reshape((len(gdp), 1))
spr_train = np.array(spr).reshape((len(spr), 1))
sur_train = np.array(sur).reshape((len(sur), 1))
dri_train = np.array(dri).reshape((len(dri), 1))

lineModel = LinearRegression()
lineModel.fit(gdp_train, spr_train)

spr_pred = lineModel.predict(gdp_train)
a1 = lineModel.coef_[0][0]
b1 = lineModel.intercept_[0]
plt.plot(gdp, spr_pred, c='blue')

lineModel.fit(gdp_train, dri_train)
dri_pred = lineModel.predict(gdp_train)
plt.plot(gdp, dri_pred, c='green')
a2 = lineModel.coef_[0][0]
b2 = lineModel.intercept_[0]

lineModel.fit(gdp_train, sur_train)
sur_pred = lineModel.predict(gdp_train)
plt.plot(gdp, sur_pred, c='red')
a3 = lineModel.coef_[0][0]
b3 = lineModel.intercept_[0]


plt.show()

print('test')