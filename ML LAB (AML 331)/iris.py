import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names
feature_names = iris.feature_names

# Create a DataFrame
df = pd.DataFrame(data, columns=feature_names)
df['species'] = target

# Set the figure size
plt.figure(figsize=(8, 6))

# Plot "Sepal length vs Sepal Width"
for species in range(len(target_names)):
    subset = df[df['species'] == species]
    plt.scatter(subset[feature_names[0]], subset[feature_names[1]], label=target_names[species])

plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('Sepal Length vs Sepal Width')
plt.legend()
plt.show()
