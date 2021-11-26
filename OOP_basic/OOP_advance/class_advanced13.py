class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age
    """特性一：將 class (類) 的方法轉換為 只能讀取的 屬性"""
    """@property 是要實現物件導向中設計中封裝的實現方式"""
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩西洋棋.' % self._name)
        else:
            print('%s正在玩大富翁.' % self._name)

def main():
    person = Person('王大槌', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳' AttributeError: can't set attribute
if __name__ == '__main__':
    main()