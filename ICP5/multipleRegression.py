import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data = data.select_dtypes(include=[np.number]).interpolate().dropna()

y = np.log(data.revenue)
X = data.drop(['revenue', 'Id'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=.33)

lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

# Finding R^2 and RMSE
print("R^2: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)

print('RMSE is: \n', mean_squared_error(y_test, predictions))


sns.regplot(x=y_test, y=predictions, ci=None, color="b")
# show the plot
plt.show()
