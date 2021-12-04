ID= input("請輸入身份證字號:").upper()
if(len(ID) != 10):
    print("錯誤，身份證字號須為 10 碼")
elif(not ID[0].isalpha()):
    print("錯誤，第一碼須為英文字母")
elif(not ID[1:].isdigit()):
    print("錯誤，後九碼須為數字")
elif(ID[1]<'1' or ID[1]>'2'):
    print("錯誤，第一個數字須為 1 或 2")
else:
     X= {'A':10, 'B':11, 'C':12, 'D':13, 'E':14,
     'F':15, 'G':16, 'H':17, 'I':34, 'J':18,
     'K':19, 'L':20, 'M':21, 'N':22, 'O':35,
     'P':23, 'Q':24, 'R':25, 'S':26, 'T':27,
     'U':28, 'V':29, 'W':32, 'X':30, 'Y':31,
     'Z':33 }
     num= X[ID[0]]//10 + (X[ID[0]]%10)*9
     for i in range(2,10):
        num += int(ID[-i])*(i-1)
     ans= 10 - num % 10
     if(ans==int(ID[-1])):
        print(ID + " 是正確的身分證字號")
     else:
        print(ID + " 不是正確的身分證字號")








# 完整版，Ex3 的延伸
# 代碼表
idcheck = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
TotalVal = 0
idcode = ""
while (len(idcode) != 10):
    idcode = input("輸入身分證號:")  # A123456789

print("身分證:" + idcode)
CapVal = idcheck[ord(idcode[0]) - 65]  # 查表
idcode11 = str(CapVal) + idcode[1:10]
TotalVal = int(idcode11[0])  # 10123456789

for index, item in enumerate(idcode11[1:10]):
    m = int(item) * (9 - index)
    TotalVal = TotalVal + m

TotalVal = TotalVal + int(idcode11[10])
print("身分證是", end='')
if TotalVal % 10 == 0:
    print("正確的")
else:
    print("錯誤的")


