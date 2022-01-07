# coding: utf-8 

import requests
from pprint import pprint

response = requests.get("https://en.wikipedia.org/robots.txt")

# vars(x) returns this dictionary of x' instance variables
# dir(x) returns a dictionary of x's attributes, its class's and base classes attributes
print(dir(response))
print(vars(response).keys())

# get response content
txt = response.text
print(txt)

# get response encoding
print(response.encoding)

# check for bad request
print(response.raise_for_status())

# get response status_code
print(response.status_code)

# response headers
#print(response.headers)
#print(json.dumps(dict(response.headers), indent=4))
pprint(dict(response.headers)) # transform to a dict first 
print()

# get response headers content
print(response.headers['content-type'])
