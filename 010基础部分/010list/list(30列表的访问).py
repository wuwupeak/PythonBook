# 列表使用索引值访问
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
# 假定列表['people01', 'people02', 'people03', 'people04']保存在名为peoples的变量中。
# Python代码peoples[0]将求值为'people01'，peoples[1]将求值为'people02'，依此类推。
# 列表后面方括号内的整数被称为“下标”。列表中第一个值的下标是0，第二个值的下标是1，第三个值的下标是2，依此类推。
# 最后一个列表元素的下标是-1，倒数第二个元素的下标是-2，以此类推。
print(peoples[0])
print(peoples[3])
print(peoples[3].title())  # 首字母大写
print(peoples[-1])  # 取列表最后一个元素
message = '这次选中的是05号：'+peoples[4]  # 元素运算
print(message)

# 列表使用切片访问
# 列表的切片格式为listName[begin:end:step]
print(peoples[0:3])  # 使用切片访问
print(peoples[:3])  # 使用切片访问，默认从头开始
print(peoples[2:])  # 使用切片访问，默认到达列表尾端
print(peoples[-4:])  # 使用切片访问，获取列表最后几个
print(peoples[0:9:3])  # 使用切片的步长来访问列表

# 遍历使用切片的列表
for people in peoples[-6:]: 
        print(people)

# index()方法用列表值来找到下标。
# 如果列表中存在重复的值，就返回它第一次出现的下标。
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peopleValue = 'people05'
peopleIndex = peoples.index(peopleValue)
print("用户" + peopleValue + "在列表片中的下标为：" + str(peopleIndex))

# peopleValue = 'people11'
# peopleIndex = peoples.index(peopleValue)
# print(peopleIndex)

# 对列表值的检查
# 利用in和not in操作符，可以确定一个值否在列表中。
# 像其他操作符一样，in和not in用在表达式中，连接两个值：一个要在列表中查找的值，以及待查找的列表。
# 这些表达式将求值为布尔值。
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
judgePeople = 'people01' in peoples
print(judgePeople)
judgePeople = 'people01' not in peoples
print(judgePeople)
judgePeople = 'people11' in peoples
print(judgePeople)

# 列表对变量的多重赋值
# 多重赋值技巧是一种快捷方式，让你在一行代码中，用列表中的值为多个变量赋值。
# 变量的数目和列表的长度必须严格相等。

# 传统赋值语句
peoples = ['people01', 'people02', 'people03']
peopleOne = peoples[0]
peopleTwo = peoples[1]
peopleThree = peoples[2]
print(peopleOne, peopleTwo, peopleThree)

# 多重赋值
peopleOne, peopleTwo, peopleThree = peoples
print(peopleOne, peopleTwo, peopleThree)