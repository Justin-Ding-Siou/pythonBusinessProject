import glob
python_files = glob.glob('f:\\teach\\python\\*.py')
for file_name in python_files:
    print('檔案為' + file_name)
    with open(file_name) as f:
        for line in f:
            print(line.rstrip())
    print()
