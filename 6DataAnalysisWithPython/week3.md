# Week 3
## Exploratory Data Analysis
- Preliminary steps:
    - Summarize main characteristics of data
    - Gain better understanding of data
    - Uncover relationships between variables
    - Extract important variables
    
## Descriptive Statistics
- Summarize using df.describe(), NaN values are excluded
- summarize categorical values with value_counts()
- Visualize numeric data with box plots
    - Median, upper quartile, lower quartile, lower/upper extremes, any outliers
    - sns.boxplot(x="x-axis", y="y-axis", data=df)
    
- Scatter plot shows relationship between two variables
    - Predictor/independent variable on x-axis
    - Target/dependent variables on y-axis
    - plt.scatter(x,y)
    
## GroupBy in Python
- Panda has groupby() method to apply to categorical variables
- df.groupby(["column-1", "column-2"], as_index=False).mean()
    - average values grouped by the two columns
    
- Pandas method pivot()
    - One variable displayed along the columns and the other variable displayed along the rows
    - df.pivot(index="column-1", columns="column-2")
    
- Heatmap to plot target variable over multiple variables
    -plt.pcolor(df, cmap="RdBu")
  
## Correlation
- Measures to what extent different variables are interdependent
- Does not imply causation
- Positive linear relationship between engine size and price
- Negative linear relationship between highway mpg and price
- Weak correlation between peak-rpm and price

## Correlation Statistics
- Pearson Correlation
    - Measure the strength of the correlation between two features
    - Returns two values: correlation coefficient (+1 to -1) and p-value (< 0.001 to > 0.1)
    - Correlation coefficient determines large positive (1), large negative (-1) or no relationship (0)
    - P-Value determines certainty in the result
        - Strong: < 0.001
        - Moderate: < 0.05
        - Weak: < 0.1
        - None: > 0.1
    
- scipi stats.pearsonr(column-1, column-2)

## Association Between two categorical variables: chi-square
- Use chi-square test  for association (denoted as x2)
- Intended to test how likely it is that an observed distribution is due to chance
- Tests a null hypothesis that the variables are independent. Does not tell you the type of relationship
- scipy.stats.chi2_contingency(cont_table, correction=True)
    - Return test value, p-value, degree of freedom
    - Prints out expected values in array




    