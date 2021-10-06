# Data Wrangling
## Pre-processing data and dealing with missing values
- convert or map raw data into another format (data cleaning or wrangling)
- Missing values can be blank, NaN, or ?
- Able to replace it? Or simply remove it (the entire entry or just the value)?
    - Can replace it with an average of similar data points
    - Replace with the highest frequency
    - Replace with other functions or based on outside knowledge
    - Just leave it
- dataframes.dropna(): can drop entire row or column
    - axis=0 for row, axis=1 for column
    - use inplace=True to modify the dataframe
    
- dataframe.replace(missing, new_value): replace the missing values
    -.replace(np.nan, mean) for example

## Data Formatting
- Able to make meaningful comparisons when data is standardized
- Wrong data type can be assigned to values
- df.astype() to convert data type
- df.rename() to rename columns. Example:
  - df.rename(columns={”city_mpg”: “city-L/100km”}, inplace=True)
  
## Data Normalization
- Uniform the values for a similar value range
- Methods
  - simple feature scaling (feature / feature.max())
  - min max (feature - feature.min() / feature.max() - feature.min())
  - z-score (zed) or standard score (typically -3 to 3)
    - feature - feature.mean() / feature.std()

## Binning in Python
- Grouping values together into "bins"
- Can improve accuracy of predictive models
- Example with price (low, medium, high)
- Can use numpy.linspace(min feature, max feature, number of dividers) to get equidistant values

## Turning Categorical Variables into Quantitative Variables in Python
- Most models can't take objects or strings as input
- Can assign a numerical value to each distinct value in a category (like 0 or 1)
  - Often called one hot encoding
  - pd.get_dummies(feature) automatically generates list of numbers