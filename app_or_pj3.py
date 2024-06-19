from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

# Initialize Flask application
# Set up Flask
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

if __name__ == '__main__':
    app.run(debug=True)
