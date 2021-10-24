class Animal():
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name):
        super().__init__('小狗'+name)
a = Animal('動物')
d = Dog('小白')
print(a.name)
print(d.name)

