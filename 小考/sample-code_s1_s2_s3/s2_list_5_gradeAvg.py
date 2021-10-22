# -*- coding: utf-8 -*-
"""
Calculate student grade avarage
"""

grades = [[79, 69, 89], [80, 80, 80], [64, 86, 60]]

def calcAvg(alist):
    # total = 0
    # for i in range(len(alist)):
    #   total += alist[i]
    total = sum(alist)
    average = total/len(alist)
    return average
    
def main():
    print("Solution 1:")
    for i in range(len(grades)):
        avg = calcAvg(grades[i])
        print('#%d student, average = %.2f' % (i+1, avg))
    print()
    # enumeate(list): create a list of tuples, each is a pair (index, value)
    # print(list(enumerate(grades)))
    print("Solution 2:")
    for i, grade in enumerate(grades):
        avg = calcAvg(grade)
        print('#%d student, average = %.2f' % (i+1, avg))
    print()
    
main()