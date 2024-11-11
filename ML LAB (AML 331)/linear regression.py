import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("advertising.csv")
X = data[['TV']]  
y = data['Sales']
model = LinearRegression()
model.fit(X, y)
predicted_sales = model.predict(X)

plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, predicted_sales, color='red', label='Regression Line')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.title('Linear Regression: TV Advertising vs Sales')
plt.legend()
plt.show()

mse = mean_squared_error(y, predicted_sales)
print(f"Mean Squared Error: {mse}")

tv_input = float(input("Enter TV advertising budget: "))
tv_input_df = pd.DataFrame({'TV': [tv_input]})  # Convert to DataFrame with the same column name
predicted_value = model.predict(tv_input_df)
print(f"Predicted Sales for TV advertising budget of {tv_input}: {predicted_value[0]}")
