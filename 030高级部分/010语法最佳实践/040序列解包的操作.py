#1.1 序列解包（sequence unpacking）。这种方法并不限于列表和元组，而是适用于任意序列类型（甚至包括字符串和字节序列）。
# 只要赋值运算符左边的变量数目与序列中的元素数目相等，你都可以用这种方法将元素序列解包到另一组变量中。
first,second,third = '小明','小李','小江'
print(first,second,third)

#1.2 解包还可以利用带星号的表达式获取单个变量中的多个元素，只要它的解释没有歧义即可。
first,second,third,*rest = '小明','小李','小江','小赵','小钱','小孙'
print(first,second,third,rest)

first,*inner,last = '小明','小李','小江','小赵','小钱','小孙'
print(first,inner,last)

#1.3 对嵌套序列进行解包。特别是在遍历由序列构成的复杂数据结构时，这种方法非常实用。
(a, b), (c, d) = (1, 2), (3, 4)
print(a,b,c,d)