# 集合是许多唯一对象的聚集
# 集合是一种鲁棒性很好的数据结构，当元素顺序的重要性不如元素的唯一性和测试元素是否包含在集合中的效率时，大部分情况下这种数据结构是很有用的。
listOne = [1, 1, 2, 3, 3, 4]
print(set(listOne))
listTwo = list(set(listOne))
print(listTwo)


listOne = ['常州', '常州', '盐城', '徐州', '苏州', '苏州']
listTwo = ['常州', '南京', '台州', '苏州', '苏州']





# 使用set对列表的快速处理方法
setOne = set(listOne)
setTwo = set(listTwo)
setCross = setOne & setTwo
setAll = setOne | setTwo
setOneUnique = setOne - setTwo
setTwoUnique = setTwo - setOne

print(setCross)
print(setAll)
print(setOneUnique)
print(setTwoUnique)