import xml.etree.ElementTree as xmltree
tree = xmltree.ElementTree(file='my.xml')
root = tree.getroot()
print(root.tag)
for a in root:
    print('標籤', a.tag, '，屬性', a.attrib, '，值', a.text)
    for b in a:
        print('標籤', b.tag, '，屬性', b.attrib, '，值', b.text)
for item in root.iter('item'):
    print(item.attrib , item.text)
for item in root.findall('./morning/item'):
    print('標籤為', item.tag, '，屬性', item.attrib, '，值', item.text)