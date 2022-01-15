
import requests
from prettytable import PrettyTable

def mday_2_date_str(mday_str):
    yr = mday_str[0:4]
    mo = mday_str[4:6]
    dt = mday_str[6:8]
    hr = mday_str[8:10]
    mi = mday_str[10:12]
    se = mday_str[12:]
    date = yr + '-' + mo + '-' + dt
    time = hr + ':' + mi + ':' + se
    return date + ' ' + time

# 網址 ，youbike1.0   
base_url = 'https://data.ntpc.gov.tw/api/datasets/'
data_id = '71CD1490-A2DF-4198-BEF1-318479775E8A'
json_params = 'json?page=0&size=1000'
url = base_url + data_id +'/' +  json_params

r = requests.get(url)
# print(url)

sites = r.json()

#sel_sites = [s for s in sites if s["sarea"] == "板橋區"]
sel_sites= []

for s in sites:
  if s["sarea"] == "板橋區":
      sel_sites.append(s)

# python pretty table
x1 = PrettyTable()
x1.field_names_youbike1 = ["場站名稱","詳細地址","總停車站","可借車數","更新時間"]


for i, s in enumerate(sel_sites):
    x1.add_row([s['sna'], s['ar'], int(s['tot']),int(s['sbi']), mday_2_date_str(s['mday'])])
print("Youbike1.0")
print(x1)



print()
# 網址 ，youbike1.0   
url2 = 'https://data.ntpc.gov.tw/api/datasets/010E5B15-3823-4B20-B401-B1CF000550C5/json?page=0&size=1000'

r = requests.get(url2)
# print(url)

sites = r.json()

sel_sites2= []

for s in sites:
  if s["sarea"] == "板橋區":
      sel_sites2.append(s)

# python pretty table
x2 = PrettyTable()
x2.field_names_youbike2 = ["場站名稱","詳細地址","總停車站","可借車數","更新時間"]


for i, s in enumerate(sel_sites2):
    x2.add_row([s['sna'], s['ar'], int(s['tot']),int(s['sbi']), mday_2_date_str(s['mday'])])
    
print("Youbike2.0")
print(x2)


