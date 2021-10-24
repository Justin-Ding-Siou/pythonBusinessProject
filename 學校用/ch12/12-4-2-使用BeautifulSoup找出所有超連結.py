import requests
from bs4 import BeautifulSoup as soup
url='http://www.python.org'
def h(url):
    if url[:4] == 'http' or url[:5]=='https':
        return True
def links(url):
    page = requests.get(url).text
    htm=soup(page,'html.parser')
    alinks=[item['href'] for item in htm.find_all('a')]
    links=[x for x in alinks if h(x)]
    return links
print('找出網址為',url,'的http與https開頭的超連結')
for link in links(url):
    print(link)
