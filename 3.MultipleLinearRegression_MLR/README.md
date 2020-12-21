# MultipleLinearRegression

[-> Repository](https://github.com/SimonDuperray/ai_MultipleLinearRegression)

## :clipboard: Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## :page_facing_up: General info
Bases of multiple linear regression model for machine learning.

### Bases
```
y = b0 + b1x1 + b2x2 + ... + bnxn
y: dependant variable
b0: constant
b1->bn: coefficients
x1->xn: independant variables
```
<b>We never use feature scaling for multiple linear regression models !!</b><br>
<b>The class used to fit and train multiple linear regression model avoids itself the dummy variable trap !!</b>

#### Assumptions of a Linear Regression Model
Before building a linear regression model, check that these assumptions are true:
* Linearity
* Homoscedasticity
* Multivariate normality
* Independence of errors
* Lack of multicollinearity

#### Dummy Variables
How implement categorical variables in multiple linear regression equations ?<br>
Equivalent of OneHotEncoder: create vector to encode categorical data.<br>
```
vector size = nb of categorical data
```

#### Dummy Variables Trap
Let's take this example:
```
There are only two types of categorical data: New York and California. To encore these data, we create a vector composed of only 2 parameters: [0 1] for NY and [1 0] for California. When NY is 0, California is 1.
```
So it is useless to take care the 2 columns. In fact, taking all columns of encoded categorical data is a trap.
```
D2=1-D1
```
You must take care of NbTotalDummyVariables-1 to don't fall in the trap.

#### P-Value
The P-Value is the probability that an outcome will occur primarly by chance. It is between 0 and 1. If it is close to 1, it means that the result is very likely to be the result of chance. On the contrary, if it os close to 0, the result is very unlikely to be the result of the chance. But there is always a risk, however small. We must therefore set a treshold from which we trust the result and its achievement.

#### Building a Model
##### 5 methods of building models
* [All-in](#AllIn)
* [Backward Elimination](#BackwardElimination)
* [Forward Selection](#ForwardSelection)
* [Bidirectional Elimination](#BidirectionalElimination)
* [Score Comparison](#ScoreComparison)

#### AllIn
* Prior knowledge
* You have to
* Preparing for Backward Elimination

#### BackwardElimination
* Step 1: Select a significance level to stay in the model (SL=0.05)
* Step 2: Fit the full model with all possible predictors
* Step 3: Consider the predictor with the <b>highest</b> P-Value. If P>SL, go to Step 4, otherwise go to END
* Step 4: Remove the predictor
* Step 5: Fit model without this "variable" and go to step 3
* END : Model Ready !

#### ForwardSelection
* Step 1: Select a significance level to enter the model (SL=0.05)
* Step 2: Fit all simple regression models <b>y ~ xn</b>. Select the one with the lowest P-Value
* Step 3: Keep this variaable and fit all possible models with one extra predictor added to the one(s) you already have
* Step 4: Consider the predictor with the <b>lowest</b> P-Value. If P<SL, go to step 3, otherwise go to END 
* END: Keep the previous model !

#### BidirectionalElimination
* Step 1: Select a significance level to enter and to stay in the model (SLENTER=0.05 and SLSTAY=0.05)
* Step 2: Perform the next step of Forward Selection (new variables must have P<SLENTER to enter)
* Step 3: Perform ALL steps of Backward Elimination (old variables must have P<SLSTAY to stay) and go to Step 2
* Step 4: No new variables can enter and no old variables can exit
* END : Model Ready !

#### ScoreComparison
* Step 1: Select a criterion of goodness of fit (Akaike criterion)
* Step 2: Construct all possible regression models 2^(n)-1 total combinations
* Step 3: Select the one with the best criterion
* END : Model Ready !

## :computer: Technologies
MultipleLinearRegression is created with:
* Python 
	
## :cd: Setup
Clone these files anywhere and browse the code.
```batch
$ git clone https://github.com/SimonDuperray/ai_MultipleLinearRegression.git
```
