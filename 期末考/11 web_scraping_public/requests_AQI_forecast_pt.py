# coding='utf-8'

import csv
import random
import requests
from datetime import datetime
from prettytable import PrettyTable
# http://zetcode.com/python/prettytable/

# Read csv
url = 'https://opendata.epa.gov.tw/api/v1/AQFN?$skip=0&$top=1000&$format=csv'

# base_url = 'https://data.epa.gov.tw/api/v1/'
# dataid = 'aqf_p_01'
# format = 'csv'
# limit = 32
# sort = 'ForecastDate asc'
# api_key ='9be7b239-557b-4c10-9775-78cadfc555e9'

# url = base_url + dataid
# # Parameters for AQI API
# AQI_params = {'format': format,'api_key': api_key, 'limit': limit, 'sorted': sort}

UserAgentList = [
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90Safari/537.36"]
    
my_user_agent = UserAgentList[random.randint(0, len(UserAgentList)-1)]
# print(my_user_agent)
my_headers = {'User-Agent': my_user_agent}

pt = PrettyTable()
pt.field_names= ['Area', 'MajorPollutant', 'AQI', 'ForecastDate', 'PublishTime']
pt.align["Area"] = "l"
pt.align["MajorPollutant"] = "l"
pt.align["AQI"] = "r"

todaystr = str(datetime.now().date())

response = requests.get(url, headers=my_headers, verify=False)
# response = requests.get(url, headers=my_headers, params=AQI_params, verify=False)


# read from response.text (a string)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    csvReader = csv.reader(response.text.splitlines())
    headers =  next(csvReader, None) # read first row
    AQI_data = []
    
    # 一行一行讀取 csv reader 物件的內容，並加入 AQI_data 陣列
    for idx, row in enumerate(csvReader):
      if row[7][:10] == todaystr:   # get data published today
        row = [idx] + row[1:]       # 新增一個虛擬的區域index 
        AQI_data.append(row)
        print(row)
    
    # Sort AQI_data by date, then by pseudo index
    AQI_sorted = sorted(AQI_data, key=lambda x: (x[4], -x[0]))

    for row in AQI_sorted:
        # print(row)
        # ['Content', 'Area', 'MajorPollutant', 'AQI', 'ForecastDate',
        #  'MinorPollutant', 'MinorPollutantAQI','PublishTime']

        rec = row[1:5] + row[7:8] # list1 + list2, 只取指定欄位的數據
        rec = [x.strip() for x in rec]
        
        rec = ['-- N/A --' if x == '' else x for x in rec] # 空值的欄位填入 -- N/A --
        # print("{:3s}\t{:8s}\t{:>4s}\t{:12s}{:16s}".format(rec[0], rec[1], rec[2], rec[3], rec[4]))
        pt.add_row(rec)
        
    print(pt)    
        