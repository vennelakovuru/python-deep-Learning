import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import StandardScaler

# Loading the Dataset
breastCancerData = pd.read_csv('breastcancer.csv')

# converting Categorical data into Numerical
le = LabelEncoder()
# Using Label Encoder transformer to encode target values
breastCancerData['diagnosis'] = le.fit_transform(breastCancerData['diagnosis'])

# Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(breastCancerData.iloc[:, 2:32], breastCancerData.iloc[:, 1],
                                                    test_size=0.25, random_state=87)

my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  # compilation

# Training data
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0, initial_epoch=0)
# Printing Summary
print("\n Summary Before Normalization: \n ")
print(my_first_nn.summary())
# Evaluating model
print(my_first_nn.evaluate(X_test, Y_test))

# Normalize the data before feeding the data to the model and
# check how the normalization change your accuracy

# Creating StandardScalar Model
scModel = StandardScaler()
# Fitting to data and transforming it.
X_train = scModel.fit_transform(X_train)
# Performing standardization by centering and scaling
X_test = scModel.transform(X_test)

my_next_nn = Sequential()  # create model
my_next_nn.add(Dense(20, input_dim=30, activation='relu'))  # hidden layer
my_next_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_next_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])  # compilation

# Training data
my_next_nn_fitted = my_next_nn.fit(X_train, Y_train, epochs=100, verbose=0, initial_epoch=0)
# Printing Summary
print("\n Summary After Normalization: \n")
print(my_next_nn.summary())
# Evaluating model
print(my_next_nn.evaluate(X_test, Y_test))
