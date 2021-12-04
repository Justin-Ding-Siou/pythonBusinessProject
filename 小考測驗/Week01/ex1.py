## 1. 以程式 印出 99 乘法表

## range(1, 11) 產生從1到10的整數序列
for i in range(1, 10):
    for j in range(1,10):
        print(str(i) + 'x' + str(j) + '=' + str(i * j) + ' ', end = '')
    print()

## 2. 輸入一個兩位數n，印出  1！， 2！ 到 n！ 的 階乘， 例如
## 使用input()獲取鍵盤輸入
num = int(input("請輸入兩位數的 n: "))

def factorial(num):
    if num < 0:
        print("階層不存在")

    elif num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num ##fact = fact * num
            num  -= 1
        return fact

print("階層 ", num, "!", factorial(num))


