import csv

# Read csv
with open('example.csv', encoding='utf-8') as csvfile:

    # csv.reader(csvfileObj): read from csv file
    csvReader = csv.reader(csvfile, delimiter=',')
    
    # 一行一行讀取 csv reader 物件的內容，並轉換成 陣列
    for idx, row in enumerate(csvReader):
        print('Row #' + str(idx) + ' ' + str(row))
    # csv.reader 物件已到盡頭 
    
    # 一次讀取 csv reader 物件的內容，並轉換成 陣列
    exampleData = list(csvReader)
    print("exampleData ...")
    print(exampleData)

    # Reading data row by row in a for loop
    for idx, row in enumerate(exampleData):
        print('Row #' + str(idx) + ' ' + str(row))
    
    
# csv.writer(csvfileObj): Write csv  
with open('example.tsv', 'w', newline='') as fw: #  for Windows
    csv.writer(fw, delimiter='\t') # , \t between cells in a row

    for row in exampleData:
        csvWriter.writerow(row)
    
fw.close()
print('Done')