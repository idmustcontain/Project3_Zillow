import csv

# Define input and output file paths for cleaning
input_file_clean = r'C:\Users\Sarah Son Kim\Downloads\Project 3\Project3_Price_Listings_or.csv'
output_file_clean = r'C:\Users\Sarah Son Kim\Downloads\Project 3\cleaned_Project3_Price_Listings_or.csv'

# Define input file path for processing RegionName
input_file_process = r'C:\Users\Sarah Son Kim\Downloads\Project 3\cleaned_Project3_Price_Listings_or.csv'

# List of columns to replace NULL values with '0' in the '20xx' format
columns_to_replace = [
    'Mar_2018', 'Apr_2018', 'May_2018', 'Jun_2018', 'Jul_2018', 'Aug_2018', 'Sept_2018', 'Oct_2018', 'Nov_2018', 'Dec_2018', 
    'Jan_2019', 'Feb_2019', 'Mar_2019', 'Apr_2019', 'May_2019', 'Jun_2019', 'Jul_2019', 'Aug_2019', 'Sept_2019', 'Oct_2019', 'Nov_2019', 'Dec_2019', 
    'Jan_2020', 'Feb_2020', 'Mar_2020', 'Apr_2020', 'May_2020', 'Jun_2020', 'Jul_2020', 'Aug_2020', 'Sept_2020', 'Oct_2020', 'Nov_2020', 'Dec_2020', 
    'Jan_2021', 'Feb_2021', 'Mar_2021', 'Apr_2021', 'May_2021', 'Jun_2021', 'Jul_2021', 'Aug_2021', 'Sept_2021', 'Oct_2021', 'Nov_2021', 'Dec_2021', 
    'Jan_2022', 'Feb_2022', 'Mar_2022', 'Apr_2022', 'May_2022', 'Jun_2022', 'Jul_2022', 'Aug_2022', 'Sept_2022', 'Oct_2022', 'Nov_2022', 'Dec_2022', 
    'Jan_2023', 'Feb_2023', 'Mar_2023', 'Apr_2023', 'May_2023', 'Jun_2023', 'Jul_2023', 'Aug_2023', 'Sept_2023', 'Oct_2023', 'Nov_2023', 'Dec_2023', 
    'Jan_2024', 'Feb_2024', 'Mar_2024', 'Apr_2024', 'May_2024'
]

# Function to clean CSV by replacing NULL values with '0' in specified columns
def clean_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        # Write the header to the output file
        writer.writeheader()
        
        for row in reader:
            # Replace NULL or empty values with '0' in specified columns
            for key in columns_to_replace:
                if key in row and (row[key] is None or row[key].strip() == ''):
                    row[key] = '0'
            
            # Write the processed row to the output file
            writer.writerow(row)
    
    print(f"NULL or empty values in specified columns have been converted to '0' in {output_file}.")

# Function to process RegionName column and validate as varchar(30) NOT NULL
def process_region_names(input_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header if exists
        
        for row in reader:
            if len(row) < 1:
                continue  # Skip empty rows
            
            region_name = row[0].strip()  # Assuming RegionName is the first column
            
            # Validate RegionName (varchar(30) NOT NULL equivalent)
            if region_name is None or len(region_name) == 0:
                print(f"Skipping empty RegionName in row: {row}")
                continue
            
            if len(region_name) > 30:
                print(f"Truncating RegionName '{region_name}' to 30 characters.")
                region_name = region_name[:30]  # Truncate to 30 characters
            
            # Process or store region_name as needed
            print(f"Processing RegionName: {region_name}")
            # Your processing logic here

    print("Processing complete.")

# Example usage:
# Clean the initial CSV file
clean_csv(input_file_clean, output_file_clean)

# Process the cleaned CSV file for RegionName validation
process_region_names(input_file_process)
