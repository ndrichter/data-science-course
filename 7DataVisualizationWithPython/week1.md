# Week 1
## Introduction to Data Visualization
- Why build visuals?
  - Exploratory analysis
  - Communicate data clearly
  - Share unbiased representation
  - Support recommendations
- Best Practices
  - Less is more effective, attractive and impactive

## Introduction to Matplotlib
- History
  - Authored by John Hunter
- Architecture
  - Artist layer, backend layer, scripting layer
  - Backend: FigureCanvas, Renderer, Event
  - Artist: one main object, Artist. Knows how to use Renderer to draw on Canvas.
    - Two types: Primitive, Composite
  - Scripting: mainly pyplot for quick plotting

## Basic Plotting with Matplotlib
- Plot function: import matplotlib.pyplot as plt
  - plt.plot(5, 5, 'o')
  - plt.show()
- Pandas
  - dataframe.plot(kind="line")
  - Other examples to use for the kind parameter:
    - bar for vertical bar plots 
    - barh for horizontal bar plots 
    - hist for histogram 
    - box for boxplot 
    - kde or density for density plots 
    - area for area plots 
    - pie for pie plots 
    - scatter for scatter plots 
    - hexbin for hexbin plot

## Line Plots
- Type of plot which displays information as a series of data points called markers connected by straight line segments
- Use dataframe.plot(kind="line")
- Can set plt.title/ylabel/xlabel then use plt.show() to display

