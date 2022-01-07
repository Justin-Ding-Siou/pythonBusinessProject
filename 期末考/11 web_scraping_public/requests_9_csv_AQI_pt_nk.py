# coding: utf-8
# get and parse AQI open data

"""空氣品質指標(AQI):
SiteName(測站名稱)、County(縣市)、AQI(空氣品質指標)、Pollutant(空氣污染指標物)、Status(狀態)、SO2(二氧化硫 ppb)、CO(一氧化碳 ppm)、CO_8hr(一氧化碳8小時移動平均 ppm)、O3(臭氧 ppb)、O3_8hr(臭氧8小時移動平均 ppb)、PM10(懸浮微粒 μgm3)、PM2.5(細懸浮微粒 μgm3)、NO2(二氧化氮 ppb)、NOx(氮氧化物 ppb)、NO(一氧化氮 ppb)、WindSpeed(風速 msec)、WindDirec(風向 degrees)、PublishTime(資料建置日期)、PM2.5_AVG(細懸浮微粒移動平均值 μgm3)、PM10_AVG(懸浮微粒移動平均值 μgm3)、Latitude(緯度)、Longitude(經度)

https://data.gov.tw/dataset/40448
https://data.epa.gov.tw/dataset/aqx_p_432/resource/8ff027dc-2da2-42e8-85de-78ac3faf470e
"""


import requests
import csv
from prettytable import PrettyTable

base_url = 'https://opendata.epa.gov.tw/webapi/api/rest/datastore/'
dataid = '355000000I-000259' # 空氣品質指標
format = 'csv'
userToken = 'Add_your_userToken_here'  # 放入你的 userToken
# url = base_url + dataid + "/?format=" + format + "&token=" + userToken
# r = requests.get(url, verify=False)

# 替代網址
base_url = 'https://data.epa.gov.tw/api/v1/'
api_key = '9be7b239-557b-4c10-9775-78cadfc555e9'
dataid = 'aqx_p_432'
limit = 200
# url = base_url + dataid + "?format=" + format + "limit=" + limit + "& api_key=" + api_key

url = base_url + dataid
# Parameters for AQI API
AQI_params = {'format': format,'api_key': api_key, 'limit': limit}

r = requests.get(url, verify=False, params=AQI_params)
#print(r.url)

rows = []

if r.status_code != 200:
    print('Failed to get data:', r.status_code)
else:
    cr = csv.reader(r.text.splitlines())
    next(cr) # skip first row
    for row in cr:
        #print(row[0:5])
        rows.append(row[0:5])

pt = PrettyTable()
pt.field_names= ["測站名稱", "縣市", "空氣品質指標", "空氣污染指標物","狀態"]
pt.align["測站名稱"] = "l"
pt.align["空氣污染指標物"] = "l"
pt.align["空氣品質指標"] = "r"

rows = [r for r in rows if len(r[2]) > 0] # skip null AQI values

# sort data rows by AQI (should be integer)
data_rows = sorted(rows, key=lambda x: int(x[2]), reverse=True)
#print(rows)

for row in data_rows:
    pt.add_row(row)
print(pt)