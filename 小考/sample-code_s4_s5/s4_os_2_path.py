import os

#os.path.realpath() - Absolute pathname
print(os.getcwd())
print(os.path.realpath('.'))

# convert a relative path to an absolute filename, use abspath().
if not os.path.exists('test1'):
    os.mkdir('test1')
print(os.path.abspath('./test1'))

curDir = os.getcwd()
# os.path.join() function constructs a pathname out of one or more partial pathnames.
print(os.path.join(curDir, 'test', 'myfile.py'))
print(os.path.join(curDir, '/test', 'myfile.py')) # / indicates absolute path

#os.path.expanduser('~'):  get the current user's home directory
print(os.path.expanduser('~'))
pathname = os.path.join(os.path.expanduser('~'), 'test', 'myfile.py')
print(pathname)

#os.path.split(): split full pathnames, directory names, and filenames into their constituent parts.
dirname, filename = os.path.split(pathname)
print("os.path.split() ...")
print("dirname", "=>", dirname)
print("filename", "=>",filename)
print()

# os.path.dirname(), os.path.basename()
print("os.path.dirname(), os.path.basename()...")
print ("dirname", "=>", os.path.dirname(pathname))
print ("basename", "=>", os.path.basename(pathname))
print ("join", "=>", os.path.join(os.path.dirname(pathname),
                                 os.path.basename(pathname)))

# os.path.splittext(): splits a filename into a tuple containing the filename and the file extension
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)

# os.path.getsize(): checking file size
print(os.path.getsize("C:\\Windows\\System32\\adsnt.dll"))
print()

# pathlib
from pathlib import Path

print("----pathlib----")
print(f"Current directory: {Path.cwd()}")
print(f"Home directory: {Path.home()}")

path = Path.home()
docs = path / 'Documents'

print(docs)
print(path.parts)
print(path.drive)
print(path.root)





