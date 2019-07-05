# 列表元素的修改
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoples[0] = 'people001'  # 修改元素值
print(peoples)

# 列表元素的添加
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoples.append('people11')  # 添加元素
print(peoples)

# 空列表添加元素
peoples = []  # 空列表
print(peoples)
peoples.append('people01')  # 为空列表添加元素
print(peoples)

# 在指定位置插入列表元素
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoples.insert(1, 'people01to02')  # 在指定索引插入元素
print(peoples)

# 删除指定位置的列表元素
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
del peoples[9]  # 删除指定索引的元素
del peoples[-1]
print(peoples)

# 删除指定值的列表元素
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peoples.remove('people05')  # 删除指定值的元素(第一个指定的值)
print(peoples)

# 使用栈的方式访问并删除列表
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
peopleDelete = peoples.pop()  # 弹出最后一个元素，栈的概念
print(peopleDelete)
print(peoples)

# 增加列表对年龄连续输入的存储
ageList = []
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
                        ageList.append(intAge)
                        print("已经输入的年龄列表为：")
                        print(ageList)

