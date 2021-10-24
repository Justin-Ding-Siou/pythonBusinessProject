g = 5
def f1():
    print(g)
f1()
def f2():
    #print(g)
    g = 10
    print(g)
f2()
print(g)