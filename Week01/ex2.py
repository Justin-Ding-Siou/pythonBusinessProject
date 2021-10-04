## 1.課本 3-24 第3題: 給定兩首唐詩 , 「紅豆生南國，春來發幾枝? 願君多采擷，此物最相思 。 」與「春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。」
##　請找出這兩首詩去除標點符號後共同的字。
import string
from string import punctuation

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”?，！【】（）、。：；’‘……￥·「」"""

poem1 = '「紅豆生南國，春來發幾枝? 願君多采擷，此物最相思。」'
dicts = {
    i:'' for i in punctuation}
punc_table = str.maketrans(dicts)
new_poem1 = poem1.translate(punc_table)
print(new_poem1)


poem2 = '「春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。」'
dicts = {
    i:'' for i in punctuation}
punc_table = str.maketrans(dicts)
new_poem2 = poem2.translate(punc_table)
print(new_poem2)

def lcs(S,T):
    m = len(S) #找到長度
    n = len(T) #找到長度
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set() # 建立空的集合
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

# ex02
ret = lcs(new_poem1, new_poem2)
for s in ret:
    print (s)

## 參考 leetcode https://blog.csdn.net/Orientliu96/article/details/103905680
## 我還不懂怎麼寫



## 2.建議定義一個 函數 例如 def fun_mul(array，multiplier, start):, 所以
## fun_mul([1,2,3,4,5,6,7,8,9], 8, 1) 輸出上半段結果
## fun_mul([1,2,3,4,5,6,7,8,9], 9, 2) 輸出下半段結果

## array 遞增，係數
## multiplier 固定陳法，X
## start 單數遞增，常數
## a * x + b = y，類似一元二次方程式

def solution():
    x = 100
    a = 2
    b = 1
    y = a*x+b

print(solution())



## 3.以程式 產生 身份證第一位字母對應表 （一堆字母對應一堆數字）
## 輸入測試的身分證id，找到堆應數字
## input: U122093098
## output: U = 28，哪裡人? 性別: 男或女

dicts = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', 'G': '16',
'H': '17', 'J': '18', 'K': '19', 'L': '20', 'M': '21', 'N': '22', 'P': '23',
'Q': '24', 'R': '25', 'S': '26', 'T': '27', 'U': '28', 'V': '29', 'W': '30',
'X': '31', 'Y': '32', 'Z': '33'}
