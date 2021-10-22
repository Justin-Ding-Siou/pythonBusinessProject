# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:08:01 2018

"""

import random

# random.randint(m, n): Return a number between m and n (both included):
num = random.randint(1, 100)

if num % 2 == 0:
    print(num, "is an even number.")
    print('%d is an even number.' % (num))
    print('{0:d} is an even number.'.format(num))
    print(f'{num} is an even number.')
else:
    print(num, "is an odd number.")
    print('%d is an odd number.' % (num))
    print('{:d} is an odd number.'.format(num))
    print(f'{num} is an odd number.')