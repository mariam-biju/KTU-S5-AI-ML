from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Apply PCA, keeping all components to see their explained variance
pca = PCA()
X_pca = pca.fit_transform(X)

# Explained variance ratio for each principal component
explained_variance = pca.explained_variance_ratio_

# Plot the PCA-transformed data (2D projection)
iris_pca_df = pd.DataFrame(data=X_pca[:, :2], columns=['Principal Component 1', 'Principal Component 2'])
iris_pca_df['Species'] = y

plt.figure(figsize=(14, 5))

# Subplot 1: 2D PCA scatter plot
plt.subplot(1, 2, 1)
sns.scatterplot(data=iris_pca_df, x='Principal Component 1', y='Principal Component 2', hue='Species', palette="viridis", s=100)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Species')

# Subplot 2: Scree plot for explained variance ratio
plt.subplot(1, 2, 2)
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o', linestyle='-', color='b')
plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.xticks(range(1, len(explained_variance) + 1))
plt.grid()

plt.tight_layout()
plt.show()
