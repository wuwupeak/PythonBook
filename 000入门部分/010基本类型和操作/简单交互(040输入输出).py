# 1.1 input()函数接受用户的输入
age = input()
print(age)
print(type(age))
# 1101input()函数调用是一个表达式，它求值为用户输入的任何字符串。
# 函数等待用户在键盘上输入一些文本，并按下回车键。

# 1.2 构造友好的输入输出
age = input("请输入您的年龄：")
print("你输入的年龄数字是：" + age)
print("程序age的数据类型是：" + str(type(age)))

# 1.3 交互式增强年龄程序
age = input("请输入您的年龄：")
print("你的年龄是：" + age)
afterYears = input("请输入过去的年份：")
ageResult = int(age) + int(afterYears)
sentence = "过去" + afterYears + "年后，" + "你的年龄是" + str(ageResult) + "岁。"
print(sentence)