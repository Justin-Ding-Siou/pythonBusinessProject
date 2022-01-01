#e8-3-1抓取台銀匯率資訊
import requests
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime, strptime, mktime
from os.path import exists

res = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
html = res.text
soup = BeautifulSoup(html, "lxml")
table_trs = soup.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr")

for single_tr in table_trs:
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).text
    currency_name = currency_name.replace("\r","").replace("\n","").replace(" ","")
    currency_rate = cell[2].text
    print(currency_name, currency_rate)
    file_name = "e8-3-1" + currency_name + ".csv"
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    f = open(file_name, "a", newline='')
    w = csv.writer(f)
    w.writerows(data)
    f.close()
