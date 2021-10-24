import re
s='昔人已乘黃鶴去，此地空余黃鶴樓。\
黃鶴一去不復返，白雲千載空悠悠。'
print(s)
ans = re.findall('^昔人',s)
print(ans)
ans = re.findall('空悠悠。$',s)
print(ans)
ans = re.findall('[黃白]',s)
print(ans)
ans = re.findall('\W',s)
print(ans)
ans = re.findall('黃鶴樓\W',s)
print(ans)
ans = re.findall('黃鶴.\W',s)
print(ans)
ans = re.findall('[^黃鶴]',s)
print(ans)