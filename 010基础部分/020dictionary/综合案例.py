# # 字典构建年龄程序
# ageNameDict = {}
# name = input("请输入您的姓名:")
# age = input("请输入您的年龄:")
# ageNameDict[name] = int(age)
# print(ageNameDict)


# # 字典构建年龄程序的应用
# ageNameDict = {}
# while True:
#         name = input("请输入您的姓名(退出请输入exit)：")
#         age = input("请输入您的年龄(退出请输入exit)：")
#         if age == "exit" or name == "exit":
#                 break
#         else:
#                 ageNameDict[name] = int(age)
#                 print(ageNameDict)
# # 程序的主要问题输名字退出exit无法直接退出，还属输完年龄退出才能终止程序


# # 字典构建年龄程序的第一次迭代
# ageNameDict = {}
# loopSig = True  # 引入了循环运行的标志位变量
# while loopSig:
#         name = input("请输入您的姓名(退出请输入exit)：")
#         if name == "exit":
#                 loopSig = False
#                 continue
#         if loopSig:
#                 age = input("请输入您的年龄(退出请输入exit)：")
#                 if age == "exit":
#                         loopSig = False
#                         continue
#         ageNameDict[name] = int(age)
#         print(ageNameDict)
# # 要对年龄有一个判断并支持重新输入


# 字典构建年龄程序的第二次迭代
ageNameDict = {}
loopSig = True  # 引入了循环运行的标志位变量
ageMax = 100
while loopSig:
        name = input("请输入您的姓名(退出请输入exit)：")
        if name == "exit":
                loopSig = False
                continue
        if loopSig:                  
                while loopSig:
                        age = input("请输入您的年龄(必须小于100，退出请输入exit)：")
                        if age == "exit":
                                loopSig = False
                                continue
                        else:
                                intAge = int(age)
                                if intAge > ageMax:
                                        continue
                                else:
                                        ageNameDict[name] = int(intAge)
                                        print(ageNameDict)
                                        break