import os
import time

source = '..'
target_dir = 'D:\Backup'

now = time.strftime('%Y-%m-%d-%H%M%S')

# os.makedirs(target_dir, exist_ok=True) # 建立備份目錄
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory
    print ('Successfully created directory', target_dir)
  
# WinRAR will use the archive extension (zip or rar) to decide the resulting archive format 
target = target_dir + os.sep + now + '.zip' 

# -r 遞迴備份子資料夾； 無 -r 只備份source 資料夾內檔案
rar_command = 'C:\\"Program Files"\\WinRAR\\WinRAR.exe a {0} {1}'.format(target, source)
print(rar_command)
print(os.path.abspath(source))

if os.system(rar_command) == 0:
    print ("備份 succeeded!")
else:
    print ("備份 failed!")