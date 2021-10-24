import string
import random
chs = string.ascii_letters + string.digits
pwd=""
for x in range(random.randint(8,12)):
    pwd+=random.choice(chs)
print(pwd)