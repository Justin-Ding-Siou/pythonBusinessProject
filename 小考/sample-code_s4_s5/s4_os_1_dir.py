# OS functions

import os

# Get the users environment 
print(os.environ)

# os.getcwd(): Returns the current working directory.
curDir = os.getcwd()

# os.listdir(path): Return a list of the entries in the directory given by path.
os.listdir(curDir)

# os.chdir(path): change current working directory ro path
os.chdir('../00 Misc/')

# os.mkdir(path): Create a directory named path with numeric mode mode.
os.mkdir('newDir') # If the directory already exists, FileExistsError is raised.

# os.rename(src, dst): Rename the file or directory src to dst.
os.rename('newDir','newDir2')

# os.rmdir(path): Remove (delete) the directory path.
os.rmdir('newDir2')

# os.makedirs(path): Recursive directory creation function.
os.makedirs('test1\\test11\\test111', exist_ok = True)

#os.removedirs(path): Remove directories recursively.
os.removedirs('test1\\test11\\test111')

# os.remove(path): Remove (delete) the file path.


