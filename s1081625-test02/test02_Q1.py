from datetime import datetime, timedelta
import os
import zipfile


# if datetime.now().date() == datetime.today().date():
    # print ("same day!")
n = 7
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

# zipfile example

def zip_dir(path):
    zf = zipfile.ZipFile('{}.zip'.format(path), 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file_name in files:
            zf.write(os.path.join(root, file_name))
file = 's1081625-test02/output'
path = 'output'
pathzip = 's1081625-test02'
zip_dir(pathzip) # 將檔案壓說
os.makedirs(path, exist_ok=True) # 建立資料夾

for file in sortedfs:
    mt = os.stat(file).st_mtime
    mtime = datetime.fromtimestamp(mt)
    if mtime >= n_days_before and os.path.isfile(file):
        print(file,"--> archive succeeds。")


