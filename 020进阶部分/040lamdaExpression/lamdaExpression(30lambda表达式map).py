# lamda 表达式对列表的处理，map
number = [x for x in range(1,101)] #列表的推导式
doubleNumber = list(map(lambda x : x*2 , number)) #使用lambda对原有列表中"每一个"元素进行处理
print(doubleNumber)
numberTwo = [x for x in range(101,201)] #列表的推导式
addNumberList = list(map(lambda x,y: x+y , number, numberTwo)) #使用lambda对元素数量相同的两个列表中"每一个"元素进行处理
print(addNumberList)


# lamda 表达式也可以用列表推导式来完成同样的功能
doubleNumber = [x*2 for x in range(1,101)]  #列表推导式的代码更简洁 doubleNumber = list(map(lambda x : x*2 , number))
print(doubleNumber)

#列表推导式不同的地方
doubleNumber = [x*2 for x in range(1,101)]  #列表推导式的代码更简洁 doubleNumber = list(map(lambda x : x*2 , number))
numberTwo = [x for x in range(101,201)] 
addnumber = [x+y for x in doubleNumber for y in numberTwo] #这个列表推导式不能代替上面的lambda
print(addnumber)
print (dict([(x,y) for x in doubleNumber for y in numberTwo])) #使用这个字典显示了addnumber = [x+y for x in doubleNumber for y in numberTwo]的计算过程


