from bs4 import BeautifulSoup as soup
fin = open('web.htm', encoding='utf-8')
s = fin.read()
htm = soup(s, 'html.parser')
print(htm.title.prettify())
print(htm.title.contents)
print(htm.title.contents[0])
print(htm.title.name)
print(htm.title.string)
print(htm.meta)
print(htm.meta['content'])
for item in htm.find_all('td'):
    print(item)
for item in htm.find_all('td',class_='table_head'):
    print(item)
for item in htm.find_all('td',class_='table_siteurl'):
    print(item.a['href'])