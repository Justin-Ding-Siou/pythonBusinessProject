# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

# Create a New File
"x" - Create - will create a file, will fail if it exists
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

"""

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile.txt", "w", encoding='utf-8')
f.write("Write a new line including 中文字 简体字 to myfile.txt")

# Loop through the file line by line:
f = open("myfile.txt", "r", encoding='utf-8')
for x in f:
    print(x)

f.close()

# Check if file exist before removing it
import os

if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
  print("myfile.txt removed")
else:
  print("The file does not exist.")
