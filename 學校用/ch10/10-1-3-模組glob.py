import glob, os
path = "f:\\teach\\python"
os.chdir(path)
for file in glob.glob("*.py"):
    print(file)