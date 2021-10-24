import requests
url = 'http://www.python.org'
data = requests.get(url)
print(data.encoding)
print(data.status_code)
print(data.headers)
print(data.text)
