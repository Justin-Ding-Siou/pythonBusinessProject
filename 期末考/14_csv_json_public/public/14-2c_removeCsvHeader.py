#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the data directory.

import csv
import os

data_dir = 'removeCsvHeaderData'
target_dir = os.path.join(data_dir, 'headerRemoved')

os.makedirs(target_dir, exist_ok=True)

# Loop through every file in the current working directory.
for filename in os.listdir(data_dir):
    if not filename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + filename + '...')

    # Read the CSV file with skipping first row
    csv_rows = []
    # Note: csv files 在 data_dir
    csvfile = open(os.path.join(data_dir, filename))
    csv_reader = csv.reader(csvfile)
    next(csv_reader) # skip first row 跳過第一列
    for row in csv_reader:
        #if csv_reader.line_num == 1:
        #    continue # skip first row
        csv_rows.append(row)
    csvfile.close()
    
    #use any to check if any column in the row contains data
    #    if any([x.strip() for x in row]):
    
    # Write out the CSV file.
    with open(os.path.join(target_dir, filename), 'w', newline='') as f:
        csv_writer = csv.writer(f)
        for row in csv_rows:
            csv_writer.writerow(row)
    f.close()
