from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
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


#----------------------------------------------------------------------------------------#
# Step 1: training data

# X = [i for i in range(10)]
# Y = [random.gauss(x,0.75) for x in X]

X = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 2, 3]
Y = [1, 2, 2, 0, 1, 4, 1, 1, 4, 7, 0, 5, 8, 0, 4, 2, 9]

X = np.array(X)
Y = np.array(Y)

Y = Y[X.argsort()]
X = X[X.argsort()]

# X.sort()
# X.sort()
print(X)
print(Y)

X = np.asarray(X)
Y = np.asarray(Y)

X = X[:, np.newaxis]
Y = Y[:, np.newaxis]

plt.scatter(X, Y)

nb_degree = 4

poly_reg = PolynomialFeatures(degree=nb_degree)

X_TRANSF = poly_reg.fit_transform(X)

poly_reg.fit(X_TRANSF, Y)

lin_reg = LinearRegression()
lin_reg.fit(X_TRANSF, Y)
plt.plot(X, lin_reg.predict(X_TRANSF))

plt.show()



import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


pump_1_filtred_df = pd.DataFrame({
    'pump_in': filtred_data['pump_1_in'],
    'pump_out': filtred_data['pump_1_out'],
    'pump_mass': filtred_data['pump_1_mass'],
    'pump_temp': filtred_data['pump_1_temp'],
    'pump_revs': filtred_data['pump_1_revs'],
    'pump_amper': filtred_data['pump_1_amper'],
    'pump_eff': filtred_data['pump_1_eff'],
    
})

train_dataset = pump_1_filtred_df.sample(frac=0.8,random_state=0)
test_dataset = pump_1_filtred_df.drop(train_dataset.index)


train_stats = train_dataset.describe()
train_stats.pop("pump_eff")
train_stats = train_stats.transpose()
train_stats

train_labels = train_dataset.pop('pump_eff')
test_labels = test_dataset.pop('pump_eff')

def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
example_result

EPOCHS = 1000

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0)


from tensorflow import keras

keras.activations.