#1.5 对多个列表的操作的传统方式与使用map方式的比较
numberOneList = [number for number in range(1,11)]
numberTwolist = list( map( lambda number : round(number * 0.1, 1), numberOneList ) ) #python是以双精度(64)位来保存浮点数，多余的位会被截掉，不使用round看到的是0.1
numberThreeList = list( map( lambda number : number * 10, numberOneList ) )

#对多个列表相同位置元素的相加操作的传统方式
numberSumList = []
for index in (range(len(numberOneList))): #使用列表长度来进行索引的控制
        numberSum = numberOneList[index] + numberTwolist[index] + numberThreeList[index]
        numberList.append(numberSum)
print(numberSumList)

#使用map函数对多个列表相同位置元素的相加操作
numberSumList =  list(map( lambda numberOne, numberTwo, numberThree : numberOne + numberTwo + numberThree, numberOneList, numberTwolist, numberThreeList ))
print(numberSumList)