import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# Reading data
data = pd.read_csv("data.csv")
# Finding the top 5 correlated features
f = data.select_dtypes(include=[np.number])
corre = f.corr()
print(corre['revenue'].sort_values(ascending=False)[:6])
# Setting up test and train data with the above got top 5 correlated features
train = data[['P2', 'P28', 'P6', 'P21', 'P11']]
test = data['revenue']
# Building a linear model and training using fit method
reg = linear_model.LinearRegression()
reg.fit(train, test)
pred = reg.predict(train)

# Finding R^2 and RMSE
print("R^2: %.2f" % r2_score(test, pred))
print("RMSE: %.2f" % mean_squared_error(test, pred))
