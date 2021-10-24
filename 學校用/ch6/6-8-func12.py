def hello(msg):
    def say(text):
        return 'Hello,'+text
    print(say(msg))
    print(say('你好'))
hello('John')