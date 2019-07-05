# 集合的交集---取两个集合的共有部分
setOne = set(list(range(1, 8)))
setTwo = set(list(range(5, 15)))
print(setOne)
print(setTwo)
setThree = setOne & setTwo
print(setThree)

# 集合的并集--取两个集合所有
setOne = set(list(range(1, 8)))
setTwo = set(list(range(5, 15)))
print(setOne)
print(setTwo)
setThree = setOne | setTwo
print(setThree)

# 集合的差集--取一个集合与另一个集合的不同部分
setOne = set(list(range(1, 8)))
setTwo = set(list(range(5, 15)))
print(setOne)
print(setTwo)
setThree = setOne-setTwo
print(setThree)
setThree = setTwo-setOne
print(setThree)


listOne = ['常州', '常州', '盐城', '徐州', '苏州', '苏州']
listTwo = ['常州', '南京', '台州', '苏州', '苏州']

## 获取列表中相同元素的传统做法
# listCross = []
# for one in listOne:
#     if one in listTwo:
#         listCross.append(one)
# print(listCross)
# setCross = set(listCross)
# listCross = list(setCross)
# print(listCross)



## 获取不同列表中所有元素值的传统做法
# listAll = listTwo
# for one in listOne:
#     if one not in listTwo:
#         listAll.append(one)
# print(listAll)
# setAll = set(listAll)
# listAll = list(setAll)
# print(listAll)


# 使用set对列表的快速处理方法
setOne = set(listOne)
setTwo = set(listTwo)

setCross = setOne & setTwo
print(setCross)

setAll = setOne | setTwo
print(setAll)