# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

file open
"r" - Read - Default value.
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""

# file_object  = open("filename", "mode")
import os

dirpath = os.path.dirname(__file__)

# Read content: file_object.read()
filename= "s4_demofile.txt"
f = open(os.path.join(dirpath, filename), "rb")
print(f.read())
print()

# Read only parts of the file: file_object.read(n): 
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
print(f.read(10)) # 10 characters
print()

# Read one line: file_object.readline(): 
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
print(f.readline())
print()

# Loop through the file line by line:
f = open(os.path.join(dirpath, filename), "r", encoding='utf-8')
for line in f:
  print(line.strip('\n'))
print()
  
# Read Lines: file_object.readlines(): 
# The with statement creates a context manager and it will automatically 
# close the file handler for you when you are done with it
filename = "s4_test4.csv"
with open(os.path.join(dirpath, filename), "r", encoding='cp950') as f:
  print(f.readlines())