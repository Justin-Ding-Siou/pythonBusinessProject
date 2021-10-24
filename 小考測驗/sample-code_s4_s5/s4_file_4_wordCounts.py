# -*- coding: utf-8 -*-
"""
Count lines, words, characters in text file: s4_read.txt

"""

in_filename = 's4_read.txt'

line_cnt = word_cnt = char_cnt = 0

with open(in_filename , 'r') as f:
    for line in f:
        line_cnt += 1
        words = line.strip('\n').split(' ')
        word_cnt += len(words)
        char_cnt += sum([len(x) for x in words]) 
        
print('%d line(s)' % (line_cnt))
print('%d word(s)' % (word_cnt))
print('%d character(s)' % (char_cnt))
