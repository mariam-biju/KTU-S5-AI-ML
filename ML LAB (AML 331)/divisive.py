import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Data for clustering
X = np.array([[1, 2], [1, 4], [1, 0], 
              [4, 2], [4, 4], [4, 0]])

def divisive_clustering(X, n_clusters=2):
    # Step 1: Start with one large cluster
    clusters = [X]
    cluster_labels = np.zeros(X.shape[0])  # Initially, all points are in the same cluster
    
    # Step 2: Iteratively split the largest cluster until n_clusters are reached
    while len(clusters) < n_clusters:
        # Find the largest cluster (the one with the most points)
        largest_cluster = max(clusters, key=len)
        
        # Perform clustering on the largest cluster using AgglomerativeClustering
        agg_clust = AgglomerativeClustering(n_clusters=2)  # Always split into 2
        agg_clust.fit(largest_cluster)
        
        # Get the labels of the split
        labels = agg_clust.labels_
        
        # Split the largest cluster into two sub-clusters
        cluster_1 = largest_cluster[labels == 0]
        cluster_2 = largest_cluster[labels == 1]
        
        # Update the list of clusters and cluster labels
        clusters.remove(largest_cluster)
        clusters.append(cluster_1)
        clusters.append(cluster_2)
        
        # Update the cluster labels
        for i, label in enumerate(labels):
            cluster_labels[np.where(np.all(X == largest_cluster[i], axis=1))[0][0]] = label

    return cluster_labels

# Perform divisive clustering
n_clusters = 2
divisive_labels = divisive_clustering(X, n_clusters)

# Output the divisive cluster labels
print("Divisive cluster labels:", divisive_labels)

# Visualizing the clusters
plt.scatter(X[:, 0], X[:, 1], c=divisive_labels, cmap='viridis')
plt.title('Divisive Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Optional: Plot the dendrogram (using linkage for visualization)
Z = linkage(X, method='ward')
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram for Divisive Clustering (using Agglomerative)')
plt.xlabel('Index')
plt.ylabel('Distance')
plt.show()
