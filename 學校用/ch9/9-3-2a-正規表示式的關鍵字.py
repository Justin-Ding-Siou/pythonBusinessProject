import string
import re
pr=string.printable
print(re.findall('\d',pr))
print(re.findall('\D',pr))
print(re.findall('\s',pr))
print(re.findall('\S',pr))
print(re.findall('\w',pr))
print(re.findall('\W',pr))
print(re.findall(r'\b','abcd'))
print(re.findall('\B','abcd'))
