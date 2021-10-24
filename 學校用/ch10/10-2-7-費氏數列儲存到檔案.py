fout=open('fib.txt','wt')
def fib(num):
    count = 1
    a = 1
    b = 1
    print(count, a, file=fout)
    while(count < num):
        a, b = b, a+b
        count += 1
        print(count, a, file=fout)
fib(1000)
fout.close()