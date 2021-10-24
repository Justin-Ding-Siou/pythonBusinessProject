import csv
with open('99.csv', 'wt', newline='') as fout:
    writer = csv.writer(fout)
    for i in range(1,10):
        for j in range(1,10):
            writer.writerows([(str(i),str(j),str(i*j))])
with open('99.csv', 'rt') as fin:
    reader = csv.DictReader(fin, fieldnames=['被乘數','乘數','積'])
    rows = [row for row in reader]
    print(rows)
    fout = open('99b.csv', 'wt',newline='',encoding='utf-8')
    writer = csv.DictWriter(fout, fieldnames=['被乘數','乘數','積'])
    writer.writeheader()
    writer.writerows(rows)
    fout.close()