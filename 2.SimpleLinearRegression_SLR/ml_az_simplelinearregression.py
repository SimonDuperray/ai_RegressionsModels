# -*- coding: utf-8 -*-
"""ML-AZ_SimpleLinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LmCq9DnxTDPua7XFpyKWZYA2jjasurIC

<h2>Importing the libraries</h2>
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""<h2>Importing the dataset</h2>"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print("X: \n",X,"\n\ny: \n",y)

"""<h2>Splitting the dataset into the training set and the test set</h2>"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("X_train: \n",X_train,"\ny_train: \n",y_train,"\n")
print("X_test: \n",X_test,"\ny_test: \n",y_test)

"""<h2>Training the Simple Linear Regression model on the Training set</h2>"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""<h2>Predicting the Tests set results</h2>"""

y_pred = regressor.predict(X_test)

"""<h2>Visualising the Training set results</h2>"""

plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience - Training set')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""<h2>Visualising the Tests set results</h2>"""

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.title('Salary vs Experience - Test set')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()