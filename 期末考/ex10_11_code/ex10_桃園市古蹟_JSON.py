import requests
import json

url="https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?\
method=exportEmapJson&typeId=A&classifyId=1.1"

response = requests.get(url)
data = json.loads(response.text)    # 取得文字再轉成json
data = response.json()              # 直接取得 json
# print(data)
# [{"name":"嘉義仁武宮","type":"1.1","level":"縣(市)定古蹟","address":"北榮街54號","longitude":"120.450824910622","latitude":"23.4815353287417","openTime":"06:00~22:00","registerDateValue":"1998-04-30","headCityName":"嘉義市政府","srcWebsite":"http://nchdb.boch.gov.tw/assets/overview/monument/19980430000001","buildingYearName":"1683-1723(清代-康熙)","buildingCreateWestYear":"1701","registerDateValue_eng":"1998-04-30","typeName":"古蹟","mainTypeName":"文化資產 ","cityName":"嘉義市","groupTypeName":"文化資產","mainTypePk":"19980430000001","version":"1.0","hitRate":176},{"name":"嘉義西門長老教會禮拜堂","type":"1.1","level":"縣(市)定古蹟","address":"導民里15鄰垂楊路309號","longitude":"120.447471812389","latitude":"23.4732069053089","openTime":"08:00~18:00","registerDateValue":"2005-03-08","headCityName":"嘉義市政府","srcWebsite":"http://nchdb.boch.gov.tw/assets/overview/monument/20050308000001","buildingYearName":"1912-1926(日本時代-大正時期)初年","buildingCreateWestYear":"","registerDateValue_eng":"2005-03-08","typeName":"古蹟","mainTypeName":"文化資產 ","cityName":"嘉義市","groupTypeName":"文化資產","mainTypePk":"20050308000001","version":"1.0","hitRate":223}]

if data:
    for d in data:
        if d['cityName'] == '桃園市':
            print(d['name'], d['level'], d['cityName'], d['address'])
else:
    print("No data available.")