# Week 3 Advanced Visualization Tools
## Waffle Chart
- Normally created to display progress towards goals
- Displayed with a number of tiles
- Not built in with matplotlib

## Word Clouds
- Depiction of the frequency of different words in some textual data
- Not built in with matplotlib

## Seaborn and Regression Plots
- Visualization library based on matplotlib
- Very efficient, able to produce plots with less code
- Regression plots
  - import seaborn as sns
  - Example: sns.regplot(x='year', y='total', data=data_frame)

## Introduction to Folium
- Helps create several types of Leaflet maps
- Enables both the binding of data to a map for choropleth visualizations, and passing visualizations as markers on the map
- Built in tile sets
- Creating a world map
  - folium.Map()
  - folium.map(location=[lat, long]), zoom_start=int) ## canada
  - use tiles parameter for different styles

## Maps with Markers
- Adding a marker
  - Need to create a feature group: folium.map.FeatureGroup()
  - Then create and add child: f_group.add_child([lat, long], radius=int, color="color", fill_color="fill_color")
  - map.add_child(f_group)
  - Can label marker with folium.Marker

## Choropleth Maps
- Areas are shaded or patterned in proportion to the measurement of the statistical variable being displayed on the map
- For example, population density or per capita income
- Higher measurement means a darker color
- Requires Geojson file
- Creating the map
  - Start with folium.Map()
  - map.choropleth(geo_path=geojson_file, data=data_frame, columns=["c1", "c2"], key_on="property", fill_color="color", legend_name="name")
  -  