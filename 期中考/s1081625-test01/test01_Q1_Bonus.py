import random
sec1 = {chr(ord('a')+i-1): chr(ord('a')+i) for i in range(26) if i % 2}
sec2 = {chr(ord('a')+i+1): chr(ord('a')+i) for i in range(26) if i % 2 == 0}

# sec1 + sec2 字串合併
sec1.update(sec2)

print(sec1)
s = 'an apple a day keeps the doctor away'

print('For randomly generated step = ', random.randrange(2, 27))
print(s)
ss = ''
for index in s:
    if index != ' ':
        ss += sec1[index]
    else:
        ss += ' '
print(ss)

# 更進一步變更密碼
us = ''
for index in ss:
    if index != ' ':
        us += sec1[index]

    else:
        us += ' '
print(us)
