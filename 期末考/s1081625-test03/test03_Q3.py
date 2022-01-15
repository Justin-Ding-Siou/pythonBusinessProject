import requests
import pandas as pd
import glob

dates = [20211001,20211101,20211201]
stockNo = 2330
url_template = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"

for date in dates :
    url = url_template.format(date, stockNo)
    file_name = "{}_{}_股價行情.csv".format(stockNo, date)
    
    data = pd.read_html(requests.get(url).text)[0]
    data.columns = data.columns.droplevel(0)
    data.to_csv(file_name, index=False)
    
    
csv_list = glob.glob('*.csv')
print(u'共發現%s個csv文件'% len(csv_list))

for i in csv_list:
    fr = open(i, 'rb').read()
    with open('2330_2020Q4_股價行情.csv','ab') as f:
        f.write(fr)

print("成功")