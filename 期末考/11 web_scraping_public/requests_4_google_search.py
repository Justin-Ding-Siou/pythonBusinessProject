#! python3
# lucky.py - Opens several Google search results.

import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

print('Googling...\n') # display text while downloading the Google page

# Google search parameters：http://www.google.com/search?hl=en&lr=lang_en&q=example
google_url = 'https://google.com/search?'
query_terms = 'covid-19'  # '農禪寺', 'Brexit' 'grasshopper 3d'
host_lang = 'en' # zh-TW, vi, en
search_lang = 'lang_en'  # lang_zh-TW, lang_vi

search_params = {'q': query_terms, 'hl': host_lang, 'lr': search_lang}

# 設定爬蟲的 headers
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

#res = requests.get(google_url + 'q=' + query_terms)
res = requests.get(google_url, params=search_params, headers=my_headers)
#res.raise_for_status()

# Get search results 
soup = BeautifulSoup(res.content, 'html.parser')
# print(res.text)

# Retrieve top five search result links.
linkElems = soup.select('.rc') # ".rc" class
numOpen = min(10, len(linkElems))

for i in range(numOpen):
    title = linkElems[i].a.text  # get first <a> tag
    link = linkElems[i].a.get('href') # get url from <href> tag
    link = unquote(link)
    print(link)
    if link.startswith('/url'):
        # /url?q=http://www.grasshopper3d.com/&sa=U&ved=0ahUKEwjS5oKg2s7WAh...
        #link.find("q"): index of q
        #link.find("&"): index of first &
        siteurl = link[link.find("q")+2:link.find("&sa")]
    elif link.startswith('/search?q'): # /search?q=grasshopper+3d&dcr=0&ie=UTF-8&prmd=ivns...
        siteurl = 'https://google.com' + link
    else:
        siteurl = link
    
    # Open a browser tab for each result.
    # webbrowser.open(siteurl)
    # print("處理過link: " + unquote(siteurl))
    print(title)
    print()