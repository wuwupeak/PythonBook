#1.2 lamda 表达式对列表的处理，filter
number = [x for x in range(1,101)] #列表的推导式
evenNumber = list(filter(lambda x : x%2 == 0 ,number)) #使用lambda获取原有列表中偶数
print(evenNumber)
filterNumber = list(filter(lambda x : x > 50 , number)) #使用lambda获取原有列表中大于50的数
print(filterNumber)

# 其实Python的for..in..if语法已经很强大，并且在易读上胜过了lambda。
number = [x for x in range(1,101)] #列表的推导式
oddNumber = list(filter(lambda x : x%2 != 0 ,number)) #使用filter获取100以内的奇数的例子
print(oddNumber)
oddNumber = [x for x in number if x % 2 != 0]
print(oddNumber)
