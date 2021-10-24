import os
os.chdir('c:\\')
print(os.getcwd())
fds = os.listdir('c:\\')
for fd in fds:
    if os.path.isdir(fd):
        print('資料夾:', fd)
    else:
        print('檔案:', fd)