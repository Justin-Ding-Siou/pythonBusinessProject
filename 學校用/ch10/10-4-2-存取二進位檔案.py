bindata = bytes(range(0,32))
with open('binfile','wb') as fout:
    fout.write(bindata)
with open('binfile','rb') as fin:
    binary = fin.read()
    print(binary)