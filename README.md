# Project3_Zillow
APIs
The following API routes are available:

/api/pricecut/<column_name>: Get the highest price cut and corresponding region name for the specified column.
/api/allcolumns: Get a list of all column names in the PriceCut table.
/api/regionnames: Get a list of all unique region names.
/api/plot/<region_name>: Get a plot of price cuts over time for the specified region.
/api/store_highest_pricecut_geojson: Get GeoJSON data of the highest price cuts by state.
/api/heatmap: Get the path to the heatmap HTML file.
static/: Contains static files like JavaScript and CSS.
templates/: Contains HTML templates.

File Structure
mydatabase-nojoin.sqlite: The SQLite database file.
populate_database.py: Script to populate the database with CSV data.
app.py: The main Flask application file.
requirements.txt: List of Python dependencies.
README.md: This README file.

Technologies Used
Flask: A micro web framework for Python.
SQLite: A C-language library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
Pandas: A data manipulation and analysis library for Python.
D3.js: A JavaScript library for producing dynamic, interactive data visualizations in web browsers.
Matplotlib: A plotting library for Python and its numerical mathematics extension NumPy.
Folium: A Python library used for visualizing geospatial data.
