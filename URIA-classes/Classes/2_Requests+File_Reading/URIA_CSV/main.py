import requests
import csv


url = "https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv"
response = requests.get(url)
if response.status_code == 200:
    rows = response.text.splitlines()
    reader = csv.reader(rows, quotechar='"')
else:
    exit("Error downloading.")


# Take the first row from the csv
column_names = next(reader)
processed = []

for row in reader:
    split = row
    meteor = {}
    # Run a for loop once for each piece of data
    # And add the data to the dictionary
    for i in range(len(split)):
        # Take the column name and data from their lists
        name = column_names[i]
        data = split[i]
        meteor[name] = data
    processed.append(meteor)

