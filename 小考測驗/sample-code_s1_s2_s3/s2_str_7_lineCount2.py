# -*- coding: utf-8 -*-
"""
@author: User
"""

s = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation."""

line_count = word_count = char_count = 0
word_dict = {}

lines = s.splitlines()
#lines = s.split('\n')  #  \r\n
#print(lines)
line_count = len(lines)

for l in lines:
    words = l.split()
    print(words)
    
    word_count += len(words)
    for w in words:
        w = w.rstrip(',.?!') # remove 標點符號
        word_dict.setdefault(w, 0) # add w to word_dict if it does not exist yet
        word_dict[w] = word_dict[w] + 1 # 次數加 1
        char_count += len(w)

print("%10s = %3d" % ("Lines", line_count))
print("%10s = %3d" % ("Words", word_count))
print("%10s = %3d" % ("Characters", char_count))
print(word_dict)

# Find top 5 frequent words; sort by value
v_sorted1 = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
v_sorted2 = sorted(word_dict, key=lambda x: word_dict[x], reverse=True)
v_sorted3 = sorted(word_dict, key=word_dict.get, reverse=True)
print(v_sorted1[:5])
print(v_sorted2[:5])
print(v_sorted3[:5])

# Find top 5 length words, sort by key's length
l_sorted2 = sorted(word_dict, key=lambda x: len(x), reverse=True)
print(l_sorted2[:5])