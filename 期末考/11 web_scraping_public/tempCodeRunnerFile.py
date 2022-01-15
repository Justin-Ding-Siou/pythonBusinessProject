# coding: utf-8

# YouBike in New Taipei City
# https://data.ntpc.gov.tw/od/detail?oid=71CD1490-A2DF-4198-BEF1-318479775E8A

import requests

def mday_2_date_str(mday_str):
    #"mday":"20180530214819"
    yr = mday_str[0:4]
    mo = mday_str[4:6]
    dt = mday_str[6:8]
    hr = mday_str[8:10]
    mi = mday_str[10:12]
    se = mday_str[12:]
    date = yr + '-' + mo + '-' + dt
    time = hr + ':' + mi + ':' + se
    return date + ' ' + time

# 網址    
base_url = 'https://data.ntpc.gov.tw/api/datasets/'
data_id = '71CD1490-A2DF-4198-BEF1-318479775E8A'
json_params = 'json?page=0&size=2000'
url = base_url + data_id +'/' +  json_params

r = requests.get(url)
print(url)

sites = r.json()

#sel_sites = [s for s in sites if s["sarea"] == "板橋區"]
sel_sites= []

for s in sites:
  if s["sarea"] == "板橋區":
      sel_sites.append(s)

for i, s in enumerate(sel_sites):
    print('%2d. %s: %s (%s, %s) %2d %s' % \
            (i+1, s['sna'], s['ar'], str(s['lat']), str(s['lng']), \
            int(s['sbi']), mday_2_date_str(s['mday'])))

# "sna":"大鵬華城","tot":"38","sbi":"3","sarea":"新店區","mday":"20180530214819",
# "lat":"24.99116","lng":"121.53398","ar":"新北市新店區中正路700巷3號",
