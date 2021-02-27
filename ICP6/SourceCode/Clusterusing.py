import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn import preprocessing
from sklearn import metrics

sns.set(style="white", color_codes=True)
warnings.filterwarnings("ignore")

# read data from csv
cc_data = pd.read_csv('CC.csv')

# see how many samples we have of each tenure
# print(cc_data["TENURE"].value_counts())

# removing null values
df1 = pd.DataFrame(cc_data.isnull().sum().sort_values(ascending=False)[:25])
df1.columns = ['Null Count']
df1.index.name = 'Feature'
# print(df1)
cc_data.loc[(cc_data['MINIMUM_PAYMENTS'].isnull() == True), 'MINIMUM_PAYMENTS'] = cc_data['MINIMUM_PAYMENTS'].mean()
cc_data.loc[(cc_data['CREDIT_LIMIT'].isnull() == True), 'CREDIT_LIMIT'] = cc_data['CREDIT_LIMIT'].mean()
x = cc_data.iloc[:, 1:-1]

# elbow method to find number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
# print(wcss)
plt.plot(range(1, 11), wcss)
plt.title('Elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Kmeans Score')
plt.show()

# nclusters = 3  # this is the k in kmeans
kmeans = KMeans(3)
kmeans.fit(x)
y_cluster_kmeans = kmeans.predict(x)
print("silhouette score: ", metrics.silhouette_score(x, y_cluster_kmeans))

# Applying kmeans on scaled features
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array, columns=x.columns)
scaled_kmeans = KMeans(3)
scaled_kmeans.fit(x_scaled)
y_scaled_kmeans = scaled_kmeans.predict(x_scaled)
print("silhouette score after scaling:", metrics.silhouette_score(x_scaled, y_scaled_kmeans))


# Applying PCA on given data set without scaling
pca = PCA(3)
x_pca = pca.fit_transform(x)
df2 = pd.DataFrame(x_pca)
df3 = pd.concat([df2, cc_data[['TENURE']]], axis=1)

# Applying KMeans on PCA result
kmeans = KMeans(3)
kmeans.fit(x_pca)
y_pca_kmeans = kmeans.predict(x_pca)
print("silhouette score after applying PCA: ", metrics.silhouette_score(x_pca, y_pca_kmeans))
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_pca_kmeans, s=50)
plt.show()
