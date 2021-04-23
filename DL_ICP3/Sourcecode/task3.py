# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FXFMsAFXG3Wq2EqrAlpxnlSiJl8Qghct
"""

#Importing required packages
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt

#Downloading the dataset
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(subset='train')
from pprint import pprint
pprint(list(newsgroups.target_names))

#Selecting the categories
categories = ['sci.med', 'sci.space']
#loading the required categories data into Dataframe
newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)

#tokenizing data
sentences= newsgroups_train.data

#Target columns to label matrix
y=newsgroups_train.target

#converting Categorical data into Numerical data
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)

#tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)

#getting the vocabulary of data
sentences = tokenizer.texts_to_matrix(sentences)

# splitting into train& test
X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

#Shape of the X_train Matrix
X_train.shape[0:]

# Number of features
# print(input_dim)
model = Sequential()#Sequential Neural Network
model.add(layers.Dense(300,input_dim=2000, activation='relu'))#hidden layer with 300neurons, input layer with 2000 Neurons
model.add(layers.Dense(2, activation='softmax'))#Output layer with 2neurons, softmax as activation
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=256)

#Calculating loss & accuracy
[testloss, testaccuracy] = model.evaluate(X_test,y_test)
print("Test data evaluation: Loss = {}, accuracy = {}".format(test_loss, testaccuracy))

print(history.history.keys())

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['accuracy', 'validation accuracy','loss','validation loss'], loc='upper left')
plt.show()

#Selecting the categories
categories = ['sci.med', 'sci.space']

#loading the required categories
newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)

#data
sentences= newsgroups_train.data

#Target columns to label matrix
y=newsgroups_train.target

#converting Categorical data into Numerical data using Label Encoding
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)

#tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)

#Importing package for padding data
from keras.preprocessing.sequence import pad_sequences
#length of max sentence data
maxLength= max([len(s.split()) for s in sentences])
#Size of vocabulary
vocab_size= len(tokenizer.word_index)+1
#Vector Tokenization
sentences_pre = tokenizer.texts_to_sequences(sentences)
#Padding
padded_docs= pad_sequences(sentences_pre,maxlen=maxLength)

#splitting into test data and train data
X_train, X_test, y_train, y_test = train_test_split(padded_docs, y, test_size=0.25, random_state=1000)
maxLength

from keras.layers import Embedding, Flatten
#Sequential Neural Network model
model = Sequential()
#Embedding layer with 8648 neurons
model.add(Embedding(vocab_size, 50, input_length=6141))
#Flattening Network
model.add(Flatten())
#hidden layer 300neurons, input layer 8648 Neurons
model.add(layers.Dense(300, activation='relu',input_dim=8648))
#Output layer 2neurons, softmax as activation
model.add(layers.Dense(2, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=256)

#Calculating loss & accuracy
[testloss1, testaccuracy1] = model.evaluate(X_test,y_test)
print("Test Data Evaluation: Loss = {}, accuracy = {}".format(testloss1, testaccuracy1))

print(history.history.keys())

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['accuracy', 'validation accuracy','loss','val_loss'], loc='upper left')
plt.show()

print("Test Data result  : Loss = {}, accuracy = {}".format(testloss, testaccuracy))
print("Test Data result with Embedded layer: Loss = {}, accuracy = {}".format(testloss1, testaccuracy1))
print("Actual Value:",y_test[5],"Predicted Value",model.predict_classes(X_test[[5],:]))