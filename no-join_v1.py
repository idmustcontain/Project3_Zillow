import sqlite3
import pandas as pd

# Define the path to your CSV files
csv_price_cut_path = r'C:\Users\Sarah Son Kim\class24\NU-VIRT-DATA-PT-02-2024-U-LOLC\02-Homework\Project3_Team5\cleaned_Project3_Price_Listings_or_cleaned.csv'
csv_market_heat_path = r'C:\Users\Sarah Son Kim\class24\NU-VIRT-DATA-PT-02-2024-U-LOLC\02-Homework\Project3_Team5\cleaned_Market Temp Index_or.csv'

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase-nojoin.sqlite', timeout=10)
c = conn.cursor()

# Create the price_cut table manually
c.execute('''
    CREATE TABLE IF NOT EXISTS PriceCut (
        RegionID INTEGER NOT NULL PRIMARY KEY,
        SizeRank INTEGER NOT NULL,
        RegionName TEXT NOT NULL,
        RegionType TEXT NOT NULL,
        StateName TEXT NOT NULL,
        Mar_2018 FLOAT NOT NULL,
        Apr_2018 FLOAT NOT NULL,
        May_2018 FLOAT NOT NULL,
        Jun_2018 FLOAT NOT NULL,
        Jul_2018 FLOAT NOT NULL,
        Aug_2018 FLOAT NOT NULL,
        Sept_2018 FLOAT NOT NULL,
        Oct_2018 FLOAT NOT NULL,
        Nov_2018 FLOAT NOT NULL,
        Dec_2018 FLOAT NOT NULL,
        Jan_2019 FLOAT NOT NULL,
        Feb_2019 FLOAT NOT NULL,
        Mar_2019 FLOAT NOT NULL,
        Apr_2019 FLOAT NOT NULL,
        May_2019 FLOAT NOT NULL,
        Jun_2019 FLOAT NOT NULL,
        Jul_2019 FLOAT NOT NULL,
        Aug_2019 FLOAT NOT NULL,
        Sept_2019 FLOAT NOT NULL,
        Oct_2019 FLOAT NOT NULL,
        Nov_2019 FLOAT NOT NULL,
        Dec_2019 FLOAT NOT NULL,
        Jan_2020 FLOAT NOT NULL,
        Feb_2020 FLOAT NOT NULL,
        Mar_2020 FLOAT NOT NULL,
        Apr_2020 FLOAT NOT NULL,
        May_2020 FLOAT NOT NULL,
        Jun_2020 FLOAT NOT NULL,
        Jul_2020 FLOAT NOT NULL,
        Aug_2020 FLOAT NOT NULL,
        Sept_2020 FLOAT NOT NULL,
        Oct_2020 FLOAT NOT NULL,
        Nov_2020 FLOAT NOT NULL,
        Dec_2020 FLOAT NOT NULL,
        Jan_2021 FLOAT NOT NULL,
        Feb_2021 FLOAT NOT NULL,
        Mar_2021 FLOAT NOT NULL,
        Apr_2021 FLOAT NOT NULL,
        May_2021 FLOAT NOT NULL,
        Jun_2021 FLOAT NOT NULL,
        Jul_2021 FLOAT NOT NULL,
        Aug_2021 FLOAT NOT NULL,
        Sept_2021 FLOAT NOT NULL,
        Oct_2021 FLOAT NOT NULL,
        Nov_2021 FLOAT NOT NULL,
        Dec_2021 FLOAT NOT NULL,
        Jan_2022 FLOAT NOT NULL,
        Feb_2022 FLOAT NOT NULL,
        Mar_2022 FLOAT NOT NULL,
        Apr_2022 FLOAT NOT NULL,
        May_2022 FLOAT NOT NULL,
        Jun_2022 FLOAT NOT NULL,
        Jul_2022 FLOAT NOT NULL,
        Aug_2022 FLOAT NOT NULL,
        Sept_2022 FLOAT NOT NULL,
        Oct_2022 FLOAT NOT NULL,
        Nov_2022 FLOAT NOT NULL,
        Dec_2022 FLOAT NOT NULL,
        Jan_2023 FLOAT NOT NULL,
        Feb_2023 FLOAT NOT NULL,
        Mar_2023 FLOAT NOT NULL,
        Apr_2023 FLOAT NOT NULL,
        May_2023 FLOAT NOT NULL,
        Jun_2023 FLOAT NOT NULL,
        Jul_2023 FLOAT NOT NULL,
        Aug_2023 FLOAT NOT NULL,
        Sept_2023 FLOAT NOT NULL,
        Oct_2023 FLOAT NOT NULL,
        Nov_2023 FLOAT NOT NULL,
        Dec_2023 FLOAT NOT NULL,
        Jan_2024 FLOAT NOT NULL,
        Feb_2024 FLOAT NOT NULL,
        Mar_2024 FLOAT NOT NULL,
        Apr_2024 FLOAT NOT NULL,
        May_2024 FLOAT NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Read the price_cut CSV file into a pandas DataFrame
df_price_cut = pd.read_csv(csv_price_cut_path)

# Ensure correct data types (if necessary)
df_price_cut['RegionID'] = pd.to_numeric(df_price_cut['RegionID'], errors='coerce', downcast='integer')
df_price_cut['SizeRank'] = pd.to_numeric(df_price_cut['SizeRank'], errors='coerce', downcast='integer')
df_price_cut['RegionName'] = df_price_cut['RegionName'].astype(str)
df_price_cut['RegionType'] = df_price_cut['RegionType'].astype(str)
df_price_cut['StateName'] = df_price_cut['StateName'].astype(str)

# List of all month columns for price_cut
price_cut_month_columns = [
    'Mar_2018', 'Apr_2018', 'May_2018', 'Jun_2018', 'Jul_2018', 'Aug_2018', 
    'Sept_2018', 'Oct_2018', 'Nov_2018', 'Dec_2018', 'Jan_2019', 'Feb_2019', 
    'Mar_2019', 'Apr_2019', 'May_2019', 'Jun_2019', 'Jul_2019', 'Aug_2019', 
    'Sept_2019', 'Oct_2019', 'Nov_2019', 'Dec_2019', 'Jan_2020', 'Feb_2020', 
    'Mar_2020', 'Apr_2020', 'May_2020', 'Jun_2020', 'Jul_2020', 'Aug_2020', 
    'Sept_2020', 'Oct_2020', 'Nov_2020', 'Dec_2020', 'Jan_2021', 'Feb_2021', 
    'Mar_2021', 'Apr_2021', 'May_2021', 'Jun_2021', 'Jul_2021', 'Aug_2021', 
    'Sept_2021', 'Oct_2021', 'Nov_2021', 'Dec_2021', 'Jan_2022', 'Feb_2022', 
    'Mar_2022', 'Apr_2022', 'May_2022', 'Jun_2022', 'Jul_2022', 'Aug_2022', 
    'Sept_2022', 'Oct_2022', 'Nov_2022', 'Dec_2022', 'Jan_2023', 'Feb_2023', 
    'Mar_2023', 'Apr_2023', 'May_2023', 'Jun_2023', 'Jul_2023', 'Aug_2023', 
    'Sept_2023', 'Oct_2023', 'Nov_2023', 'Dec_2023', 'Jan_2024', 'Feb_2024', 
    'Mar_2024', 'Apr_2024', 'May_2024'
]

# Convert month columns to float for price_cut
df_price_cut[price_cut_month_columns] = df_price_cut[price_cut_month_columns].apply(pd.to_numeric, errors='coerce')

# Remove duplicates based on RegionID
df_price_cut.drop_duplicates(subset=['RegionID'], inplace=True)

# Insert the data into the price_cut table
df_price_cut.to_sql('PriceCut', conn, if_exists='append', index=False)  # Use 'append' to add data to the table without replacing it

# Verify the data in price_cut table
for row in c.execute('SELECT * FROM PriceCut LIMIT 5'):
    print(row)

# Create the market_heat table manually
c.execute('''
    CREATE TABLE IF NOT EXISTS MarketHeat (
        RegionID INTEGER NOT NULL PRIMARY KEY,
        Mar_2018_TempIndex INTEGER NOT NULL,
        Apr_2018_TempIndex INTEGER NOT NULL,
        May_2018_TempIndex INTEGER NOT NULL,
        Jun_2018_TempIndex INTEGER NOT NULL,
        Jul_2018_TempIndex INTEGER NOT NULL,
        Aug_2018_TempIndex INTEGER NOT NULL,
        Sept_2018_TempIndex INTEGER NOT NULL,
        Oct_2018_TempIndex INTEGER NOT NULL,
        Nov_2018_TempIndex INTEGER NOT NULL,
        Dec_2018_TempIndex INTEGER NOT NULL,
        Jan_2019_TempIndex INTEGER NOT NULL,
        Feb_2019_TempIndex INTEGER NOT NULL,
        Mar_2019_TempIndex INTEGER NOT NULL,
        Apr_2019_TempIndex INTEGER NOT NULL,
        May_2019_TempIndex INTEGER NOT NULL,
        Jun_2019_TempIndex INTEGER NOT NULL,
        Jul_2019_TempIndex INTEGER NOT NULL,
        Aug_2019_TempIndex INTEGER NOT NULL,
        Sept_2019_TempIndex INTEGER NOT NULL,
        Oct_2019_TempIndex INTEGER NOT NULL,
        Nov_2019_TempIndex INTEGER NOT NULL,
        Dec_2019_TempIndex INTEGER NOT NULL,
        Jan_2020_TempIndex INTEGER NOT NULL,
        Feb_2020_TempIndex INTEGER NOT NULL,
        Mar_2020_TempIndex INTEGER NOT NULL,
        Apr_2020_TempIndex INTEGER NOT NULL,
        May_2020_TempIndex INTEGER NOT NULL,
        Jun_2020_TempIndex INTEGER NOT NULL,
        Jul_2020_TempIndex INTEGER NOT NULL,
        Aug_2020_TempIndex INTEGER NOT NULL,
        Sept_2020_TempIndex INTEGER NOT NULL,
        Oct_2020_TempIndex INTEGER NOT NULL,
        Nov_2020_TempIndex INTEGER NOT NULL,
        Dec_2020_TempIndex INTEGER NOT NULL,
        Jan_2021_TempIndex INTEGER NOT NULL,
        Feb_2021_TempIndex INTEGER NOT NULL,
        Mar_2021_TempIndex INTEGER NOT NULL,
        Apr_2021_TempIndex INTEGER NOT NULL,
        May_2021_TempIndex INTEGER NOT NULL,
        Jun_2021_TempIndex INTEGER NOT NULL,
        Jul_2021_TempIndex INTEGER NOT NULL,
        Aug_2021_TempIndex INTEGER NOT NULL,
        Sept_2021_TempIndex INTEGER NOT NULL,
        Oct_2021_TempIndex INTEGER NOT NULL,
        Nov_2021_TempIndex INTEGER NOT NULL,
        Dec_2021_TempIndex INTEGER NOT NULL,
        Jan_2022_TempIndex INTEGER NOT NULL,
        Feb_2022_TempIndex INTEGER NOT NULL,
        Mar_2022_TempIndex INTEGER NOT NULL,
        Apr_2022_TempIndex INTEGER NOT NULL,
        May_2022_TempIndex INTEGER NOT NULL,
        Jun_2022_TempIndex INTEGER NOT NULL,
        Jul_2022_TempIndex INTEGER NOT NULL,
        Aug_2022_TempIndex INTEGER NOT NULL,
        Sept_2022_TempIndex INTEGER NOT NULL,
        Oct_2022_TempIndex INTEGER NOT NULL,
        Nov_2022_TempIndex INTEGER NOT NULL,
        Dec_2022_TempIndex INTEGER NOT NULL,
        Jan_2023_TempIndex INTEGER NOT NULL,
        Feb_2023_TempIndex INTEGER NOT NULL,
        Mar_2023_TempIndex INTEGER NOT NULL,
        Apr_2023_TempIndex INTEGER NOT NULL,
        May_2023_TempIndex INTEGER NOT NULL,
        Jun_2023_TempIndex INTEGER NOT NULL,
        Jul_2023_TempIndex INTEGER NOT NULL,
        Aug_2023_TempIndex INTEGER NOT NULL,
        Sept_2023_TempIndex INTEGER NOT NULL,
        Oct_2023_TempIndex INTEGER NOT NULL,
        Nov_2023_TempIndex INTEGER NOT NULL,
        Dec_2023_TempIndex INTEGER NOT NULL,
        Jan_2024_TempIndex INTEGER NOT NULL,
        Feb_2024_TempIndex INTEGER NOT NULL,
        Mar_2024_TempIndex INTEGER NOT NULL,
        Apr_2024_TempIndex INTEGER NOT NULL,
        May_2024_TempIndex INTEGER NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Read the market_heat CSV file into a pandas DataFrame
df_market_heat = pd.read_csv(csv_market_heat_path)

# Ensure correct data types for market_heat (if necessary)
df_market_heat['RegionID'] = pd.to_numeric(df_market_heat['RegionID'], errors='coerce', downcast='integer')
for col in df_market_heat.columns:
    if 'TempIndex' in col:
        df_market_heat[col] = pd.to_numeric(df_market_heat[col], errors='coerce', downcast='integer')

# Insert the data into the market_heat table
df_market_heat.to_sql('MarketHeat', conn, if_exists='append', index=False)  # Use 'append' to add data to the table without replacing it

# Verify the data in market_heat table
for row in c.execute('SELECT * FROM MarketHeat LIMIT 5'):
    print(row)

# Close the connection
conn.close()
