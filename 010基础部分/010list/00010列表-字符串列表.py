# 字符串列表的定义
# “列表”是一个值，它包含多个字构成的序列。
# 术语“列表值”指的是列表本身（它作为一个值，可以保存在变量中，或传递给函数，像所有其他值一样），而不是指列表值之内的那些值。
# 列表值看起来像这样：['people01', 'people02', 'people03', 'people04']。
# 就像字符串值用引号来标记字符串的起止一样，列表用左方括号开始，右方括号结束，即[]。
# 列表中的值也称为“表项”。表项用逗号分隔（就是说，它们是“逗号分隔的”）。
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表



# # 列表元素的遍历
# for people in peoples:
#     print(people)

# # 列表元素的下标
# print(peoples[0])

# # 使用下标遍历列表元素值
# for index in range(0,10):
#     print(peoples[index])

# # 计算列表的元素个数的内置函数
# elementNumber = len(peoplesTwo)
# print("peoples变量存储的列表总共有" + str(elementNumber) + "个元素！")

# # 使用列表元素下标和列表长度来下标遍历列表元素
# for index in range(len(peoples)):
# print(peoples[index])

# # 使用列表元素值来获取列表元素下标的第一种方法
# peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表
# elementValue = 'people04'
# elementIndex = 0
# for people in peoples:
# print("目前检索的元素下标是：" + str(elementIndex))
# print("目前检索的元素值是：" + people)
# if elementValue == people:
# print("用户" + elementValue + "的下标是：" + str(elementIndex))
# break
# else:
# elementIndex = elementIndex + 1


# # 使用列表元素值来获取列表元素下标的第二种方法
# elementValue = 'people08'
# for elementIndex in range(len(peoples)):
# if elementValue == peoples[elementIndex]:
# print("用户" + elementValue + "的下标是：" + str(elementIndex))
# break


# # 使用列表元素值来获取列表元素下标的内置函数
# peopleName = 'people02'
# indexNumber = peoples.index(peopleName)
# print("用户" + peopleName + "在列表片中的下标为：" + str(indexNumber))

# # 对列表元素值进行排序的内置函数
# peoples.sort()  # 升序
# print(peoples)
# peoples.sort(reverse = True)  # 降序
# print(peoples)

# -------------------------------------------------------------------------------------------------
# 使用enumerate遍历列表下标和列表值
# enumerate函数用于遍历序列中的元素以及它们的下标
# 多用于在for循环中得到计数,enumerate参数为可遍历的变量，如 字符串，列表等
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表
for index, people in enumerate(peoples):
        print("下标是:" + str(index) + "的列表元素值是:" + people)

# 定义空列表并添加列表元素的内置函数
peoples = []
peoples.append("people01")
print(peoples)
peoples.append("people02")
print(peoples)

# 删除列表元素的内置函数
peoples = ['people01', 'people01', 'people02',  'people06', 'people07', 'people08','people09', 'people10']

peoples.pop()  # 使用栈的方式删除列表元素，后进先出
print(peoples)

peoples.remove('people01')  # 删除指定元素值的列表元素(第一个符合的值)
print(peoples)

del peoples[0]  # 删除指定元素下标的列表元素
print(peoples)

# 判定元素值是否在列表中存在的语句
peoples = ['people01', 'people01', 'people01', 'people02', 'people02', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表
peopleExist = "people01" in peoples
print(peopleExist)
peopleExist = "people11" not in peoples
print(peopleExist)

#  将列表中的唯一值构建为一个新列表的处理程序
peoples = ['people01', 'people01', 'people01', 'people02', 'people02', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表
peoplesUnique = []
for people in peoples:
        if people not in peoplesUnique:
                peoplesUnique.append(people)
print(peoplesUnique)

# 计算列表中唯一值出现次数的处理程序
peoplesCount = []
for peopleUnique in peoplesUnique:
        peopleCount = 0
        for people in peoples:
                if people == peopleUnique:
                        peopleCount = peopleCount + 1
        peoplesCount.append(peopleCount)
print(peoplesUnique)
print(peoplesCount)

# 获取元素值在列表中出现次数的内置函数
peoples = ['people01', 'people01', 'people01', 'people02', 'people02', 'people06', 'people07', 'people08','people09', 'people10']  #字符串列表
peopleCount = peoples.count("people01")
print(peopleCount)

# 计算列表中唯一值出现次数的处理程序
peoplesUnique = []
for people in peoples:
        if people not in peoplesUnique:
                peoplesUnique.append(people)
for peopleUnique in peoplesUnique:
        peopleCount = peoples.count(peopleUnique)
        print(peopleUnique + "在列表中出现了" + str(peopleCount) + "次。")

