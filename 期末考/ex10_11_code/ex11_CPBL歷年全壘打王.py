import requests
from bs4 import BeautifulSoup

url="https://www.cpbl.com.tw/stats/yearaward"
response = requests.get(url, verify=False)
html = response.text
soup = BeautifulSoup(html, "html.parser")

record_div = soup.find("div", {"class": "RecordTable"})  # Old
record_div = soup.find("div", class_="RecordTable")      # New1
record_div = soup.find("div", "RecordTable")             # New2


# Get interested headers
headers = []
head_tr = record_div.select_one("table tr")

# Get all headers
for cell in head_tr.find_all("th"):
  headers.append(cell.text)

# print 欄位： "年度", "Team", "全壘打王", "全壘打"
print('{:4} {:11}\t{:3} {:2}'.format(headers[0], "Team",headers[-2], headers[-1]))

# Get data
for data_tr in record_div.select("table tr")[1:11]:
    data = []
    cells = data_tr.select("td")
    data.append(cells[0].text.strip()) # get year
    for cell in cells[-2:]:            # get team, "全壘打王", "全壘打"
      if cell.find('span'):            # 如果 有 span, 抓全部
        for s in cell.find_all('span'):
          data.append(s.getText().strip())
      else:
        data.append(cell.text.strip())
    print('{:4} {:11}\t{:6} {:2}'.format(data[0], data[-3], data[-2], data[-1]))
    