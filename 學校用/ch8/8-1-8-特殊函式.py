class Animal():
    def __init__(self, name):
        self.__name = name
    def sound(self):
        pass
    def show_name(self):
        return self.__name
    def eq(self, other):
        return self.__name == other.show_name()
    def __eq__(self, other):
        return self.__name == other.show_name()
class Dog(Animal):
    def __init__(self, name, leg):
        super().__init__('小狗'+name)
        self.leg = leg
    def sound(self):
        return '汪汪叫'
d1 = Dog('小黑', 4)
d2 = Dog('小黑', 4)
print(d1.eq(d2))
print(d1 == d2)
d3 = Dog('小白', 4)
print(d1.eq(d3))
print(d1 == d3)