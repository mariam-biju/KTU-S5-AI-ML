import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

n = int(input("Enter the number of data points: "))

X_values = []
y_values = []
print("Enter the values:")
for i in range(n):
    x = float(input(f"Enter value for X[{i}]: "))
    y = float(input(f"Enter value for y[{i}]: "))
    X_values.append(x)
    y_values.append(y)

X = np.array(X_values).reshape(-1, 1)
y = np.array(y_values).reshape(-1, 1)

df = pd.DataFrame({'Col_0': X.flatten(), 'Col_1': y.flatten()})
print("\nGenerated DataFrame:")
print(df)

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print(f"\nCoefficients: {model.coef_[0][0]}")
print(f"Intercept: {model.intercept_[0]}")

plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Fitted Line')
plt.xlabel('Col_0')
plt.ylabel('Col_1')
plt.title('Linear Regression')
plt.legend()

x_new = float(input("Enter a new X value to predict y: "))
y_new_pred = model.predict(np.array([[x_new]]))
print(f"Predicted y : {y_new_pred[0][0]}")

plt.show()


