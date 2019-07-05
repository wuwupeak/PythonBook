# 1.4 类的继承
class People():
        def __init__(self,name,age):
                self.name = name #类的属性定义
                self.age = age
                self.gender = '女' #类的属性默认值
        def getPeopleInfo(self): #类的方法定义
                print(self.name + '，年龄是' + str(self.age) + '岁，'  +'性别是' + self.gender+'。')
        def setMale(self):
                self.gender = '男'

class Student(People): #继承自People
        def __init__(self,name,age):
                super().__init__(name,age)
                self.school = '常州信息职业技术学院' #子类新增的属性
        def getSchoolInfo(self): #子类新增的函数
                print(self.name + '来自学校：' + self.school)
        def setSchool(self, schoolName): #子类新增的函数
                self.school = schoolName

student = Student('李莉',22)
student.getPeopleInfo()
student.getSchoolInfo()
student.setSchool('常州工学院')
student.getSchoolInfo()