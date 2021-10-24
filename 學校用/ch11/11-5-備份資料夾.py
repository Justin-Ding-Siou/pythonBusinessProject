import os
import time
src_dir = ['d:\\blog']
for d in src_dir:
    index=d.rfind('\\')
    fmt = '%Y%m%d_%H%M%S'
    target_file = 'd:\\backup\\' + d[index+1:] + '_' + time.strftime(fmt) + '.zip '
    zipcmd = '7z a -tzip ' + target_file + d
    if os.system(zipcmd) == 0:
        print('備份成功')
    else:
        print('備份失敗')
