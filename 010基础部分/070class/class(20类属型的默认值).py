# 1.2 类属型的默认值
class People():
        def __init__(self,name,age):
                self.name = name #类的属性定义
                self.age = age
                self.gender = '女' #类的属性默认值
        def study(self): #类的方法定义
                print(self.name + '年龄是' + str(self.age) + '岁'  +'性别是' + self.gender+'正在学习中。。。')

people = People('王小强',32) #对象(实例)的初始化
people.gender = '男' 
people.study()
print( 'name属性的值：' + people.name)

people01 = People('张小花',24)
people01.study()
print( 'name属性的值：' + people01.name)

class People():
        def __init__(self,name,age,gender = '女'):#类的属性默认值
                self.name = name #类的属性定义
                self.age = age
                self.gender = gender
        def study(self): #类的方法定义
                print(self.name + '年龄是' + str(self.age) + '岁'  +'性别是' + self.gender+'正在学习中。。。')

people = People('王小强',32,'男') #对象(实例)的初始化
# people.gender = '男' 
people.study()
print( 'name属性的值：' + people.name)

people01 = People('张小花',24)
people01.study()
print( 'name属性的值：' + people01.name)