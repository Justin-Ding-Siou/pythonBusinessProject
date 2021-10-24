s1 = '春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'

# string.split(separator, maxsplit)
list1 = s1.split('，')
print(list1)

# separator.join(iterable) 
# iterable: such as list, str, dict and tuple)
s2 = '#'.join(list1)
print(s2)

# string.replace(oldvalue, newvalue, count)
s3 = s1.replace('春','冬')
print(s3)

print("s1為", s1, '在s1的', s1.find('花落'), '位置發現"花落"')
print("s1為", s1, '在s1中從右邊數過來第一個出現"處"的位置為', s1.rfind('處'))
print(s1.startswith('春眠'))
print(s1.endswith('多少。'))
print('s1=', s1,"s1.count('處')等於", s1.count('處'))
s1 = '春眠不覺曉'
print(s1.center(10))
print(s1.rjust(10))
print(s1.ljust(10))
s1 = 'An apple a day.'
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
print(s1.upper())
print(s1.lower())
s1='123'
print(s1.zfill(5))
s1 = ' Hello, Mary.  '
print(s1.strip())
print(s1.lstrip(' H'))
print(s1.rstrip(' .'))
