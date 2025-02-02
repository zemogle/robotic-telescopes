# Import CSV data from file surve_responses.csv into a json file
# Usage: python importsurveydata.py

import csv
import json

# Open the CSV file
csvfile = open('survey_responses.csv', 'r')
# jsonfile = open('survey_responses.json', 'w')

# Read the CSV file
fieldnames = ("Timestamp","Your Name" ,"organisation" ,"Contact Email Address", "website","facility","number","networked","location" ,"modes","waveband","instrumentation","apertures","historic","hours","used_by","available_to_whom")
reader = csv.DictReader(csvfile, fieldnames)

# Skip the header row
next(reader)
next(reader)

# Write the JSON file
# jsonfile.write('[')
for row in reader:
    print(row.get('Timestamp'), row.get('Your Name'), row.get('Contact Email Address'))
#     json.dump(row, jsonfile)
#     jsonfile.write(',\n')
# jsonfile.write(']')
# jsonfile.close()
csvfile.close()

print("Import complete")