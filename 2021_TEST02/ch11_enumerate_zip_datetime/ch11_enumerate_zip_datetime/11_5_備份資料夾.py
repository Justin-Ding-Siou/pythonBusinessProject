import os
import time

src_dir = ['..']                        # 變更來源目錄
backup_path = 'f:\\backup\\'            # 變更備份目錄
os.makedirs(backup_path, exist_ok=True) # 建立備份目錄

for d in src_dir:
    d_path = os.path.abspath(d)         # 找出絕對路徑
    # d_name = os.path.basename(d_path)
    print(d_path)
    index = d_path.rfind('\\')          # 找到最後一個 '\'
    print(index)
    fmt = '%Y%m%d_%H%M%S'
    # d_path[index+1:]:  d_path的最後一段
    target_file = backup_path + d_path[index+1:] + '_' + time.strftime(fmt) + '.zip '
    zipcmd = '7z a -tzip ' + target_file + d # 7z.exe must be in PATH
    if os.system(zipcmd) == 0:
        print(d_path, '備份成功')
    else:
        print(d_path, '備份失敗')
