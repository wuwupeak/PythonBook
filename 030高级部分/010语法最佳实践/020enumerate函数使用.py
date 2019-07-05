#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#enumerate: 列举，枚举，数

#1.1 获取列表索引的低效做法
index = 0 
namesList = ['周杰伦','李健','谢霆锋','庾澄庆']
for name in namesList:
    print(index,name)
    index = index + 1

#1.2 使用enumerate获取列表索引的高效做法
namesList = ['周杰伦','李健','谢霆锋','庾澄庆']
for index, name in enumerate(namesList):
    print(index,name)

#1.3 使用enumerate直接获取索引和列表值
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonsList= list(enumerate(seasons))
print(seasonsList)

#1.3 使用enumerate直接获取索引和列表值
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonsList = list(enumerate(seasons,1)) #使用第二个参数控制索引的开始
seasonsDict = dict (enumerate(seasons,1))
print(seasonsList)
print(seasonsDict)

