# Week 5
## Model Evaluation and Refinement
- Figure out how well the trained model can be used to predict new data
- Can use in sample data or training data, or out of sample evaluation or test data
- Split data set into training and testing (like 70/30%)
    - Build and train model with training set
    - Use testing set to assess the performance of a predictive model
    
- Scikit train_test_split will randomly split the set
- Generalization error: measure of how well our data does at predicting previously unseen data
- Cross validation: most common out of sample evaluation metrics
    - Each partition or fold of data is used for both training and testing
    
- Scikit cross_val_score() for cross validation
- Scikit cross_val_predict() to return predictions that was obtained for each element when it was in the test set

## Overfitting, Underfitting and Model Selection
- Using polynomial regression, increasing/decreasing order to determine fit

## Ridge Regression
- Ridge regression is a regression that is employed in a Multiple regression model when Multicollinearity occurs
- Multicollinearity is when there is a strong relationship among the independent variables
- This helps to prevent overfitting
- Ridge regression controls the magnitude of these polynomial coefficients by introducing the parameter alpha.
- Alpha is a parameter we select before fitting or training the model
    - Can use cross validation to select the most appropriate alpha value
    
- scikit Ridge object takes in alpha parameter

## Grid Search
- Allows us to scan through multiple parameters with few lines of code
- Parameters like the alpha term discussed in the previous video are not part of the fitting or training process
- scikit GridSearchCV
    - provide hyperparameters, model, and number of folds
    - can also provide normalization option (True/False)
    
## Summary
- Identify over-fitting and under-fitting in a predictive model: Overfitting occurs when a function is too closely 
  fit to the training data points and captures the noise of the data. Underfitting refers to a model that can't 
  model the training data or capture the trend of the data.
  
- Apply Ridge Regression to linear regression models: Ridge regression is a regression that is employed in a 
  Multiple regression model when Multicollinearity occurs.
  
- Tune hyper-parameters of an estimator using Grid search: Grid search is a time-efficient tuning technique that 
  exhaustively computes the optimum values of hyperparameters performed on specific parameter values of estimators.