#reduce的使用：reduce(function, iterable[, initializer])
#reduce()函数把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。

from functools import reduce
#1.1 使用reduce函数典型代码
def add(numberOne, numberTwo):
    return numberOne + numberTwo

def muliply(numberOne, numberTwo):
    return numberOne * numberTwo

numberList = [number for number in range(1,6)]
print(numberList)

numberAdd = reduce(add, numberList)
print(numberAdd)

numberMul = reduce(muliply, numberList)
print(numberMul)

#1.2 使用reduce函数与匿名函数的结合
numberList = [number for number in range(1,11)]
print(numberList)

#使用reduce函数对单个列表的相加操作
numberAdd = reduce( lambda numberOne, numberTwo : numberOne + numberTwo , numberList) 
print(numberAdd)

#使用reduce函数对单个列表的相乘操作
numberMul = reduce( lambda numberOne, numberTwo : numberOne * numberTwo , numberList) 
print(numberMul)
