sec1 = {chr(ord('a')+i): chr(ord('a')+i-1) for i in range(26) if i % 2}
sec2 = {chr(ord('a')+i): chr(ord('a')+i+1) for i in range(26) if i % 2 == 0}
sec1.update(sec2)
print(sec1)
s = 'an apple a day keeps the doctor away'
print(s)
ss = ''
for c in s:
    if c != ' ':
        ss += sec1[c]
    else:
        ss += ' '
print(ss)
us = ''
for c in ss:
    if c != ' ':
        us += sec1[c]
    else:
        us += ' '
print(us)
