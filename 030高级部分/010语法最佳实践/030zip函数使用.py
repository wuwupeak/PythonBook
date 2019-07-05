#1.1 zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
namesList = ['周杰伦','李健','谢霆锋','庾澄庆']
ageList = [40,45,46,53]
zipped = zip(namesList,ageList)
for zipedTuple in zipped:
    print(zipedTuple)

#1.2 对两个大小相等的可迭代对象进行均匀遍历时，使用zip函数是一种常用模式
namesList = ['周杰伦','李健','谢霆锋','庾澄庆']
ageList = [40,45,46,53]
for zipedTuple in zip(namesList,ageList):
    print(zipedTuple)