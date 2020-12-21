# Decision Tree Regression

CART (Classification And Regression Trees):
* Classification Trees
* Regression Trees

To build decision trees we should stay in 2D (with the 2 independant variables (x1, x2))
Dependant variable (y) is not visible.<br><br>
[![decisiontree.png](https://i.postimg.cc/Y9vy8j70/decisiontree.png)](https://postimg.cc/HcC2kYV1)<br><br>
[![decitreepred.png](https://i.postimg.cc/fRdNy5y2/decitreepred.png)](https://postimg.cc/ZWJgD8rp)<br><br>
[![finaltree.png](https://i.postimg.cc/SxCBks1H/finaltree.png)](https://postimg.cc/BjZYCq0C)<br><br>

Entropy (get informations about that)

More precise for multi features datasets !<br><br>
[![decisiontreepredi.png](https://i.postimg.cc/7631LvrH/decisiontreepredi.png)](https://postimg.cc/tZgnrMgw)<br><br>
<br><br>

# Random Forest Regression

Ensemble Learning: when you take multiple algorithms or the same algorithm multiple times and you put them together to male something much more powerful than the original.<br>
* Step 1: Pick at random K data points from the Training set
* Step 2: Build the Decision Tree associated to these K data points
* Step 3: Choose the number NTree of trees you want to build and repeat Steps 1 & 2
* Step 4: For a new data point, make each one of your Ntree trees predict the value of Y to for the data point in question, and assign the new data point the average across all of the predicted Y values.
<br><br>
[![randomforest.png](https://i.postimg.cc/4NqrtthY/randomforest.png)](https://postimg.cc/D8Qj3S6h)<br><br>

# Evaluating Regression Models Performance

## R-Squared
Sum of squares of residuals: SSres = SUM(yi - y^i)²
Sum of squares of totlals: SStot = SUM(yi - yAVG)²

R² = 1 - (SSres/SStot)

## Ajusted R-Squared
SSres->min => R² will never decrease
Problem with a third variable for a multiple linear regression model.
