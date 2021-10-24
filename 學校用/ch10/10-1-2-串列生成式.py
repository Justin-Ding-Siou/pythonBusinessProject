import os
path = "c:\\"
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print(files)
print(dirs)