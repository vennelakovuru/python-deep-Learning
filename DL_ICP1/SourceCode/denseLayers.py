import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:8], dataset[:, 8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=8, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,  verbose=0, initial_epoch=0)
print("\nSummary before adding Dense Layers: \n")
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))

# Adding dense layers
my_next_nn = Sequential()  # create model
my_next_nn.add(Dense(20, input_dim=8, activation='relu'))  # hidden layer
my_next_nn.add(Dense(10, input_dim=8, activation='relu'))  # hidden layer
my_next_nn.add(Dense(5, input_dim=8, activation='relu'))  # hidden layer

my_next_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_next_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

my_next_nn_fitted = my_next_nn.fit(X_train, Y_train, epochs=100,  verbose=0, initial_epoch=0)

print("\nSummary after adding Dense Layers: \n")
print(my_next_nn.summary())
print(my_next_nn.evaluate(X_test, Y_test))

