
import json

string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

# json.loads(string): convert string of json data to a json object
jsonObj = json.loads(string_of_json_data)

print("jsonObj is a", type(jsonObj))
print(jsonObj)
print(jsonObj['name'])

#{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

jsonObj = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}

# json.dumps(jsonObj): convert a json object back to string of json data 
string_of_json_data = json.dumps(jsonObj)

print("strig_of_json_data is a", type(string_of_json_data))
print(string_of_json_data)
#print(string_of_json_data['name']
#'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'