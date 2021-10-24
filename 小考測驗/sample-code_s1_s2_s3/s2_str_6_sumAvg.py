# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:45:12 2018

Get sum and average of a list of numbers
"""

s = input("Enter numbers separated by space: ")

slist = s.split()
print(slist)

total = 0
for i in slist:
    total = total + int(i)

print("%7s = %d" % ("Total", total))
print("Average = %.2f" % (total/len(slist)))


import re
str = "This,isa;test"
# re.split(pattern, string)
print(re.split(",|;", str))

# Using list comprehension
nlist = [int(x) for x in s.split()]

print("%7s = %d" % ("Total", sum(nlist)))
print("Average = %.2f" % (sum(nlist)/len(nlist)))
