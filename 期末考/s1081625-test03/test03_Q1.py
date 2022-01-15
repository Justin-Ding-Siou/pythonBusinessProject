# 請先安裝 pip install AnueCrawler
from anuecrawler.news import headline
# 抓取當天資料
hd = headline
#指定日期範圍
# print(headline)
print()

hd.browse('2021-1-13','2021-1-13')
#擷取指定資料(依據鉅亨網API)
X = hd.query(['title'])
print("Crawling 頭條新聞 | Anue 鉅亨 新聞...")

print(X)

