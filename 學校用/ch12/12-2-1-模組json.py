import json
dic = { 1: 'a',2: 'b',3: 'c'}
js = json.dumps(dic)
print(js)
dic2 = json.loads(js)
print(dic2)