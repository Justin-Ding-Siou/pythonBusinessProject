import requests
from bs4 import BeautifulSoup as soup
url='http://www.python.org/'
def getnews(url):
    page = requests.get(url).text
    htm=soup(page,'html.parser')
    items = [elem for elem in htm.find_all('div', class_='shrubbery') ]
    for item in items:
        if item.h2.contents[1] == 'Latest News':
            ys = [y for y in item.find_all('li')]
            for y in ys:
                time = y.time['datetime']
                link = y.a['href']
                title = y.a.string
                print(time, title, link)
getnews(url)