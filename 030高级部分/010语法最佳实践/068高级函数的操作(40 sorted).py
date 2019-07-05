#使用sorted函数的典型用法
numbers = [5,7,-6,3,4,1,2,-60]
numbersSorted = sorted(numbers)
print(numbersSorted)
numbersSorted = sorted(numbers,reverse = True)
print(numbersSorted)

strings = ['cake','apple','Good','book','test','Air']
stringsSorted= sorted(strings)
print(stringsSorted)
stringsSorted= sorted(strings, reverse = True)
print(stringsSorted)

#使用key参数的sorted函数用法
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
numbers = [5,7,-6,3,4,1,2,-60]
numbersSorted = sorted(numbers, key = abs)
print(numbersSorted)
numbersSorted = sorted(numbers , key = abs, reverse = True)
print(numbersSorted)

strings = ['cake','apple','Good','book','test','Air']
stringsSorted= sorted(strings, key = str.lower)
print(stringsSorted)
stringsSorted= sorted(strings, key = str.lower, reverse = True)
print(stringsSorted)
