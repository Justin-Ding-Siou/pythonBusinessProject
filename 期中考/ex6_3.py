file = open('periodic_table.txt','rt',encoding='utf-8')
periodic_table = list(file)
print(periodic_table)


print()
# 1. 找出週期內的固態
# 2. 是否有放射性，在一是否為金屬 desc sorted(list, lambda)
# 當我們把 reverse 設成 True 的時候，會把排序的結果由預設的 ascending 改成 descending
solid_elements_test = [item for item in periodic_table if item['Phase'] == 'solid']
print(*solid_elements_test)
# second sorted
solid_lst3 = sorted(solid_elements_test, key=lambda x: x['Metal'], reverse=True)
# first sort
solid_lst3.sort(key=lambda x: x['Radioactive'], reverse=True)


for x in solid_lst3:
    print("{:>2d} {:2s} {:3s} {:3s}".format(x['AtomicNumber'], x['Symbol'], x["Radioactive"], x['Metal']))

# 當字串長度大於 2時，前方加入空白
# 當
print()
solid_lst4 = sorted(solid_elements_test, key=lambda x: (x['Radioactive'], x['Metal']), reverse=True)
for item in solid_lst4:
    print("{:>2d} {:2s} {:3s} {:3s}".format(item['AtomicNumber'], item['Symbol'], item['Radioactive'], item['Metal']))
