# 位置实参的顺序
def printInfo(name,gender):
        print('姓名为' + name + '的用户性别是' + gender + '。')

printInfo('张三','男')
printInfo('男','张三') #实参顺序错误
printInfo(gender = '男',name = '张三') #关键字实参

# 形参的默认值
def printUserInfo(name,gender = '男'): #形参的默认值
        print('姓名为' + name + '的用户性别是' + gender + '。')

printUserInfo('张三')
printUserInfo('李丽','女')