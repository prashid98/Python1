import csv

#open the CSV file
file = open("Csv_json/data.csv")
#read the  csv file
csvreader = csv.reader(file)
rows = []
#processing the each row data's
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

# writing in csv file
with open('Csv_json/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])