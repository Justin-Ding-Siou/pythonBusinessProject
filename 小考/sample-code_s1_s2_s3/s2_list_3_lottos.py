
# -*- coding: utf-8 -*-
"""
7組不重複大樂透電腦選號： 6個 1-49 的亂數
"""
import random

# Create lotto numbers without duplicates 
def create_lotto(): 
    lotto = []
    n = 1
    while n <= 6:
        rn = random.randint(1, 49)
        if rn not in lotto:
            lotto.append(rn)
            n += 1
    lotto.sort()
    #lotto2 = [str(x).zfill(2) for x in lotto]
    #print(lotto2)
    return lotto
   
def main():
    lottoLst = []
    c = 1
    while c <= 7:
        newlist = create_lotto()
        if newlist not in lottoLst:
            lottoLst.append(newlist)
            c += 1
            print(newlist)
        
main()