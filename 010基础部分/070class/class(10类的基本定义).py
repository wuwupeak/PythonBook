# # 1.1 类的基本定义和引用
# class People():
#         def __init__(self,objectName,objectAge):
#                 self.name = objectName #类的属性定义
#                 self.age = objectAge
#         def study(self): #类的方法定义
#                 print(self.name + '年龄是' + str(self.age) + '岁正在学习中。。。')


# people = People('王小强',32) #对象(实例)的初始化
# people01 = People('张小花',24)

# message = people.name + '和' +people01.name + '一起去吃饭'
# print(message)

# people.study()
# people01.study()

# 1.1 类的基本定义和引用
class People():
        def __init__(self,objectName,objectAge,objectGender):
                self.name = objectName #类的属性定义
                self.age = objectAge
                self.gender = objectGender
        def study(self): #类的方法定义
                print(self.name + '年龄是' + str(self.age) + '岁正在学习中。。。')
        def ageAdd(self): #方法对属性的操作
                self.age = self.age + 1


people = People('王小强',32,'男') #对象(实例)的初始化
people01 = People('张小花',24,'女')

print(people.name + '的性别是：' + people.gender + ',年龄是：' + str(people.age) + '。')
print(people01.name + '的性别是：' + people01.gender + ',年龄是：' + str(people01.age) + '。')

people.ageAdd()
print(people.name + '的性别是：' + people.gender + ',年龄是：' + str(people.age) + '。')
print(people01.name + '的性别是：' + people01.gender + ',年龄是：' + str(people01.age) + '。')








# people01.name = '李晓红' #对象的属性改变
# people01.study()
# print( 'name属性的值：' + people01.name)