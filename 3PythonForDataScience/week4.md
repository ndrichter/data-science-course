# Week 4
## Reading and Writing Files with Open
- Using open to get File object
- params file path and mode
- use with statement so file always closes
- .readline() to read each line of File object (or use for line in file)

## Writing Files with Open
- Using open to create File, and write to it
- Mode w for writing
- Using method .write()
- Mode a for appending to existing file

## Pandas
- Python library for data analysis
- read_csv() to load from csv
- standard to use as pd
- Dataframes
    - read_csv() returns dataframe
    - use .head() to see first five rows
    - can create DFs from dictionaries
    
- .unique() to find unique elements in DF
- .to_csv() for saving DF as csv

- Pandas Notebook in Watson Studio
    - https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/8e73cc54-bb07-48fa-9ea8-542de5c6433d/view?access_token=74987043a97e7f15a3ef3f8357c41084b788197e706e274dd69a80dcece4ca05
  
## Numpy in Python
- One dimensional
  - Library for scientific computing
  - numpy array is list with same type of element
  - can use array index for changing values or slicing
  - vector addition and subtraction
  - array multiplication with a scalar
  - product of two numpy arrays
  - dot product, represents how similar two vectors are
  - can add a constant element to each array element (broadcasting)
  - universal functions on arrays (mean, max, sin, linspace to generate array of evenly spaced numbers)
  
- Two dimensional
  - ndim: think of it as how many nested lists
  - shape: number of rows and columns as a tuple
  - adding arrays for matrix addition
  - use dot for matrix multiplication