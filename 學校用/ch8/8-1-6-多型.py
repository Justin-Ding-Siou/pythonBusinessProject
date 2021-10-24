class Animal():
    def __init__(self, name):
        self.name = name
    def who(self):
        return self.name
    def sound(self):
        pass
class Dog(Animal):
    def __init__(self, name):
        super().__init__('小狗'+name)
    def sound(self):
        return '汪汪叫'
class Bird():
    def __init__(self, name):
        self.name = '小鳥'+name
    def who(self):
        return self.name
    def sound(self):
        return '啾啾叫'
def talk(obj):
    print(obj.who(), '正在', obj.sound())
a = Animal('動物')
talk(a)
d = Dog('小黑')
talk(d)
b = Bird('小黃')
talk(b)