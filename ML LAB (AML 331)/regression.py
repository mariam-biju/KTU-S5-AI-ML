import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('winequality.csv')  

print("Dataset Preview:")
print(df.head())
df = df.dropna()  

feature_columns = ['fixed acidity', 'residual sugar', 'alcohol']
target_column = 'quality'

def single_linear_regression(df):
    X = df[['fixed acidity']]  
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'\nSingle Linear Regression - \nMSE: {mse:.2f}\n')
    try:
        fixed_acidity = float(input("Enter fixed acidity for prediction: "))
        new_data = np.array([[fixed_acidity]])
        new_prediction = model.predict(new_data)
        print(f'Single Linear Regression Prediction for Fixed Acidity={fixed_acidity}: quality={new_prediction[0]:.2f}\n')
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual data')
    plt.plot(X_test, y_pred, color='red', label='Predicted line')
    plt.xlabel('Fixed Acidity')
    plt.ylabel('Quality')
    plt.title('Single Linear Regression')
    plt.legend()
    plt.show()

def multivariate_linear_regression(df):
    X = df[feature_columns]
    y = df['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Multivariate Linear Regression - \nMSE: {mse:.2f}\n')

    data = {}
    for feature in feature_columns:
        while True:
            try:
                data[feature] = float(input(f"Enter value for {feature}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    new_data = pd.DataFrame([data])
    new_prediction = model.predict(new_data)
    print(f'Multivariate Linear Regression Prediction of Quality: {new_prediction[0]:.2f}\n')

def polynomial_regression(df):
    X = df[['fixed acidity']].values  
    y = df['quality'].values

    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Polynomial Regression - \nMSE: {mse:.2f}\n')
    try:
        fixed_acidity = float(input("Enter fixed acidity for polynomial regression prediction: "))
        new_data = np.array([[fixed_acidity]])
        new_data_poly = poly.transform(new_data)
        new_prediction = model.predict(new_data_poly)
        print(f'Polynomial Regression Prediction for Fixed Acidity={fixed_acidity}: Quality= {new_prediction[0]:.2f}\n')
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")

    # Plotting the polynomial regression
    plt.figure(figsize=(10, 6))
    # Create a range of values for fixed acidity
    X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    X_range_poly = poly.transform(X_range)
    y_range_pred = model.predict(X_range_poly)

    plt.scatter(X, y, color='green', label='Actual data')
    plt.plot(X_range, y_range_pred, color='orange', label='Polynomial fit')
    plt.xlabel('Fixed Acidity')
    plt.ylabel('Quality')
    plt.title('Polynomial Regression')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    single_linear_regression(df)
    multivariate_linear_regression(df)
    polynomial_regression(df)








