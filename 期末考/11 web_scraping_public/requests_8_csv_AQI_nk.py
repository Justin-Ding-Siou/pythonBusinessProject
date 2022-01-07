"""空氣品質指標(AQI):
SiteName(測站名稱)、County(縣市)、AQI(空氣品質指標)、Pollutant(空氣污染指標物)、Status(狀態)、SO2(二氧化硫 ppb)、CO(一氧化碳 ppm)、CO_8hr(一氧化碳8小時移動平均 ppm)、O3(臭氧 ppb)、O3_8hr(臭氧8小時移動平均 ppb)、PM10(懸浮微粒 μgm3)、PM2.5(細懸浮微粒 μgm3)、NO2(二氧化氮 ppb)、NOx(氮氧化物 ppb)、NO(一氧化氮 ppb)、WindSpeed(風速 msec)、WindDirec(風向 degrees)、PublishTime(資料建置日期)、PM2.5_AVG(細懸浮微粒移動平均值 μgm3)、PM10_AVG(懸浮微粒移動平均值 μgm3)、Latitude(緯度)、Longitude(經度)

https://data.gov.tw/dataset/40448
"""

# coding: utf-8
# get and parse AQI open data

import requests
import csv

base_url = 'https://opendata.epa.gov.tw/webapi/api/rest/datastore/'
dataid = '355000000I-000259'
format = 'csv'
userToken = 'Add_your_userToken_here'  # 放入你的 userToken
url = base_url + dataid + "/?format=" + format + "&token=" + userToken

# 替代網址
base_url = 'https://data.epa.gov.tw/api/v1/'
# aqx_p_432?format=csv&limit=100&api_key='
api_key = '9be7b239-557b-4c10-9775-78cadfc555e9'
dataid = 'aqx_p_432'
limit = 200
# url = base_url + dataid + "?format=" + format + "limit=" + limit + "& api_key=" + api_key


url = base_url + dataid
# Parameters for AQI API
AQI_params = {'format': format,'api_key': api_key, 'limit': limit}
r = requests.get(url, verify=False, params=AQI_params)

print(r.url)

if r.status_code != 200:
    print('Failed to get data:', r.status_code)
else:
    cr = csv.reader(r.text.splitlines())
    """
    headers = next(cr)
    headers = [s.replace("\ufeff", "") for s in headers[0:5]]
    print(headers)
    """
    for row in cr: 
      
      if row[4] != '設備維護':
        print(row[0:5])
