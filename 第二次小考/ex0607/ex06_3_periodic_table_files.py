# Find solid elements that are Radioactive or Metal
import json
import csv

# Loop through the file line by line:
f = open("periodic_table.txt", "r", encoding='utf-8')

# for x in f:
  # if x.strip().startswith('{'):
    # print(x.strip().strip(',')
    
data = [line.strip().strip(',') for line in f if line.strip().startswith('{')]
# print(data[0])

pt_dict_lst1 = [json.loads(s) for s in data]
print(pt_dict_lst1[0])
print()


filename = 'periodic_table.csv'
pt_dict_lst2 = []

with open(filename, 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader) # get first row
    lines = list(csv_reader)
    # print(lines[0:2])
    
    for l in lines:
      d = {i[0]: i[1] for i in zip(header, l)}
      pt_dict_lst2.append(d)
print(pt_dict_lst2[0])
print()

# assert pt_dict_lst1[0] == pt_dict_lst2[0]

# Get periodic table copy
periodic_table = pt_dict_lst2.copy()

solid_elements = [x for x in periodic_table if x['Phase'] == 'solid']
#print(*solid_elements)

# sort by 'Radioactive', then by 'Metal' -- multiple passes
solid_lst = sorted(solid_elements, key=lambda x: x['Metal'], reverse=True)
solid_lst.sort(key=lambda x: x['Radioactive'], reverse=True)

# sort by 'Radioactive', then by 'Metal' -- one pass
solid_lst2 = sorted(solid_elements, key=lambda x: (x['Radioactive'], x['Metal']), reverse=True)

for x in solid_lst:
  print("{:>2} {:2s} {:3s} {:3s}".format(x['AtomicNumber'], 
          x['Symbol'], x["Radioactive"], x['Metal']))
                 
assert solid_lst == solid_lst2
assert pt_dict_lst1[0] == pt_dict_lst2[0]