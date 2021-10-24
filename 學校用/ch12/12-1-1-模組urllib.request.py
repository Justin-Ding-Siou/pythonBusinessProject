import urllib.request as ur
url='https://www.python.org'
resp=ur.urlopen(url)
print(resp.geturl())
print(resp.status)
print(resp.getheaders())
data=resp.read()
print(data)
print(data.decode())
