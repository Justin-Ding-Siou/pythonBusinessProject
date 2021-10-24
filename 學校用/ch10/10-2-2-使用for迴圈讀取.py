fin = open('poem.txt','rt',encoding='utf-8')
for line in fin:
    print(line.rstrip())
fin.close()