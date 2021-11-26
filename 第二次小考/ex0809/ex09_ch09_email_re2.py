# validating an email, one email at a time
import re

emails = ['asss@',  '_test@mail.yzu.edu.tw', '.bbb@nec.co.jp','test@.edu.tw', 
'John..Doe@example.com', 'john@example.com.','ase2ss.xxx.go',  
'test2.yzu@mis-.goto.com', 'test2.yzu@-server.goto.com', 'test2.yzu@mis-server.goto.com',
'aaa@xxx.kr', 'yzu.python@gmail.com', 'John.Doe@example.com', 'join_me@yzu.edu.tw', ]


# Simple regex
print("First Try:")
regex = '[a-zA-Z0-9]+@[a-zA-Z0-9\.]+'
for email in emails:
  match = re.search(regex, email)
  if match:
    print(email)
print()


# More elaborated regex
# regex 1 fail at '_test@mail.yzu.edu.tw', '.bbb@nec.co.jp', 
# 'John..Doe@example.com', 'john@example.com.', 'test2.yzu@mis-.goto.com',
'test2.yzu@-server.goto.com'
# regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"

# regex 2 fails at 'john@example.com.', 'test2.yzu@mis-.goto.com',
# 'test2.yzu@-server.goto.com'
# regex = r"^[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"

# regex 3 fails at 'test2.yzu@mis-.goto.com', 'test2.yzu@-server.goto.com'
# regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@(\w+[.]){1,3}\w{2,3}$'
# regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@([a-zA-Z0-9-]+[\.]){1,3}\w{2,}$'

regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@([a-zA-Z0-9]+[-]?[a-zA-Z0-9]+[\.]){1,3}[a-zA-Z]{2,}$'

# print(s)
print("Second Try:")
for email in emails:
  match = re.search(regex, email)
  if match:
    print(email)

