from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Example Data: 2D points
iris = load_iris()
X = iris.data  # Features
y = iris.target

# Applying K-Means with k=2
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

# Getting the cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizing the clusters and centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='grey', marker='X')  # Mark centroids
plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Output the cluster labels and centroids
print("Cluster Labels:", labels)
print("Cluster Centroids:", centroids)

new_data = [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.7, 1.5], [7.2, 3.6, 6.1, 2.5]]  # Example new points
predicted_clusters = kmeans.predict(new_data)

print("\nNew data points:\n", new_data)
print("Predicted clusters for new data points:", predicted_clusters)
