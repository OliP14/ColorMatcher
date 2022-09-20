import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Get datatset to be clustered
iris = sns.load_dataset('iris')
iris.head()

# Trim dataset to only have 2 columns that we want to be put on the scatter plot
# Make the scatter plot
trimmedData = iris.loc[: , ['sepal_length', 'sepal_width']]
plt.scatter(x=trimmedData['sepal_length'], y=trimmedData['sepal_width'])

# Create K-Means model and fit it to the dataset we want to use
model = KMeans(n_clusters = 3)
model.fit(trimmedData)
trimmedData['label'] = model.labels_

# Create scatter plot with data, colorcoded according to the k-means results
plt.scatter(x=trimmedData['sepal_length'], y=trimmedData['sepal_width'], c=trimmedData['label'])
plt.show()