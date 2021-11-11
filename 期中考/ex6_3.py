import json

fin = open('periodic_table.txt','rt',encoding='utf-8')
p_dict = {}

for line in fin:
    foo1 = line.replace('periodic_table = [','')
    foo2 = foo1.replace(']','')
    foo3 = foo2.rstrip()
    print(foo3)
    jsObj = json.dumps(foo3)
print(type(foo3))
print(type(jsObj))







fin.close()