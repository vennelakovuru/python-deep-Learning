import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Reading data
traindf = pd.read_csv('glass.csv')
X = traindf.drop("Type", axis=1)
Y = traindf["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Using the Naive Bayes classifier model and training the model with the train sets using the fit method
NaiveModel = GaussianNB()
NaiveModel.fit(X_test, y_test)
y_pred = NaiveModel.predict(X_test)

accuracy_score(y_test, y_pred)
print("Classification report for Naive Bayes model:\n", classification_report(y_test, y_pred))
