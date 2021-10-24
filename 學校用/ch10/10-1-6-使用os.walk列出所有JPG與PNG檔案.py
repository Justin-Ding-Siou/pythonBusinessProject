import fnmatch, os
path = "f:\\python"
exts = ['*.jpg', '*.jpeg', '*.png', '*.tif']
matches = []
for root, dirs, files in os.walk(path):
    for ext in exts:
        for file in fnmatch.filter(files, ext):
            matches.append(os.path.join(root, file))
for image in matches:
    print(image)