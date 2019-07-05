#iterable: 可迭代的; 可重复的; 迭代的
#map的使用：map(function, iterable, ...)
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

numberList = [number for number in range(1,11)]
print(numberList)

#1.1 使用for循环来处理列表元素值翻倍
numberProcessList = []
for number in numberList:
        numberProcess = number * 2
        numberProcessList.append(numberProcess)
print(numberProcessList)


#1.2 使用map函数来处理列表元素值翻倍
def multiply(number):
    return number * 2

numberProcessList = list(map(multiply, numberList))
print(numberProcessList)

# 使用map函数来计算球体体积
import math
def volumeSphere(radius):
    return round(4 * math.pi * radius**3/3, 2) #python是以双精度(64)位来保存浮点数，多余的位会被截掉,使用round来定义小数位数的精度

volumeSphereList = list(map(volumeSphere, numberList))
print(volumeSphereList)

#1.3 使用map函数与匿名函数结合来处理列表元素值翻倍
numberProcessList = list( map( lambda number : number  * 2 , numberList) )
print(numberProcessList)

# 使用map函数与匿名函数结合来计算球体体积
volumeSphereList = list(map(lambda radius :  round(4 * math.pi * radius**3/3, 2), numberList))
print(volumeSphereList)

#1.4 使用列表推导式来处理列表元素值翻倍
numberProcessList = [number*2 for number in numberList]
print(numberProcessList)

#1.5 对多个列表的操作的传统方式与使用map方式的比较
numberOneList = [number for number in range(1,11)]
numberTwolist = list( map( lambda number : round(number * 0.1, 1), numberOneList ) ) 
numberThreeList = list( map( lambda number : number * 10, numberOneList ) )

#传统方式
numberSumList = []
for index in (range(len(numberOneList))): #使用列表长度来进行索引的控制
        numberSum = numberOneList[index] + numberTwolist[index] + numberThreeList[index]
        numberSumList.append(numberSum)
print(numberSumList)

#使用map函数的方式
numberSumList =  list(map( lambda numberOne, numberTwo, numberThree : numberOne + numberTwo + numberThree, numberOneList, numberTwolist, numberThreeList ))
print(numberSumList)

