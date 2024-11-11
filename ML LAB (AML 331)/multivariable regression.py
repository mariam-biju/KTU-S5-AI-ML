import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('BostonHousing.csv')  
print("Dataset Preview:")
print(data.head())
data = data.dropna()  
feature_columns = ['CRIM', 'AGE', 'TAX']
target_column = 'MEDV'
X = data[feature_columns]
y = data['MEDV']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
#train_r2 = r2_score(y_train, y_train_pred)
#test_r2 = r2_score(y_test, y_test_pred)

print(f"Training Mean Squared Error (MSE): {train_mse}")
#print(f"Training R² Score: {train_r2}")
print(f"Testing Mean Squared Error (MSE): {test_mse}")
#print(f"Testing R² Score: {test_r2}")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, color='blue', label='Training Predictions')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('Training Data Predictions')
plt.legend()


plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, color='red', label='Testing Predictions')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('Testing Data Predictions')
plt.legend()
#plt.tight_layout()
plt.show()
