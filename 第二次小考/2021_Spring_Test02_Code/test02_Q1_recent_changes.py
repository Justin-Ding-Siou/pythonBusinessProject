from datetime import datetime, timedelta
import os

# if datetime.now().date() == datetime.today().date():
    # print ("same day!")
n = 2
now = datetime.now()
n_days_before = now - timedelta(days=n)

# Find files under current directory  
files = [item for item in os.listdir('.') if os.path.isfile(item)]

# Find max filename length
max_len = max([len(file) for file in files])

# sort files by st_mtime
sortedfs = sorted(files, key=lambda x: os.stat(x).st_mtime)  

# for files in os.listdir('.'):
print("起始時間:", n_days_before)
print("現在時間:", now)
print()
for file in sortedfs:
    mt = os.stat(file).st_mtime
    mtime = datetime.fromtimestamp(mt)
    if mtime >= n_days_before:
        print('{1:{0}s} {2}'.format(max_len, file, mtime))