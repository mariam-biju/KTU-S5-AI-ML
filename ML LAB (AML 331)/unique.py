import numpy as np
import pandas as pd

n = int(input("Enter the dimension: "))
array = np.zeros((n, n))
print("Enter the elements:")
for i in range(n):
    for j in range(n):
        array[i, j] = int(input(f"Element [{i + 1}, {j + 1}]: "))
df = pd.DataFrame(array, columns=[f'Col{i}' for i in range(n)])
print("\nDataFrame:")
print(df)
unique_rows = df[~df.duplicated(keep=False)]
print("\nUnique rows:")
print(unique_rows)
