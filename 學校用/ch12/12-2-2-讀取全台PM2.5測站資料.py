import requests
import json
url="https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json"
result=requests.get(url, verify=False)
data=json.loads(result.text)
for item in data:
    print(item['county'],item['Site'],item['PM25'],item['DataCreationDate'])
