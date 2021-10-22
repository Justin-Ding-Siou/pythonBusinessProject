import os

totalSize = 0
pathname = 'C:\\Windows\\System32'

for filename in os.listdir(pathname):
    totalSize = totalSize + os.path.getsize(os.path.join(pathname, filename))

print(pathname + " has " + str(totalSize/10**6) + " Mbytes.")