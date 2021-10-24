class Leg():
    def __init__(self, num, look):
        self.num = num
        self.look = look
class Animal():
    def __init__(self, name, leg):
        self.__name = name
        self.leg = leg
    def show_name(self):
        return self.__name
    def show(self):
        print(self.show_name(),'有', self.leg.num, '隻', self.leg.look, '腿')
leg = Leg(4, '短短的')
a = Animal('小狗', leg)
a.show()