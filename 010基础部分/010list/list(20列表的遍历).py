# 对字符串每个字母的遍历
valueString = 'Hello, world!'  # 注意空格也是一个字符
for value in valueString:
        print(value)

valueString = '来啦老弟'  # 注意空格也是一个字符
for value in valueString:
        print(value)


# 列表的遍历
peoples = ['people01', 'people02', 'people03', 'people04', 'people05', 'people06', 'people07', 'people08','people09', 'people10']
for people in peoples:  # 遍历列表
        print(people)

# 更友好的遍历输出
for people in peoples:  # 遍历列表
        print('目前遍历到的元素值是:'+people)
print("列表的元素总数是:" + str(len(peoples)) + '个')

