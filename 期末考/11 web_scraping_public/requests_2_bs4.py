# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

r = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
page = r.content
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())

# Search for any p tag that has the class outer-text
print("--> Find all p tags ...")
print(soup.find_all('p', class_='outer-text'))

print("--> Find all p tags ...")
print(soup.find_all('p', 'outer-text'))
print()

# Find the first p tag that has the class outer-text
print("--> Find the first p tag ...")
print(soup.find('p', attrs={'class': 'outer-text'}))
print()
print("--> Find specific p tag ...")
print(soup.find('p', id='first'))
print()

# Using CSS Selectors: select all p tags under div
print("--> Find all p tags under div ...")
print(soup.select("div p"))