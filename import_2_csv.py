import csv

# Define input and output file paths for cleaning
input_file_clean = r'C:\Users\Sarah Son Kim\Downloads\Project 3\Market Temp Index_or.csv'
output_file_clean = r'C:\Users\Sarah Son Kim\Downloads\Project 3\cleaned_Market Temp Index_or.csv'

# Define input file path for processing RegionName
input_file_process = r'C:\Users\Sarah Son Kim\Downloads\Project 3\cleaned_Market Temp Index_or.csv'

# List of columns to replace NULL values with '0' in the '20xx' format
columns_to_replace = [
    'Mar_2018_TempIndex', 'Apr_2018_TempIndex', 'May_2018_TempIndex', 'Jun_2018_TempIndex', 'Jul_2018_TempIndex', 'Aug_2018_TempIndex', 'Sept_2018_TempIndex', 'Oct_2018_TempIndex', 'Nov_2018_TempIndex', 'Dec_2018_TempIndex', 
    'Jan_2019_TempIndex', 'Feb_2019_TempIndex', 'Mar_2019_TempIndex', 'Apr_2019_TempIndex', 'May_2019_TempIndex', 'Jun_2019_TempIndex', 'Jul_2019_TempIndex', 'Aug_2019_TempIndex', 'Sept_2019_TempIndex', 'Oct_2019_TempIndex', 'Nov_2019_TempIndex', 'Dec_2019_TempIndex', 
    'Jan_2020_TempIndex', 'Feb_2020_TempIndex', 'Mar_2020_TempIndex', 'Apr_2020_TempIndex', 'May_2020_TempIndex', 'Jun_2020_TempIndex', 'Jul_2020_TempIndex', 'Aug_2020_TempIndex', 'Sept_2020_TempIndex', 'Oct_2020_TempIndex', 'Nov_2020_TempIndex', 'Dec_2020_TempIndex', 
    'Jan_2021_TempIndex', 'Feb_2021_TempIndex', 'Mar_2021_TempIndex', 'Apr_2021_TempIndex', 'May_2021_TempIndex', 'Jun_2021_TempIndex', 'Jul_2021_TempIndex', 'Aug_2021_TempIndex', 'Sept_2021_TempIndex', 'Oct_2021_TempIndex', 'Nov_2021_TempIndex', 'Dec_2021_TempIndex', 
    'Jan_2022_TempIndex', 'Feb_2022_TempIndex', 'Mar_2022_TempIndex', 'Apr_2022_TempIndex', 'May_2022_TempIndex', 'Jun_2022_TempIndex', 'Jul_2022_TempIndex', 'Aug_2022_TempIndex', 'Sept_2022_TempIndex', 'Oct_2022_TempIndex', 'Nov_2022_TempIndex', 'Dec_2022_TempIndex', 
    'Jan_2023_TempIndex', 'Feb_2023_TempIndex', 'Mar_2023_TempIndex', 'Apr_2023_TempIndex', 'May_2023_TempIndex', 'Jun_2023_TempIndex', 'Jul_2023_TempIndex', 'Aug_2023_TempIndex', 'Sept_2023_TempIndex', 'Oct_2023_TempIndex', 'Nov_2023_TempIndex', 'Dec_2023_TempIndex', 
    'Jan_2024_TempIndex', 'Feb_2024_TempIndex', 'Mar_2024_TempIndex', 'Apr_2024_TempIndex', 'May_2024_TempIndex'
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


# Example usage:
# Clean the initial CSV file
clean_csv(input_file_clean, output_file_clean)

