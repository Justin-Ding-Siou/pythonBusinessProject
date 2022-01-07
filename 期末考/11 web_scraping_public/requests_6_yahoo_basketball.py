#! python3
# lucky.py - Opens several Yahoo NBA News.

import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlsplit

print('Crawling Yahoo Basketball News...') # display text while downloading the Google page

base_url = 'https://tw.news.yahoo.com/basketball'

myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

# Download the raw CA Bundle at https://certifi.io/en/latest/
# cert_path = "C:/Users/Public/drivers/certs.pem"

r = requests.get(base_url, verify=False, headers=myheaders)

#print(r.raise_for_status())
#print(r.status_code)

# Get crawling results 
soup = BeautifulSoup(r.text, 'html.parser')
page_title = soup.select('head > title')[0].text
print("\n----" + page_title + "----\n")

# Retrieve top ten search result links.
#linkElems = soup.select('li.js-stream-content.Pos\(r\) a.C\(\$c-fuji-grey-l\)')
linkElems = soup.select('li[class*="js-stream-content"] a[class*="fuji-grey-l"]') # <a> tag under "li"
print(len(linkElems))
numOpen = min(20, len(linkElems))

bad_urls = ['http://help.yahoo.com', 'https://info.yahoo.com', 'https://beap.gemini.yahoo.com', 'https://twhbl.yahoo.com.tw', 'https://b.gemini.yahoo.com', 'https://yahoo-hbl.tumblr.com']
nba_words = ['nba', 'NBA', '勇士', '湖人']

for i in range(numOpen):
    title = linkElems[i].text
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link)
    #print("原始的link: " + link + "\n")
    if link.startswith('http'):
        # https://info.yahoo.com/privacy/tw/yahoo/relevantads.html
        # link.find(".com"): index of .com
        if ".com.tw" in link:
            baseurl = link[0:link.find(".com.tw")+7]
        else: # .com
            baseurl = link[0:link.find(".com")+4]
        # baseurl = "{0.scheme}://{0.netloc}".format(urlsplit(link))
        # print(baseurl)
        if baseurl not in bad_urls:
            siteurl = link
        else:
            # print("bad url: ", baseurl)
            continue
    # /nba-戈貝爾開賽三分鐘爆氣被趕出場-回到健身房繼續訓練-082252250.html
    # /勇士半場變4打5，場均三分外線17中1成進攻漏洞
    elif any(w in link for w in nba_words):
        print(title)
        print("處理過link: " + link)
        siteurl = 'https://tw.news.yahoo.com' + link
    else: 
        continue
    
    # Open a browser tab for each result.
    # webbrowser.open_new(siteurl)
    
    print("Final link: " + unquote(siteurl))
    print()