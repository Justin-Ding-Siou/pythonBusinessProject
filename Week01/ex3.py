import random

# 產生一組六個數的隨機陣列
print("測試")
for i in range(6):
    L1 = random.randint(1,50)
    print(L1, end=' ')
print(sep='/')
print()


# sqmple 從 list 中隨機抽取 n 個元素，並將 n 個元素以 list 的形式返回
print("第一題")
for i in range(7):
    L2 = random.sample(range(1, 50), 6)
    print(L2, sep= '/')
print()


print("第二題")
ID = input("輸入身分證字號:").upper()
if(len(ID) != 10):
    print("錯誤，身分證字號為10碼")
elif(not ID[0].isalpha()):
    print("錯誤，第一碼須為英文字母")
elif(not ID[1:].isdigit()):
    print("錯誤，後九碼須為數字")
elif(ID[1]< '1' or ID[2] < '2'):
    print("錯誤，第一個數字須為 1 或 2")
else:
    C =  {'A':10, 'B':11, 'C':12, 'D':13, 'E':14,
     'F':15, 'G':16, 'H':17, 'I':34, 'J':18,
     'K':19, 'L':20, 'M':21, 'N':22, 'O':35,
     'P':23, 'Q':24, 'R':25, 'S':26, 'T':27,
     'U':28, 'V':29, 'W':32, 'X':30, 'Y':31,
     'Z':33 }

    # C[ID[0]]
    # EX C[A] = 10 , ID[0] = C's key
    # 15 // 2 ，取 餘 數
    num = C[ID[0]]//10 + (C[ID[0]]%10)*9

    # 第 2 到 第 10 的 數
    # ID[-i])，讀 取 id 倒 數 第 一 個 數
    # 10*1 + 9*2 + 8*3 ..........
    for i in range(2,10):
        num += int(ID[-i])*(i-1)

    ans = 10 - num % 10
    if(ans == int(ID[-1])):
        print(ID + " 是正確的身分證字號")
    elif(int(ID[-1]) == 0):
        print(ID + " 是正確的身分證字號")
    else:
        print(ID + " 不是正確的身分證字號")





