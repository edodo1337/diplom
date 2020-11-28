import pandas as pd

file = "aes_data.xlsx"

# data = pd.read_excel(file)

# print(data.head())

# from iapws import IAPWS97, IAPWS95

# sat_steam = IAPWS97(P=1, x=1)
# sat_liquid = IAPWS97(T=300, x=0)  # saturated liquid with known T
# steam = IAPWS97(P=0.1, T=300)  # steam with known P and T

# water1 = IAPWS97(P=1, T=380)
# water2 = IAPWS95(P=1, T=380)

# print(water1.rho, water1.phase)
# print(water2.rho, water2.phase)

from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
import numpy as np
import random

#----------------------------------------------------------------------------------------#
# Step 1: training data

X = [i for i in range(10)]
Y = [random.gauss(x,0.75) for x in X]

X = np.asarray(X)
Y = np.asarray(Y)

X = X[:,np.newaxis]
Y = Y[:,np.newaxis]

plt.scatter(X,Y)

nb_degree = 4

poly_reg = PolynomialFeatures(degree = nb_degree)

X_TRANSF = poly_reg.fit_transform(X)

poly_reg.fit(X_TRANSF, Y)

lin_reg = LinearRegression()
lin_reg.fit(X_TRANSF,Y)
plt.plot(X,lin_reg.predict(X_TRANSF))

plt.show()