from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import io
import base64
from collections import defaultdict

# Initialize Flask application
app = Flask(__name__, template_folder="", static_url_path='/static')
CORS(app)

# Set up the database connection
engine = create_engine("sqlite:///mydatabase-nojoin.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
PriceCut = Base.classes.PriceCut
MarketHeat = Base.classes.MarketHeat

# Dynamically get the column names for PriceCut and MarketHeat
PriceCut_columns = [column.name for column in PriceCut.__table__.columns if 'RegionID' not in column.name and 'SizeRank' not in column.name and 'RegionName' not in column.name and 'RegionType' not in column.name and 'StateName' not in column.name]
MarketHeat_columns = [column.name for column in MarketHeat.__table__.columns]

# Dictionary of state coordinates using abbreviations
state_coords = {
    'AL': (32.806671, -86.791130),
    'AK': (61.370716, -152.404419),
    'AZ': (33.729759, -111.431221),
    'AR': (34.969704, -92.373123),
    'CA': (36.116203, -119.681564),
    'CO': (39.059811, -105.311104),
    'CT': (41.597782, -72.755371),
    'DE': (39.318523, -75.507141),
    'FL': (27.766279, -81.686783),
    'GA': (33.040619, -83.643074),
    'HI': (21.094318, -157.498337),
    'ID': (44.240459, -114.478828),
    'IL': (40.349457, -88.986137),
    'IN': (39.849426, -86.258278),
    'IA': (42.011539, -93.210526),
    'KS': (38.526600, -96.726486),
    'KY': (37.668140, -84.670067),
    'LA': (31.169546, -91.867805),
    'ME': (44.693947, -69.381927),
    'MD': (39.063946, -76.802101),
    'MA': (42.230171, -71.530106),
    'MI': (43.326618, -84.536095),
    'MN': (45.694454, -93.900192),
    'MS': (32.741646, -89.678696),
    'MO': (38.456085, -92.288368),
    'MT': (46.921925, -110.454353),
    'NE': (41.125370, -98.268082),
    'NV': (38.313515, -117.055374),
    'NH': (43.452492, -71.563896),
    'NJ': (40.298904, -74.521011),
    'NM': (34.840515, -106.248482),
    'NY': (42.165726, -74.948051),
    'NC': (35.630066, -79.806419),
    'ND': (47.528912, -99.784012),
    'OH': (40.388783, -82.764915),
    'OK': (35.565342, -96.928917),
    'OR': (44.572021, -122.070938),
    'PA': (40.590752, -77.209755),
    'RI': (41.680893, -71.511780),
    'SC': (33.856892, -80.945007),
    'SD': (44.299782, -99.438828),
    'TN': (35.747845, -86.692345),
    'TX': (31.054487, -97.563461),
    'UT': (40.150032, -111.862434),
    'VT': (44.045876, -72.710686),
    'VA': (37.769337, -78.169968),
    'WA': (47.400902, -121.490494),
    'WV': (38.491226, -80.954456),
    'WI': (44.268543, -89.616508),
    'WY': (42.755966, -107.302490)
}

# Define color mapping based on highest price cut ranges
def get_color(value):
    if 1 <= value < 4:
        return 'yellow'
    elif 4 <= value < 7:
        return 'orange'
    elif 7 <= value < 10:
        return 'orangered'
    elif 10 <= value < 13:
        return 'red'
    elif 13 <= value < 16:
        return 'darkred'
    else:
        return 'gray'

#################################################
# Flask Routes
#################################################

@app.route("/help")
def welcome():
    """List all available API routes."""
    return (
        "Available Routes:<br/>"
        "/api/pricecut/<column_name><br/>"
        "/api/allcolumns<br/>"
        "/api/regionnames<br/>"
        "/api/plot/<region_name><br/>"
        "/api/map/<marker><br/>"
        "/api/store_highest_pricecut_geojson<br/>"
        "/api/heatmap<br/>"
    )

@app.route("/")
def index():
    """Render the home page"""
    return render_template('template.html')

@app.route("/api/pricecut/<column_name>")
def by_column(column_name):
    """Search by column name for highest price cut"""
    session = Session(engine)
    # Get the maximum value for the specified column
    most_highest_pricecut = session.query(func.max(getattr(PriceCut, column_name))).scalar()

    # Retrieve the row where the highest value is found
    row_with_highest_pricecut = session.query(PriceCut).filter(getattr(PriceCut, column_name) == most_highest_pricecut).first()

    # Extract and format the desired columns
    if row_with_highest_pricecut:
        result = {
            "message": f"The highest price cut (%) in {column_name}: {most_highest_pricecut}",
            "RegionName": row_with_highest_pricecut.RegionName,
            "StateName": row_with_highest_pricecut.StateName
        }
    else:
        result = {"message": f"No data found for column {column_name}"}

    session.close()
    return jsonify(result)

@app.route("/api/allcolumns")
def all_columns():
    """List of all column names for PriceCut"""
    return jsonify(PriceCut_columns)

@app.route("/api/regionnames")
def region_names():
    """Get unique RegionName values"""
    session = Session(engine)
    region_names = session.query(PriceCut.RegionName).distinct().all()
    session.close()
    return jsonify([name[0] for name in region_names])

@app.route("/api/plot/<region_name>")
def plot(region_name):
    """Plot data for the selected region"""
    session = Session(engine)
    data = session.query(PriceCut).filter(PriceCut.RegionName == region_name).all()
    session.close()

    # Convert data to DataFrame
    data_dict = {column: [getattr(d, column) for d in data] for column in PriceCut_columns}
    df = pd.DataFrame(data_dict)

    # Plotting
    img = io.BytesIO()
    ax = df.T.plot(kind='bar', color='skyblue', figsize=(11, 6))  # Transpose the DataFrame to get the months on the x-axis
    ax.legend().remove()  # Remove the legend

    # Only show x-axis labels for specific months
    x_labels = [label if any(m in label for m in ['Mar', 'Jun', 'Sept', 'Dec']) else '' for label in df.columns]
    ax.set_xticklabels(x_labels, rotation=45, ha='right')

    plt.title(f'Price Cut(%) in {region_name}')
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return jsonify({'plot_url': plot_url})

@app.route("/api/store_highest_pricecut_geojson")
def store_highest_pricecut_geojson():
    """Store highest price cut and state information for all columns into GeoJSON"""
    session = Session(engine)
    results = []

    for column in PriceCut_columns:
        # Get the maximum value for the specified column
        most_highest_pricecut = session.query(func.max(getattr(PriceCut, column))).scalar()

        # Retrieve the row where the highest value is found
        row_with_highest_pricecut = session.query(PriceCut).filter(getattr(PriceCut, column) == most_highest_pricecut).first()

        # Extract and format the desired columns
        if row_with_highest_pricecut:
            state_abbr = row_with_highest_pricecut.StateName
            if state_abbr in state_coords:
                latitude, longitude = state_coords[state_abbr]
                geometry = Point(longitude, latitude)
                result = {
                    "ColumnName": column,
                    "HighestPriceCut": most_highest_pricecut,
                    "RegionName": row_with_highest_pricecut.RegionName,
                    "StateName": row_with_highest_pricecut.StateName,
                    "geometry": geometry
                }
                results.append(result)

    session.close()

    # Convert the results to a GeoDataFrame
    gdf = gpd.GeoDataFrame(results)

    # Set the coordinate reference system (CRS) to WGS84 (EPSG:4326)
    gdf.set_crs(epsg=4326, inplace=True)

    # Convert the GeoDataFrame to GeoJSON
    geojson = gdf.to_json()

    return jsonify(geojson)

@app.route("/api/heatmap")
def heatmap():
    """Create a heatmap of the count of highest price cuts by state"""
    session = Session(engine)
    state_count = defaultdict(int)

    for column in PriceCut_columns:
        # Get the maximum value for the specified column
        most_highest_pricecut = session.query(func.max(getattr(PriceCut, column))).scalar()

        # Retrieve the row where the highest value is found
        row_with_highest_pricecut = session.query(PriceCut).filter(getattr(PriceCut, column) == most_highest_pricecut).first()

        # Increment the count for the state
        if row_with_highest_pricecut:
            state_abbr = row_with_highest_pricecut.StateName
            state_count[state_abbr] += 1

    session.close()

    heat_data = []

    # Prepare data for heatmap
    for state_abbr, count in state_count.items():
        if state_abbr in state_coords:
            latitude, longitude = state_coords[state_abbr]
            heat_data.append([latitude, longitude, count])

    # Create a map centered on the US
    m = folium.Map(location=[37.0902, -95.7129], zoom_start=5)

    # Add the heatmap
    HeatMap(heat_data).add_to(m)

    # Add CircleMarkers with tooltips and popups
    for data in heat_data:
        color = get_color(data[2])
        folium.CircleMarker(
            location=[data[0], data[1]],
            radius=10,
            color=color,
            weight=1,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
            popup=folium.Popup(f"Number of Highest Price Cuts: {data[2]}", parse_html=True),
            tooltip=f"Number of Highest Price Cuts: {data[2]}"
        ).add_to(m)

    # Add a legend to the map
    legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; right: 50px; width: 100px; height: 140px; 
                 border:2px solid grey; z-index:9999; font-size:10px;
                 background-color:white; opacity: 0.8;
                 padding: 10px;
                 ">
                 &nbsp;<b>&nbsp;Number of Highest Price Cuts</b> <br>
                 &nbsp;<i style="background:yellow; width: 10px; height: 10px; display: inline-block;"></i> 1 - 3<br>
                 &nbsp;<i style="background:orange; width: 10px; height: 10px; display: inline-block;"></i> 4 - 6<br>
                 &nbsp;<i style="background:orangered; width: 10px; height: 10px; display: inline-block;"></i> 7 - 9<br>
                 &nbsp;<i style="background:red; width: 10px; height: 10px; display: inline-block;"></i> 10 - 12<br>
                 &nbsp;<i style="background:darkred; width: 10px; height: 10px; display: inline-block;"></i> 13 - 15<br>
     </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))

    # Save the map to an HTML file
    heatmap_path = "static/heatmap.html"
    m.save(heatmap_path)

    return jsonify({"heatmap_path": heatmap_path})


if __name__ == '__main__':
    app.run(debug=True)

