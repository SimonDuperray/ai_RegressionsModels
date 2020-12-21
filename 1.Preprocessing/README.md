# Data Preprocessing

[-> Repository](https://github.com/SimonDuperray/ai_DataPreprocessing)

## :clipboard: Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## :page_facing_up: General info
Data preprocessing algorithm for machine learning models.
Add notes about used functions.

### Regressions
Simple Linear Regression: ```y = b0 + b1x1```<br><br>
Multiple Linear Regression: ```y = b0 + b1x1 + b2x2 + ... + bnxn```<br><br>
Polynomial Linear Regression: ```y = b0 + b1x1 + b2x1^2 + ... + bnx1^n```<br><br>

### Feature Scaling
Standardisation: ``` xstand = (x-mean(x))/(standard deviation(x))```<br>
[-3;+3] ; recommended when you have a normal distribution in most of your features<br><br>

Normalisation: ```xnorm = (x-min(x))/(max(x)-min(x))```<br>
[0;1] ; do the job all the time<br><br>

Always scale X_train data.<br>
<b>Do we have to apply feature scaling (standardization) to the dummy variables in the matrix of features ?</b><br>
<p>-> No because standardization set all the values of the features in the same range.</p>


## :computer: Technologies
DataProcessing is created with:
* Python (sklearn)
* Google Colab
	
## :cd: Setup
Clone these files anywhere and browse the code.
```batch
$ git clone https://github.com/SimonDuperray/ai_DataPreprocessing.git
```
