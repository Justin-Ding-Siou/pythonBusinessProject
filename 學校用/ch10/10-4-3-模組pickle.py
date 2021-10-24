import pickle
mylist = [a for a in range(1,10)]
with open('pickle','wb') as fout:
    pickle.dump(mylist,fout)
with open('pickle','rb') as fin:
    p = pickle.load(fin)
    print(p)