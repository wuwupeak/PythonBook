#1.1 使用字典推导具有与列表推导相同的优点。
# 因此在许多情况下，字典推导要更加高效、更加简短、更加整洁。
# 对于更复杂的代码而言，需要用到许多if语句或函数调用来创建一个字典，这时最好使用简单的for循环，尤其是它还提高了可读性。
squares = {number : number**2 for number in range(5)}
print(squares)

squares = {str(number) : number**2 for number in range(5)}
print(squares)

#1.2 使用Python标准库的collections模块提供了名为OrderedDict的有序字典。
from collections import OrderedDict
squares = OrderedDict((str(number),number) for number in range(5))
print(squares)
print(squares.keys())

<<<<<<< HEAD
#1.3 对字典的排序
testDict = {'b':3,'a':4,'d':1,'c':2}
testDictOrdered = sorted(testDict.items(),key = lambda x:x[0],reverse = True)
print(testDictOrdered)
testDictOrdered = sorted(testDict.items(),key = lambda x:x[1],reverse = True)
print(testDictOrdered)
=======
#1.3 使用sorted函数对字典进行排序
fruitDict = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
orderByFruit = OrderedDict(sorted(fruitDict.items(), key = lambda item:item[0]))
orderByNumber = OrderedDict(sorted(fruitDict.items(), key = lambda item:item[1]))
print(orderByFruit)
print(orderByNumber)

#1.4 使用sorted函数对字典进行逆排序
fruitDict = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
orderByFruit = OrderedDict(sorted(fruitDict.items(), key = lambda item:item[0]), reversed = True)
orderByNumber = OrderedDict(sorted(fruitDict.items(), key = lambda item:item[1]), reversed = True)
print(orderByFruit)
print(orderByNumber)
>>>>>>> 863484d0d739c62ed98baf1d5535d474c5faa24c
