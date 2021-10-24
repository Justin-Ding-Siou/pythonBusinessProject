import re
s='昔人已乘黃鶴去，此地空余黃鶴樓。\
黃鶴一去不復返，白雲千載空悠悠。'
print(s)
ans = re.match('昔人',s)
if ans:
    print(ans.group())
else:
    print("找不到開頭是「昔人」")
ans = re.match('黃鶴',s)
if ans:
    print(ans.group())
else:
    print("找不到開頭是「黃鶴」")
ans = re.match('.*黃鶴',s)
if ans:
    print(ans.group())
else:
    print("找不到開頭是「.*黃鶴」")
ans = re.search('黃鶴',s)
if ans:
    print(ans.group())
else:
    print("找不到「黃鶴」")
ans = re.findall('黃鶴',s)
if ans:
    print(ans)
else:
    print("找不到「黃鶴」")
ans = re.split('，',s)
print(ans)
ans = re.sub('。','；',s)
print(ans)