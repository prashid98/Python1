import json

#read the data from the json file
with open('Csv_json/data2.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Prashid', 'languages': ['English', 'Nepali']}
print(data)
