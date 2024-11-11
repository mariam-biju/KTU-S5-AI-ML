from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Example Data: 2D points
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])

# Applying DBSCAN
dbscan = DBSCAN(eps=3, min_samples=2)
dbscan.fit(X)

# Getting the cluster labels
labels = dbscan.labels_

# Visualizing the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma')
plt.title("DBSCAN Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Output the labels
print("Cluster Labels:", labels)
