import os
import time

drive = "D:"                                         # 變更Drive C:, D:
src_dir = ['..', 'D:\\Users\\public\\drivers\\']     # 變更來源目錄
backup_path = drive + os.sep + 'Backup' + os.sep     # 變更備份目錄
os.makedirs(backup_path, exist_ok=True)              # 建立備份目錄

for d in src_dir:
    d_path = os.path.abspath(d)         # 找出絕對路徑
    d_name = os.path.basename(d_path)
    print("d_path: ", d_path)
    print("d_name: ", d_name)
    
    index = d_path.rfind('\\')          # 找到最後一個 '\'
    fmt = '%Y%m%d_%H%M%S'
    # d_path[index+1:]:  d_path的最後一段
    # D:\backup\Python入門_程式碼_20211104_161635.zip
    target_file = backup_path + d_path[index+1:] + '_' + time.strftime(fmt) + '.zip '
    
    # zipcmd = '7z a -tzip ' + target_file + d                               # 7z.exe in PATH
    zipcmd = 'C:\\"Program Files"\\7-Zip\\7z.exe a -tzip ' + target_file + d # 7z.exe not in PATH
    print(zipcmd)
    if os.system(zipcmd) == 0:
        print(d_path, '備份成功\n')
    else:
        print(d_path, '備份失敗\n')
