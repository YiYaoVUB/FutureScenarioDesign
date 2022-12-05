import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

def read_csv_data(filename, encode='ANSI'):     # get the socioeconomic data and ISIMIP data from csv
    pd_reader = pd.read_csv(filename, encoding=encode, header=None)
    data = np.array(pd_reader)
    return data[:, 1:]

data_to_regression = read_csv_data('C:\Research2\Regression\Data_Regression_more_than_1000.csv')
Y_train = data_to_regression[:, 1:4]
X_train = data_to_regression[:, 4:]


regressor = MLPRegressor(random_state=1, max_iter=500, activation='relu', hidden_layer_sizes=1)
regressor.n_layers_ = 2
regressor.out_activation_ = 'softmax'
regressor.n_outputs_ = 4
regressor.fit(X_train, Y_train)
Y_pred = regressor.predict(X_train)
plt.scatter(Y_train[:, 0], Y_pred[:, 0], color='red')
plt.scatter(Y_train[:, 1], Y_pred[:, 1], color='blue')
plt.scatter(Y_train[:, 2], Y_pred[:, 2], color='green')
plt.scatter(Y_train[:, 0]+Y_train[:, 1]+Y_train[:, 2], Y_pred[:, 0]+Y_pred[:, 1]+Y_pred[:, 2], color='black')
plt.show()





print('test')