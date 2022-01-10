#e8-3-1抓取台銀匯率資訊
import requests
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime

rate_list = ['歐元', '美金', '英鎊', '日圓']

res = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
html = res.text
soup = BeautifulSoup(html, "lxml")
table_trs = soup.find("table", {"title":"牌告匯率"}).find("tbody").find_all("tr")

file_name = "ex13_台銀_" + "外匯賣出匯率" + ".csv"
now = strftime("%Y-%m-%d %H:%M:%S", localtime())
print(now)
curs = ['時間']
rates = [now]

for single_tr in table_trs:
    cell = single_tr.select("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).text
    currency_name = currency_name.replace("\r","").replace("\n","").replace(" ","")
    currency_rate = cell[2].text
    print(currency_name, currency_rate)
    curs.append(currency_name)
    rates.append(currency_rate)
    
with open(file_name, "a+", encoding="utf-8-sig", newline='') as f:
  writer = csv.writer(f)
  if f.tell() == 0:
    writer.writerow(curs)
  writer.writerow(rates)

print(f"{file_name} saved.")