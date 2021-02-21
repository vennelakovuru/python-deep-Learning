import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# reading restaurant data
data = pandas.read_csv("data.csv")

# read test and train data
train = data.drop(['revenue', 'City Group', 'Type'], axis=1)
test = data["revenue"].astype(str)

# Building a linear model and training the model with the train sets using the fit method
reg = linear_model.LinearRegression()
reg.fit(train, test)
pred = reg.predict(train)

# Finding R^2 and RMSE
print("R^2: %.2f" % r2_score(test, pred))
print("RMSE: %.2f" % mean_squared_error(test, pred))
