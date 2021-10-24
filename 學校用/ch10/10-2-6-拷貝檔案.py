fin=open('poem.txt','rt',encoding='utf-8')
fout=open('poem2.txt','wt',encoding='utf-8')
line=fin.readline()
while line:
    fout.write(line)
    line=fin.readline()
fin.close()
fout.close()
