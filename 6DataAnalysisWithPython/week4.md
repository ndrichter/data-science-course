# Week 4
## Model Development
- Model can be thought as a mathematical equation used to predict a value given one or more other values
- Relates one or more independent variables to dependent variables
- More relevant data will provide more accurate models

## Linear Regression and Multiple Linear Regression
- Linear regression refers to one independent variable to make a prediction
- Multiple will refer to multiple independent variables to make a prediction
- Simple linear regression
    - The predictor variable x
    - The target variable y
    - Intercept and slope
    - Use data points to determine fit, usually stored in numpy arrays. These are used to predict
    
- Fitting a simple linear model
    - import linear_model from scikit-learn
    - create linear regression object using the constructor (LinearRegression)
    - lm.fit(x,y): x is predictor variable, y is target variable. Output is an array
    
- SLR Estimated Linear Model
    - Can view the intercept with lm.intercept
    - Can view the slope with lm.coef
    - Intercept + Slope * predictor = estimate
    
- MLR
    - One continuous target (Y) variable
    - Two or more predictor (X) variables
    
- Fitting a Multiple Linear Model Estimator
    - Extract predictor variables and store them (Z = df[["predictor1", "predictor2"]])
    - Train the model as before (lm.fit(Z, target))
    - Can also obtain a prediction (lm.predict(X))
    
## Model Evaluation Using Visualization
- Why use regression plot? Gives good estimate of:
    - Relationship between two variables
    - Strength of the correlation
    - Direction of the relationship (positive or negative)
    
- Regression plot shows combination of scatterplot and the fitted linear regression line
- Can use regplot from seaborn library
    - sns.regplot(x=predictor, y=target, data=dataframe)
    
- Residual plot represents the error between the actual value. Can help determine if linear regression is appropriate
    - Using seaborn: sns.residplot(feature, target)
    
- Distribution Plot
    - Counts the predicted value versus the actual value
    - Useful for visualizing models with more than one independent variable or feature
    - ax1 = sns.distplot(feature, hist=False, color="r", label="Actual Value")
      sns.distplot(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)

## Polynomial Regression and Pipelines
- Speical case of the geenral linear regression model
- Useful for describing curvilinear relationships
  - Curvilinear relationships: by squaring or setting higher-order terms of the predictor variables
  
- 2nd, third, and higher orders
- polyfit function
- Scikit learn needed for multiple dimensions
  - sklearn.preprocessing import PolynomialFeatures
  - pr=PolynomialFeatures(degree=2, include_bias=False)
  - then use pr.fit_transform([x,y], include_bias=False)
  
- Pipelines
  - Perform series of transformations, then prediction
  
## Measures for In-Sample Evaluation
- Way to numerically determine how good the model fits on a dataset
- Two important measures to determine the fit of a model
  - Mean squared error (MSE)
  - R-squared (R^2)
  
- MSE
  - sklearn.metrics import mean_squared_error
  - mean_squared_error(actual_values, predicted_values)
  
- R^2
  - Coefficient of determination or R Squared
  - Measure to determine how close the data is to the fitted regression line
  - R^2 is the percentage of variation of the target variable (Y) that is explained by the linear model
  - closer to 1: good fit
  - lm.score(x, y)
