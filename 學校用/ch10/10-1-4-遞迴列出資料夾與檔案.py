import os
path = 'f:\\python'
def find_dir(dir):
    fds = os.listdir(dir)
    for fd in fds:
        full_path = os.path.join(dir, fd)
        if os.path.isdir(full_path):
            print('資料夾:',full_path)
            find_dir(full_path)
        else:
            print('檔案:', full_path)
find_dir(path)