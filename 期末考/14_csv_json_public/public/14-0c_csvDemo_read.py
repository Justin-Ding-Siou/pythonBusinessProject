import csv

# Read csv directly
with open('example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    #headers = next(reader, None) # skip first row
    for row in csv_reader:
        print(type(row))
        print(row)
        print(row[0])
f.close()
        
# Read as text file
with open('example.csv', encoding='utf-8') as f:
    lines = f.readlines()
    
for line in lines:
    print(type(line))
    print(line)
    print(line[0])
f.close()