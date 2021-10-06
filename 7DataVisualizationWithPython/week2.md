# Week 2
## Area Plots
- Area chart or graph
- Commonly used to represent cumulated totals using numbers or percentages over time
- Based on line plot
- Generating area plots
  - Using matplotlib
  - df.plot(kind='area')
  - plt title, ylabel, xlabel, and show()

## Histograms
- Way of representing the frequency distribution of a variable
- Generating histograms
  - Using matplotlib
  - df.plot(kind='hist')
  - Then plt title, ylabel, xlabel and show()
  - Use numpy to evenly distribute histogram data bins
    - np.histogram(df)
    - then in df.plot(), use param xticks = num_bins

## Bar Charts
- Commonly used to compare the values of a variable at a given point in time
- Generating using matplotlib
  - df.plot(kind='bar')
  - plt title, ylabel, xlabel, and then show()

## Pie Charts
- Circular statistical graphic divided into slices to illustrate numerical proportion
- Use pandas groupby function
- Generating using matplotlib
  - df.plot(kind='pie')
  - plt title and show
- Arguments of pie chart flaws, people seem to think bar charts are better representations

## Box Plots
- Way to statistically represent distribution of given data through five dimensions
  - Minimum: smallest number of sorted data
  - First Quartile: 25% of the way through the sorted data
  - Median: median of the sorted data
  - Third Quartile: 75% of the way through the sorted data
  - Maximum: highest number of the sorted data
  - Also display outliers that fall outside upper and lower extremes
- Generating using matplotlib
  - df.plot(kind='box')
  - plt title, ylabel, show

## Scatter Plots
- Type of plot that displays values pertaining to typically two variables against each other
- Usually it is a dependent variable plotted against an independent variable to determine if any correlation between the two exist
- Generating with matplotlib
  - df.plot(kind='scatter', x='x_var', y='y_var')
  - plt title, xlabel, ylabel, then show
