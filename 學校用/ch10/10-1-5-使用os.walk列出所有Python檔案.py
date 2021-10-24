import os
path = "f:\\python"
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
             print(os.path.join(root, file))