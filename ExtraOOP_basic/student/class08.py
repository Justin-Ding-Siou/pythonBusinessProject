class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.'%(self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

def main():
    # 創建學生對象並指定姓名和年齡
    stu1 = Student('漯河', 38)
    # 給對象發訊息
    stu1.study('Python程式設計')
    # 給對象發watch_av 消息
    stu1.watch_movie()
    stu2 = Student('旺大小', 15)
    stu2.study('公民與社會')
    stu2.watch_movie()

if __name__ == '__main__':
    main()