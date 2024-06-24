# Project3_Zillow
# Data Analytics Dashboard

This interactive dashboard explores housing market data, including price cuts and market heat indices. It allows users to visualize trends across various regions over time through interactive charts and maps.

## Features

- **Interactive Bar Chart:** Displays price cuts over time for selected regions.
- **Heatmap:** Shows the highest price cuts by state.
- **Metadata Panel:** Displays demographic information and details of the highest price cuts for selected columns.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/data-analytics-dashboard.git
Navigate to the project directory:

bash
Copy code
cd data-analytics-dashboard
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare the database:

Place your CSV files in the specified directory.
Run the script to populate the database:
bash
Copy code
python populate_database.py
Run the Flask application:

bash
Copy code
flask run
Access the application at http://127.0.0.1:5000.
Deployment
The dashboard is deployed on GitHub Pages and can be accessed here.

Data
The dataset is provided by Housing Market Data and the Market Heat Index projects.

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Instructions

1. Replace `<your-username>` with your actual GitHub username.
2. Ensure that any additional setup steps specific to your project are included.
3. Verify the deployment link once you have deployed your project to GitHub Pages.
4. Ensure that the `LICENSE` file is included in your repository with the correct license details.
