from bs4 import BeautifulSoup
import requests
import csv
import time


# 存下全部匯率資料
result = []

# 台灣銀行匯率網址
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

# 使用requests物件的get方法把網頁抓下來
response = requests.get(url) 

# text屬性為html文件原始碼
html_doc = response.text 

# 指定lxml作為解析器來建立Beautiful物件
soup = BeautifulSoup(html_doc, "lxml") 

# 找到匯率內容表格
rate_table = soup.find('table').find('tbody')

rate_table_rows = rate_table.find_all('tr')

for row in rate_table_rows:
    # 解析每一列的資料
    columns = row.find_all('td')

    # 存放解析後的每一筆資料
    data = []
    
    for c in columns:
        if c.attrs['data-table'] == '幣別':
            last_div = None
            divs = c.find_all('div')
            
            # 取得最後一個div標籤
            for last_div in divs:pass
            
            # 取得幣別
            data.append(last_div.string.strip())
        elif c.getText().find('查詢') != 0 and str(c).find('print_width') > 0 :
            # 存入匯率資訊
            data.append(c.getText().strip())
    
    # 存入已解析完的一個幣別的全部匯率
    result.append(tuple(data))

print(result)

# 以目前時間建立檔名
now = time.localtime()
file_name = time.strftime('%Y%m%d_%H%M%S.csv', now)
print('輸出的檔案:', file_name)

# 開啟輸出的 CSV 檔案
with open(file_name, 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerow(['幣別', '現金買入', '現金賣出', '即期買入', '即期賣出'])
    writer.writerows(result)