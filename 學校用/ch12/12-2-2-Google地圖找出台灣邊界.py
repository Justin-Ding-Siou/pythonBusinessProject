import requests
import json
url="http://maps.googleapis.com/maps/api/geocode/json?address=taiwan&sensor=false"
result=requests.get(url)
data=json.loads(result.text)
print(data)
for i in data['results']:
    for key,value in i['geometry']['bounds'].items():
        print(key,value)