def hello(msg):
    def say(hi):
        return hi+msg
    return say
x=hello('Claire')
y=hello('Fiona')
print(x('Hello,'))
print(y('Hi,'))