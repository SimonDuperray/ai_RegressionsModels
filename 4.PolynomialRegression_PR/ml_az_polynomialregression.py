# -*- coding: utf-8 -*-
"""ML-AZ_PolynomialRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyE823OHAjfiTuAge1pfuTg8tAmqE9JJ
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

"""<h2>Training the Linear Regression model on the whole dataset</h2>"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

"""<h2>Training the Polynomial Regression model on the whole dataset</h2>"""

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

poly_reg_4 = PolynomialFeatures(degree=4)
X_poly4 = poly_reg_4.fit_transform(X)
lin_reg_4 = LinearRegression()
lin_reg_4.fit(X_poly4, y)

"""<h2>Visualising the Linear Regression results</h2>"""

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title("Truth of Bluff (Linear Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""<h2>Visualising the Polynomial Regression results</h2>

<h3>Degree 2</h3>
"""

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(X_poly), color='blue')
plt.title("Degree 2 (Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_4.predict(X_poly4), color='blue')
plt.title("Degree 4 (Polynomial Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""<h2>Visualising Polynomial Regression Model (smoothest curve)</h2>"""

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_4.predict(poly_reg_4.fit_transform(X_grid)), color = 'blue')
plt.title('Degree 4 - Smoothest Curve (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""<h2>Predicting a new result with Linear Regression</h2>"""

lin_reg.predict([[6.5]])

"""<h2>Predicting a new result with Polynomial Regression</h2>"""

lin_reg_4.predict(poly_reg_4.fit_transform([[6.5]]))