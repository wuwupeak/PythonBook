# 1.3 通过方法修改属性值
class People():
        def __init__(self,name,age):
                self.name = name #类的属性定义
                self.age = age
                self.gender = '女' #类的属性默认值
        def study(self): #类的方法定义
                print(self.name + '年龄是' + str(self.age) + '岁'  +'性别是' + self.gender+'正在学习中。。。')
        def setMale(self):
                self.gender = '男'

people = People('王小强',32) #对象(实例)的初始化
people.setMale()
people.study()
print( 'name属性的值：' + people.name)