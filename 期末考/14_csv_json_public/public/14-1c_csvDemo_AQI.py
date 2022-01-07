import csv

# Read csv

with open('AQI_20191101.csv', encoding='utf-8') as f:

    # csv.reader(f): read from csv file
    csv_reader = csv.reader(f, delimiter=',')

    headers = next(csv_reader)
    # Remove 'utf-8-sig' BOM
    headers = [s.replace("\uFEFF", "") for s in headers]
    print(headers[0:5])
    
    for row in csv_reader:
        print(row[0:5])

f.close()
print('Done')