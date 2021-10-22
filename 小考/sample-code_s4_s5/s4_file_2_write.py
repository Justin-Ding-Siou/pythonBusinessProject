# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:59:04 2018

Write to an Existing File

"a" - Append - will append to the end of the file
"w" - Write  - will overwrite any existing content
"x" - Create - Creates the specified file, returns an error if the file exists
"""

# Open the file and append content to the file:
f = open("s4_demofile2.txt", "a")
f.write("Now the file has one more line!\n")

# Loop through the file line by line:
f = open("s4_demofile2.txt", "r", encoding='utf-8')
for x in f:
    print("read after one append:", x.strip('\n'))
print()
f.close()

# Open the file "s4_demofile2.txt" and overwrite the content:
f = open("s4_demofile2.txt", "w", encoding='utf-8')
f.write("Woops! the content overwritten! 中文字1\n")
# f.close()

# Loop through the file line by line:
f = open("s4_demofile2.txt", "r", encoding='utf-8')
for x in f:
    print("read after overwriting:", x.strip('\n'))
print()
# f.close()

# Open the file "s4_demofile2.txt" for reading and writing:
with open("s4_demofile2.txt", "a+", encoding='utf-8') as f:
  print(f.tell())
  f.write("Woops! new content appended! 中文字2\n")
  f.write("Woops! new content appended! 中文字3\n")
  print(f.tell())
  f.seek(0, 0) # f.seek(offset, whence): f.seek(0,0), f.seek(0,2)
  print("read after writing:", f.readline())
  
# os.SEEK_SET or 0 (absolute file positioning)
# os.SEEK_CUR or 1 (seek relative to the current position) 
# os.SEEK_END or 2 (seek relative to the file’s end)


#   for x in f:
#     print("read after two appends:",x.strip('\n'))

print("\nReopen a file:")
f = open("s4_demofile2.txt", "r", encoding='utf-8')
for x in f:
    print(x.strip('\n'))