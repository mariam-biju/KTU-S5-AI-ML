import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pd.read_csv("Ice_cream selling data.csv")
X = data['Temperature (°C)'].values.reshape(-1, 1)
y = data['Ice Cream Sales (units)'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

degree = 2
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
model = LinearRegression()
model.fit(X_train_poly, y_train)
y_train_pred = model.predict(X_train_poly)
y_test_pred = model.predict(X_test_poly)

#train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

#print(f"Train MSE: {train_mse}")
print(f"Test MSE: {test_mse}")

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, color='red', label='Training Data')
X_train_sorted = np.sort(X_train, axis=0)
X_train_poly_sorted = poly.transform(X_train_sorted)
y_train_pred_sorted = model.predict(X_train_poly_sorted)
plt.plot(X_train_sorted, y_train_pred_sorted, color='blue', label=f'Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Ice Cream Profits')
plt.title('Training Data and Polynomial Regression')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, color='green', label='Test Data')
X_test_sorted = np.sort(X_test, axis=0)
X_test_poly_sorted = poly.transform(X_test_sorted)
y_test_pred_sorted = model.predict(X_test_poly_sorted)
plt.plot(X_test_sorted, y_test_pred_sorted, color='blue', label=f'Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Ice Cream Profits')
plt.title('Testing Data and Polynomial Regression')
plt.legend()
plt.tight_layout()
plt.show()

user_temp = float(input("Enter the temperature to predict ice cream profits: "))
user_temp_poly = poly.transform([[user_temp]])
predicted_profit = model.predict(user_temp_poly)
print(f"Predicted ice cream profits for temperature {user_temp}°C: ${predicted_profit[0]:.2f}")
