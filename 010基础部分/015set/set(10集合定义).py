# 集合是许多唯一对象的聚集
# 集合是一种鲁棒性很好的数据结构，当元素顺序的重要性不如元素的唯一性和测试元素是否包含在集合中的效率时，大部分情况下这种数据结构是很有用的。
listOne = [1, 1, 2, 3, 3, 4]
print(set(listOne))
listTwo = list(set(listOne))
print(listTwo)
