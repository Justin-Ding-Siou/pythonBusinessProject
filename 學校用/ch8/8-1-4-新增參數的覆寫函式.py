class Animal():
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class Dog(Animal):
    def __init__(self, name, leg):
        super().__init__('小狗'+name)
        self.leg = leg
    def sound(self):
        return '汪汪叫'
d = Dog('小黑', 4)
print(d.name, '有', d.leg, '條腿')
print(d.name, d.sound())