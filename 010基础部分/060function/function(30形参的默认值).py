# 形参的默认值
def printUserInfo(name,gender = '男'): #形参的默认值
        print('姓名为' + name + '的用户性别是' + gender + '。')

printUserInfo('张三')
printUserInfo('李丽','女')