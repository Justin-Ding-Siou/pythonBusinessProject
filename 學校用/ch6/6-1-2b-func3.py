g = 5
def f():
    global g
    print(g)
    g = 10
    print(g)
f()
print(g)
