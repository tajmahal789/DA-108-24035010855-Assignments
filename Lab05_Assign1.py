import os
import csv
import requests

# Define the CSV file URL
csv_url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv"
csv_filename = "Country_Flags.csv"
flags_directory = "flags"

# Download the CSV file
response = requests.get(csv_url)
with open(csv_filename, "wb") as file:
    file.write(response.content)

# Ensure the flags directory exists
os.makedirs(flags_directory, exist_ok=True)

# Read the CSV file and download flag images
with open(csv_filename, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    
    for row in reader:
        country_name, flag_url = row[0], row[2]  # Adjust based on CSV structure
        
        if flag_url:  # Ensure there's a URL
            flag_response = requests.get(flag_url)
            flag_filename = os.path.join(flags_directory, f"{country_name}.png")
            
            with open(flag_filename, "wb") as flag_file:
                flag_file.write(flag_response.content)
            print(f"Downloaded: {country_name}")
