# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:40:00 2018

"""
# Create a simple dictionary {key1: value1, key2:value2}
dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(dict1)

# Create dictionary using dict()
dict2 = dict(brand="Ford", model="Mustang", year=1964)
## note that keywords are not string literals 不是字串
## note the use of equals  = rather than colon for the assignment
print(dict2)

#  Get the value of a specific key
print(dict1["year"])

# Change value of a specific key
dict2["year"] = 2018
print(dict2)

# Loop Through a Dictionary
## get keys
for k in dict1:
    print(k)
for k in dict1.keys():
    print(k)
    
## get values
for k in dict1:
    print(dict1[k])
for v in dict1.values():
    print(v)
    
## get key and value
for k, v in dict1.items():
    print(k,v)
    
# Add new items
dict1['color'] = 'red'
print(dict1)

# remove items
#del dict1['color']
x = dict1.pop('color') # return key's value
print(x)
print(dict1)
print()

# setdefault: return value of a specific key, otherwise set it
# 如果 "year" 是一個 key, 回傳 dict1["year"], 
# 否則 dict1["year"]=1999, 回傳 1999
x = dict1.setdefault("year", 1999)
print(x)

x = dict1.setdefault("color", "white")
print(x)
print(dict1)
print()

# dir() function returns all properties and methods of the specified object
print(dir(dict1))