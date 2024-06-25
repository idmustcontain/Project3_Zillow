# Overview

In this project, we aim to engineer two datasets found on Zillow. One of the files shows the price cut percentage month-to month over several regions across the country. We plan to use the years 2018-2024 to reflect market conditions throughout the pandemic, and a high interest-rate market. Along with showing a trend in price cuts throughout months, we also have data illustrating the heat index in these regions month-to-month. The heat index will tell us the overall strength of the real estate market in the area, with higher numbers showing a sellers market, and lower leaning towards a buyers market. Our plan is to store these datasets into a database using SQL. Our project is designed to show the process of extracting our datasets, and transforming the data by converting file types, allowing for proper loading on our database.

# Instructions

Our data spans from 2018 to 2024. You can select any date from the drop down menu to receive the highest price cut during that time period. You can also select a region, state or city and receive the price cuts for that specific region as well. With our data set you will receive aggregated data and plot points that will allow us to make an educated decision about the market and determine whether it would be a buyers market or a sellers market based on historical data provided by Zillow.

# Ethical Considerations

In creating this data view we were committed to keeping the highest ethical considerations when applying ELT methods to our data set. When aggregating and manipulating real estate data sets there are many things to consider.

1) Race bias
2) Socioeconomic bias
3) Shareholder impact

# Race Bias 
Our data set does not discriminate against any group, culture or religion. Our data is set up to avoid race or any cultural inequalities. It is easy to make predictions based on inequalities as history shows certain regions suffer large price cuts. But there have been advances over time that have benefited certain groups and repaired racial inequalities for some areas. Our data spans 6 years and over 900 unique data points that removes all historical racial biases.

# Socioeconomic Bias
We are also aware of the social impacts of our data as well. Throughout this assignment we worked diligently to avoid contributing to any negative economic disadvantages in areas that suffer from low income households. By providing a wide array of data from different class systems we remove all socioeconomic bias.

# Shareholder Impact
Our data is meant to inform buyers and sellers alike. Our data view derives from a reputable source (“Zillow Inc”) and its sole purpose is to provide historical facts through observed market rates deltas. It is common practice to ensure your data is informative and subjective for all shareholders involved in market transactions.
	
In closing, it is important to keep these ethical principles in mind when aggregating data. All datasets should have a reputable source. By adhering to these principles mentioned we aim to create a data set that is not only useful and informative but also respectful of the individuals and communities it represents. By doing so, our data could be used to make educated decisions for future use.



# Project3_Zillow
# Data Analytics Dashboard

This interactive dashboard explores housing market data, including price cuts. It allows users to visualize trends across various regions over time through interactive charts and map.

## Features

- **Interactive Bar Chart:** Displays price cuts over time for selected regions.
- **Heatmap:** Shows the highest price cuts by state.
- **Metadata Panel:** Displays demographic information and details of the highest price cuts for selected date.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/idmustcontain/Project3_Zillow.git
Navigate to the project directory:


Place your CSV files in the specified directory.

python app_or_pj3.py
Access the application at http://127.0.0.1:5000.
Deployment
The dashboard is deployed on GitHub Pages and can be accessed here.

Data
The dataset is provided by Housing Market Price Cut projects.

License
This project is licensed under the MIT License - see the LICENSE file for details.


### Instructions

1. Ensure that any additional setup steps specific to your project are included.
2. Verify the deployment link once you have deployed your project to GitHub Pages.
3. Ensure that the `LICENSE` file is included in your repository with the correct license details.
