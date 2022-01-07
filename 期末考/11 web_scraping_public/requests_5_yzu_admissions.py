# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

base_url = 'https://www.yzu.edu.tw/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}

r = requests.get(base_url, headers=headers)

#print(r.raise_for_status())
#print(r.status_code)

# Get crawling results 
soup = BeautifulSoup(r.content, 'html.parser')

page_title = soup.select('head  title')[0].text
print('Crawling %s 招生訊息...\n' % (page_title))

# Retrieve top five search result links.
linkElems = soup.select('div.slideCon.mod_admissions div.linkItem a')
print(len(linkElems))
numOpen = min(10, len(linkElems))

include_words = ['碩士班', '博士班', '大學部']

for i in range(numOpen):
    title = linkElems[i].getText()
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)
    
    # print(any(w in title for w in include_words))
    # title 一定要有 ['碩士班', '博士班', '大學部'] 其中一個

    if any(w in title for w in include_words):
         link = 'https://www.yzu.com.tw' + link
         print(title)
         print(link)
         print()
    else:
         continue 
