import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report

# Reading data
traindf = pd.read_csv('glass.csv')
X = traindf.drop("Type", axis=1)
Y = traindf["Type"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

SVMmodel = svm.SVC(kernel='linear')
SVMmodel.fit(X_train, y_train)
y_pred = SVMmodel.predict(X_test)
accuracy_score(y_test, y_pred) * 100
print("Classification_report for SVM model:\n", classification_report(y_test, y_pred))

