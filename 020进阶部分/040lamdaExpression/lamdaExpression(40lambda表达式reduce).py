#1.4 lamda 表达式对列表的处理，reduce
from functools import reduce
number = [x for x in range(1,101)] #列表的推导式
sumNumber = reduce(lambda x,y : x+y , number) #使用lambda对原有列表中"每一个"元素进行"累计操作"
print("列表中所有数字的和是:" + str(sumNumber))