class Animal():
    count = 0
    def __init__(self):
        Animal.count += 1
    def kill(self):
        Animal.count -= 1
    @classmethod
    def show_count(cls):
        print('現在有',cls.count,'隻動物')
a = Animal()
Animal.show_count()
b = Animal()
Animal.show_count()
c = Animal()
Animal.show_count()
a.kill()
Animal.show_count()
