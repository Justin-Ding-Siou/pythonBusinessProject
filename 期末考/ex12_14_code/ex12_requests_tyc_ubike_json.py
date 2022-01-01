# coding: utf-8

# YouBike in New Taipei City
# https://data.tycg.gov.tw/opendata/datalist/datasetMeta?oid=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c

import requests
import random

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


user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"]
    
my_user_agent = random.choice(user_agent_list)
my_headers = {'User-Agent': my_user_agent}

base_url = 'http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
tycParams = {'format':'json', 'limit':400}

area = "中壢區"

r = requests.get(base_url, params=tycParams, headers=my_headers)
print(r.url)

# Get sites
sites = r.json()['result']['records']
sel_sites = [site for site in sites if site["sarea"] == area]

data_rows = []

for s in sel_sites:
    row = [s['sna'], s['ar'], int(s['sbi']), float(s['lat']), float(s['lng'])]
    data_rows.append(row)

data_sorted = sorted(data_rows, key=lambda x: x[2], reverse=True)

print('---------- ' + area + ' Top 10 可借車數場站 ----------')
for r in data_sorted[:10]:
    print(f'{r[0]}: {r[1]}, {r[2]}, ({r[3]}, {r[4]})')
print()    
