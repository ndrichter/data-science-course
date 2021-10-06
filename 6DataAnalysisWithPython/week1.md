# Importing Datasets
## The Problem and Understanding the Data
- Analysis needed due to: data is everywhere, helps answer questions from data, predicting unknown
- Dataset used for lab: csv of used automobiles
- CSV contains rows, first row can be a header
- Name of value we want to predict: target or label

## Python Packages for Data Science
- Scientific computing libraries
    - Pandas (data structures and tools)
    - NumPy (arrays and matrices)
    - SciPy (integrals, solving differential equations, optimization)
    
- Visualization Libraries:
    - Matplotlib (plots and graphs, most popular)
    - Seaborn (plots like heat maps, time series and violin plots)
    
- Algorithmic Libraries:
    - Scikit-learn (machine learning: regression, classification)
    - Statsmodels (explore data, estimate statistical models, and perform statistical tests)
    
## Importing and Exporting Data in Python
- Importing data two important properties:
    - Format: csv, json, xlsx, hdf
    - File path of dataset
    
- Pandas has read_csv() method
- Print dataframe with df.head() or df.tail()
- Assign columns with df.columns = defined_columns
- df.to_csv(path) to export dataset

## Getting Started Analyzing Data with Python
- Understanding basic insights about data with Pandas methods
    - Check data types: object, int64, float64, datetime64
    - Data type compatibility with python methods
    
- df.dtypes to check data types
- df.describe() returns statistical summary
    - .describe(include="all") to get full summary of all columns
    
- df.info() shows top and bottom 30 rows

## Accessing Databases with Python
- SQL APIs
- DB APIs
    - Connection and query objects (cursor)
    - Connection methods: cursor, commit, rollback, close
    - Cursor methods: execute, fetchall