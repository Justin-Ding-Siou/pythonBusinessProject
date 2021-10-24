import requests
import xml.etree.ElementTree as xmltree
url="https://pypi.python.org/pypi?%3Aaction=rss"
result=requests.get(url)
element=xmltree.fromstring(result.text)
print(xmltree.dump(element))
for item in element.findall('./channel/item'):
    for b in item:
        print(b.tag, b.text)
    print()
