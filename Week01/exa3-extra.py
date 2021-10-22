import string

# Step1: 建立英文字元與數字對照表
chars_to_remove = 'IO'
alphabet_string = string.ascii_uppercase
# print(alphabet_string)

for char in chars_to_remove:
    alphabet_string = alphabet_string.replace(char, "")
num_list = list(range(10, 34))
alphanum_dict = {letter: str(num) for (letter, num) in zip(alphabet_string, num_list)}
print(alphanum_dict)

data = input("請輸入身份證號碼: ")
id = data.upper()

# 都是英數字 & 10個字元 & 第一個是字母 & 其他是數字
if (id.isalnum()) & (len(id) == 10) & (id[0].isalpha()) & (id[1:len(id)].isdigit()):
    letter = id[0]
    digits = id[1:-1]
    letter_num = alphanum_dict.get(letter)
    ln_ten = int(letter_num[0])  # 字母對應數字的十位數
    ln_unit = int(letter_num[1])  # 字母對應數字的個位數

    # Step 2: 英文轉成的數字, 個位數乘9再加上十位數
    part1 = ln_unit * 9 + ln_ten

    # Step3: 各數字從右到左依次乘 1, 2, 3, 4, ..., 8
    part2 = 0
    for k in range(0, len(digits)):
        # print(digits[k], 8-k)
        part2 = part2 + (int(digits[k])) * (8 - k)

    # Step4: 求出(2),(3)之和 + 最後1碼
    result = part1 + part2 + int(id[-1])
    print('result = ', result)

    # Step 5: 求出(4)除10後之餘數,用10減該餘數,結果就是檢查碼，若餘數為0，檢查碼就是 0。
    # example： result % 10 = 3, 10 -3 = 7 --> (result + 7) % 10 = 0
    # ref: https://www.w3schools.com/python/python_operators.asp
    [_, reminder] = divmod(result, 10)
    reminder = result % 10

    if reminder == 0:
        print("This is a valid ID.")
    else:
        print("Invalid ID.")

else:
    print("請輸入合法的身份證字號.")

