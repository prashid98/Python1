import csv
#open the file in the readmode
with open('CSV_json/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #open the file in writemode
    with open('CSV_jason/new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
