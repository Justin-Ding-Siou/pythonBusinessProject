class Animal():
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class Dog(Animal):
    def __init__(self, name):
        super().__init__('小狗'+name)
    def sound(self):
        return '汪汪叫'
    def move(self):
        print(self.name + '在馬路上行走')
d = Dog('小黑')
print(d.name, d.sound())
d.move()