# -*- coding: utf-8 -*-
# Opens several Bing search results.

import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

print('Searching Bing...') # display text while downloading the Bing page

# Bing search parameters：https://www.bing.com/search?q=example&setlang=en-US&mkt=en
bing_url = 'https://www.bing.com/search?'
query_terms =  '農禪寺' # '異塵餘生76'  # '農禪寺', 'Brexit' 'grasshopper 3d'
host_lang = 'zh-TW' # zh-TW, en-gr, en-us # 界面語言
search_lang = 'zh-TW'  # zh-TW, en-us     # 資料語言

# 設定搜尋參數
search_params = {'q': query_terms, 'setLang': host_lang, 'mkt': search_lang}

# 設定爬蟲的 headers
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

#res = requests.get(bing_url + 'q=' + query_terms)
res = requests.get(bing_url, params=search_params, headers=my_headers)

#print(res.raise_for_status())
print(res.url)
print(unquote(res.url)) # 把 % 開頭的16進位網址轉換為正常文字
print()

# Get search results 
soup = BeautifulSoup(res.text, 'html.parser')

# Retrieve top five search result links.
linkElems = soup.select('.b_algo h2 a') # <a> tag under <h2> inside div.b_algo
numOpen = min(10, len(linkElems))

for i in range(numOpen):
    title = linkElems[i].text  # getText()
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)
    print("Link: " + link)
    if not link.startswith('http'): # 開頭沒有 http 
        #  /search?q=Visual+programming+language+wikipedia&...
        siteurl = 'https://bing.com' + link
    else: # 正常網址, 例如 https://udn.com/news/story/6811/2909774
        siteurl = link
    
    # Open a browser tab for each result.
    # webbrowser.open_new(siteurl)
    print(title)
    # print("Processed link: " + unquote(siteurl))
    print()