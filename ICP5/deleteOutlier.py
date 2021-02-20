import pandas as pd
import matplotlib.pyplot as plt

# Reading data
houseprice = pd.read_csv('train.csv')

# Setting Style for graph
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

# Plotting the scatter plot & labeling x,y and title
print(houseprice[['GarageArea']])
plt.scatter(houseprice.GarageArea, houseprice.SalePrice)
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Plot before removing outliers')
plt.show()

# Filtering the values and plotting the scatter plot
filtered_entries = houseprice[(houseprice.GarageArea < 1000) & (houseprice.GarageArea > 200)]
plt.scatter(filtered_entries.GarageArea, filtered_entries.SalePrice)
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Plot after removing outliers')
plt.show()
