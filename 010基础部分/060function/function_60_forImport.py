# 1.1 基本的函数定义
def printName(userName):
        print('打印名字为' + userName + '的用户')

def sumTwo(one,two):
        print('输入的两个数的和是' + str(one + two))

# 1.2 位置实参的顺序
def printInfo(name,gender):
        print('姓名为' + name + '的用户性别是' + gender + '。')

# 1.3 形参的默认值
def printUserInfo(name,gender = '男'): #形参的默认值
        print('姓名为' + name + '的用户性别是' + gender + '。')

# 1.4 返回值
def get_fullName(firstName,lastName):
        return (firstName+lastName)

def get_name(firstName,lastName,middleName = ''):#使用默认值增强灵活性
        return(firstName + middleName + lastName)

# 1.5 任意数量的实参-元祖
def print_peoples(*peoples):
        for people in peoples:
                print(people)

def print_info(gender,*peoples):
        print('性别是' + gender + '性的同学如下：')
        for people in peoples:
                print(people)

# 1.6 任意数量的关键字实参-字典
def build_info(**user):
        userInfo = {}
        for key,value in user.items():
                userInfo[key] = value
        return userInfo

