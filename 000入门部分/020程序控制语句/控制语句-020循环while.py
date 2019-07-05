# 1.1while语句-循环
# 利用while语句，可以让一个代码块一遍又一遍的执行。
# 只要while语句的条件为True，while子句中的代码就会执行。在代码中，while语句总是包含下面几部分：

# 关键字；
# 条件（求值为True或False的表达式）；
# 冒号；
# 从新行开始，缩进的代码块（称为while子句）
# while True:
#         print("开始循环了")
# 使用shift+F5强制结束程序
# 无限循环的程序的应用场景，监控系统中的连接探测

# import time
# while True:
#         print("开始循环了")
#         time.sleep(5)
# time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。

# 1.2 使用变量来控制循环次数
count = 0
while count < 6:
        count = count + 1
        print("count的值为：" + str(count))
# 使用变量来控制循环次数

# 1.3 使用用户输入和break来控制循环
# 有一个捷径，让执行提前跳出while循环子句。
# 如果执行遇到break语句，就会马上退出while循环子句。
while True:
        name = input("请输入姓名(退出请输入exit)：")
        if name == "exit":
                break
        else:
                print("您输入的姓名是：" + name)

# 1.3 使用用户输入和continue来控制循环
# continue语句用于循环内部。
# 如果程序执行遇到continue语句，就会马上跳回到循环开始处，重新对循环条件求值（这也是执行到达循环末尾时发生的事情）。
while True:
        name = input("请输入姓名(退出请输入exit)：")
        if name == "exit":
                break
        else:
                print("您输入的姓名是：" + name)
                while True:
                        password = input(name + "请输入用户密码(退出请输入exit)：")
                        if password == "123456":
                                print("用户密码输入正确！")
                                break
                        else:
                                continue

# 1.4 增加循环对年龄程序的改进
while True:
        age = input("请输入您的年龄(退出请输入exit)：")
        ageMax = 100
        if age == "exit":
                break
        else:
                print("你的年龄是：" + age)
                intAge = int(age)  # 使用intAge变量将三次类型转换减少到一次
                if (intAge < 1) or (intAge > ageMax):
                        print("年龄输入错误！不能小于1岁或大于100岁")
                else:
                        afterYears = input("请输入过去的年份：")
                        ageResult = intAge + int(afterYears)
                        if ageResult > ageMax:
                                print("过去的年份输入错误！不能大于100岁")
                        else:
                                sentence = "过去" + afterYears + "年后，" + "你的年龄是" + str(ageResult) + "岁。"
                                print(sentence)