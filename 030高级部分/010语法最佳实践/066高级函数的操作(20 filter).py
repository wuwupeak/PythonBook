#filter的使用：filter(function, iterable)
#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


numberList = [number for number in range(1,11)]
print(numberList)
#1.1 使用for循环来实现列表的奇数过滤
numberOddList = []
for number in numberList:
        if (number%2 == 1):
                numberOddList.append(number)
print(numberOddList)

#1.2 使用filter函数来实现列表的奇数过滤
def isOdd(number):
    return number % 2 == 1
numberOddList= list(filter(isOdd, numberList))
print(numberOddList)

#1.3 使用filter函数与匿名函数相结合的奇数过滤
numberOddList = list(filter(lambda number : number%2 == 1, numberList))
print(numberOddList)

#1.4 不能直接使用类表推到式的处理
numberOddList = [number%2 == 1 for number in numberList]
print(numberOddList)

elementList = ['A', '', 'B', 'd ', 'C', '    good']
#使用filter和map函数结合对字符串进行清洗
def elementStrip(element):
        return element.strip()

def isEmpty(element):
        if len(element) == 0:
                return False
        return True

elementsStripList = list(map(elementStrip, elementList))
elementsCleanList = list(filter(isEmpty, elementsStripList))
print(elementsCleanList)


#使用filter函数、map函数与匿名函数的例子
elementsStripList = list(map(lambda element:element.strip(), elementList))
print(elementsStripList)
elementsCleanList = list(filter(lambda element: len(element) != 0, elementsStripList))
print(elementsCleanList)


#不推荐的写法，该写法会导致可读性极差
elementsCleanList = list(filter(lambda element: len(element) != 0, list(map(lambda element:element.strip(), elementList))))
print(elementsCleanList)

