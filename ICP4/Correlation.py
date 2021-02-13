import pandas as pd
train = pd.read_csv('train_preprocessed.csv')
# Finding the correlation
print("correlation between ‘survived’ column and ‘sex’ column :", train['Survived'].corr(train['Sex']))
