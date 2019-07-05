# 1.1if语句-判定
# if语句的子句（也就是紧跟if语句的语句块），将在语句的条件为True时执行。如果条件为False，子句将跳过。
age = 40
if age == 40:
        print("年龄为40")
# if关键字；
# 条件（即求值为True或False的表达式）；
# 冒号；
# 在下一行开始，缩进的代码块（称为if子句）。

# 1.2 else语句
# if子句后面有时候也可以跟着else语句。只有if语句的条件为False时，else子句才会执行。
# 在英语中，else语句读起来可能是：“如果条件为真，执行这段代码。否则，执行那段代码”。
age = 50
if age == 40:
        print("年龄为40")
else:
        print("年龄不为40")

# 1.3 elif语句
# 虽然只有if或else子句会被执行，但有时候可能你希望，“许多”可能的子句中有一个被执行。
# elif语句是“否则如果”，总是跟在if或另一条elif语句后面。
# 它提供了另一个条件，仅在前面的条件为False时才检查该条件。
age = 50
if age == 40:
        print("年龄为40")
elif age == 50:
        print("年龄为50")
else:
        print("年龄不为40")

# 1.4 if使用比较操作符和逻辑运算符混合运算
age = 50
if (age == 40) or (age == 50):
        print("年龄为40或者50")
else:
        print("年龄不为40或者50")

# 1.2 改进的年龄计算程序
age = input("请输入您的年龄：")
print("你的年龄是：" + age)
if (int(age) <1) or (int(age) > 100) :
        print("年龄输入错误！不能小于1岁大于100岁")
else:
        afterYears = input("请输入过去的年份：")
        ageResult = int(age) + int(afterYears)
        if ageResult > 100:
                print("过去的年份输入错误！不能大于100岁")
        else:
                sentence = "过去" + afterYears + "年后，" + "你的年龄是" + str(ageResult) + "岁。"
                print(sentence)

# 1.3 增加变量对年龄程序的改进
age = input("请输入您的年龄：")
ageMax = 100
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