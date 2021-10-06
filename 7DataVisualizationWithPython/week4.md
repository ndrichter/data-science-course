# Week 4 Dashboards
## Dashboarding Overview
- Creating charts/graphs in one central location with real time visuals
- Can be interactive to drill down into different sections
- Dash from Plotly for web based dashboarding
- Other tools: Panel, Voila, Streamlit
- Dashboard tools: bokeh, ipywidgets, matplotlib, Bowtie, Flask

## Introduction to Plotly
- Interactive open source plotting library, supports over 40 unique chart types
- Sub modules
  - Graph objects: low level interface to figures, traces, and layout
  - Express: high level wrapper
- Express used for quick simple syntax

## Introduction to Dash
- Open source user interface python library from Plotly
- Rendered in web browsers, can be deployed to servers
- Components: core and HTML
- HTML
  - component for every tag
  - keyword args describe HTML attributes
- Core
  - higher level generated through react.js library
  - Examples: creating sliders, input areas, check items, and datepickers

## Make Dashboards Interactive
- Callbacks
  - Python function that is automatically called by Dash whenever an input component's property changes
  - Decorated with @app.callback
  - Provide an output and input for components

