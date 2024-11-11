import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

# Data for clustering
X = np.array([[1, 2], [1, 4], [1, 0], 
              [4, 2], [4, 4], [4, 0]])

# Perform Agglomerative Hierarchical Clustering
clustering = AgglomerativeClustering(n_clusters=2, linkage='single')  # You can choose other linkages too ('single', 'complete', 'average')

# Fit the model and get the cluster labels
clustering.fit(X)

# Output the cluster labels for each point
print("Cluster labels:", clustering.labels_)

# Output the number of leaves (data points) and number of connected components
print("Number of leaves:", clustering.n_leaves_)
print("Number of connected components:", clustering.n_connected_components_)

# Output the hierarchical tree structure (children of each node)
print("Children (tree structure):")
print(clustering.children_)

# Optional: Visualize the dendrogram
# Since AgglomerativeClustering in scikit-learn does not provide direct access to the full linkage matrix,
# you can use the linkage matrix from scipy to plot a dendrogram.
from scipy.cluster.hierarchy import linkage

# Use the same data and linkage criterion to generate a linkage matrix
Z = linkage(X, method='single')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram for Agglomerative Clustering')
plt.xlabel('Index')
plt.ylabel('Distance')
plt.show()
