# Random Forest Regression

Ensemble Learning: when you take multiple algorithms or the same algorithm multiple times and you put them together to male something much more powerful than the original.<br>
* Step 1: Pick at random K data points from the Training set
* Step 2: Build the Decision Tree associated to these K data points
* Step 3: Choose the number NTree of trees you want to build and repeat Steps 1 & 2
* Step 4: For a new data point, make each one of your Ntree trees predict the value of Y to for the data point in question, and assign the new data point the average across all of the predicted Y values.
<br><br>
[![randomforest.png](https://i.postimg.cc/4NqrtthY/randomforest.png)](https://postimg.cc/D8Qj3S6h)<br><br>
