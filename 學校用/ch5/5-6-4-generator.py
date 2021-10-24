odd = (num for num in range(1,10) if (num % 2) == 1)
print(odd)
for num in odd:
    print(num)
for num in odd: #只能執行一次，此區塊不會輸出資料
    print(num)