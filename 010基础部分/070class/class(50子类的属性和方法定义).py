# 1.5子类的属性和方法定义
class People():
        def __init__(self,name,age):
                self.name = name #类的属性定义
                self.age = age
                self.gender = '女' #类的属性默认值
        def getPeopleInfo(self): #类的方法定义
                print(self.name + '，年龄是' + str(self.age) + '岁，'  +'性别是' + self.gender+'。')
        def setMale(self):
                self.gender = '男'

class Student(People):
        def __init__(self,name,age,grade):#增加子类的属性
                super().__init__(name,age)
                self.grade = grade #增加子类的属性
        def getPeopleInfo(self): #重写父类的方法
                print(self.name + '，年龄是' + str(self.age) + '岁，'  +'性别是' + self.gender+'。'
                        + '现在上' + str(self.grade) + '年级。')

student = Student('李莉',22,2)
student.getPeopleInfo()