# Linear Regression
## Introduction to Regression
- Process of predicting a continuous value
- Two types of variables: Y - dependent, X - independent
- Dependent value should be continuous, independent can be measured
- Types of regression models:
  - Simple regression: one independent var is used to estimate dependent var. Can be linear or non-linear
  - Multiple regression: more than one independent var. Can also be linear or non-linear
- Can be used for sales forecasting, satisfaction analysis, price estimation, employment income

## Simple Linear Regression
- Pros
  - Fast and basic
  - No parameter tuning
  - Easy to understand, highly interpretable

## Model Evaluation in Regression Models
- Model evaluation approaches
  - Train and test on the same dataset
    - Simplest approach
    - Train model on entire dataset, then test it using a portion of same dataset
    - High training accuracy and low out of sample accuracy
      - Training accuracy: percentage of correct predictions model makes when using the test dataset
      - Out of sample accuracy: percentage of correct predictions the model makes on data the model has not been trained on
      - Important to have high out of sample accuracy
  - Train / Test split
    - Splitting dataset into training and testing sets respectively which are mutually exclusive
    - After which you train with the training set and test with the testing set
    - More accurate out of sample accuracy
- K-fold cross validation
  - Split up datasets into k number of folds
  - Results of these evaluations are averaged
  - Performs multiple train/test splits

## Evaluation Metrics in Regression Models
- Helps to explain performance of the model
- Error: measure of how far the data is from the fitted regression line
- Mean Absolute Error: It is the mean of the absolute value of the errors. 
  - This is the easiest of the metrics to understand since it’s just average error.
- Mean Squared Error (MSE): (MSE) is the mean of the squared error. 
  - It’s more popular than Mean Absolute Error because the focus is geared more towards large errors. 
  - This is due to the squared term exponentially increasing larger errors in comparison to smaller ones.
- Root Mean Squared Error (RMSE)
- R-squared is not an error, but rather a popular metric to measure the performance of your regression model. 
  - It represents how close the data points are to the fitted regression line. 
  - The higher the R-squared value, the better the model fits your data. 
  - The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).

## Multiple Linear Regression
- Determine independent variable effectiveness on prediction
- Predict impact of changes
- Estimating multiple linear regression parameters
  - Ordinary least squares - linear algebra operations, can take a long time
  - Optimization algorithm: gradient descent, good for large dataset

## Non-Linear Regression
- Different types, called polynomial regressions. This includes quadratic, cubic, exponential, and logarithmic
- Fits a curved line to your data
- Can be transformed into linear regression model
- 