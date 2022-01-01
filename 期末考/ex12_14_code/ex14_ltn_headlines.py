# -*- Coding: utf-8 -*-

# import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlsplit
import random

url = 'https://www.ltn.com.tw'

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"]
    
my_user_agent = random.choice(user_agent_list)
my_headers = {'User-Agent': my_user_agent}

r = requests.get(url, headers=my_headers)

#print(r.raise_for_status())
#print(r.status_code)

# Get crawling results 
soup = BeautifulSoup(r.text, 'html.parser')

page_title = soup.select('head title')[0].text
print('Crawling %s ...\n' % (page_title))

# Retrieve top five search result links.
linknodes = soup.select('div.swiper-slide a') # <a> tag under div.swiper-slide class
limit = min(10, len(linknodes))

keywords = ['breakingnews']
skip_words = ['TAIPEI TIMES']
bad_urls= ['https://pv1.ltn.com.tw/']

cat_dict = {'world': '國際', 'politics': '政治', 'society': '社會', 'life': '生活', 'sports': '體育','ec.ltn': '財經', 'ent.ltn': '娛樂', 'entertainment': '娛樂', 'business': '財經', 'election': '選舉', 'people': '人物'} 

for i in range(limit):
    title = linknodes[i].text.strip('\n')
    link = linknodes[i].get('href') # get url from <href> tag
    link = unquote(link)
    #print(title)
    print("--> 原始 link: " + link)
    cat ='其他'
    # 根據網址的特定字判斷類別
    for k in cat_dict.keys():
        if k in link:
            cat = cat_dict[k]
            break

    # print(urlsplit(link))
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(link))
    
    # 去除標題包含特定停用字, 以及基本網址在排除名單的連結
    # print(any(w in title for w in skip_words))
    # if not any(w in title for w in skip_words) and base_url not in bad_urls:
    
    # 接受含正面表列關鍵字的link
    if any(w in link for w in keywords):
        print(cat + "： " + title)
        print(link)
        #print(base_url)
        print()
        #webbrowser.open(link)
        
input("Press any key to continue...")