#1.1 “布尔”数据类型
boolType = True
print(boolType)
boolType = False
print(boolType)
# 1101 虽然整型、浮点型和字符串数据类型有无数种可能的值，但“布尔”数据类型只有两种值：True和False。
# Boolean（布尔）的首字母大写，因为这个数据类型是根据数学家George Boole命名的。
# 在作为Python代码输入时，布尔值True和False不像字符串，两边没有引号，它们总是以大写字母T或F开头，后面的字母小写。

# 1.2 比较操作符
print(2 == 2)
print(2 == 3)
print('yes' == 'yes')
print('Yes' == 'yes')

boolType = 2 != 2
print(boolType)
print(2 != 3)
print('yes' != 'yes')
print('Yes' != 'yes')
# 如果两边的值一样，==（等于）求值为True。如果两边的值不同求值为False。
# ==和!=操作符实际上可以用于所有数据类型的值。
# 整型或浮点型的值永远不会与字符串相等。表达式42 == '42'求值为False是因为，Python认为整数42与字符串'42'不同。

print(2 >= 2)
print(2 <= 3)

print(2 > 2)
print(2 < 3)
# <、>、<=和>=操作符仅用于整型和浮点型值

# 1.3 逻辑运算符
result = True and True
print(result)
result = True and False
print(result)
result = False and False
print(result)
# 1301 如果两个布尔值都为True，and操作符就将表达式求值为True，否则求值为False。

result = True or True
print(result)
result = True or False
print(result)
result = False or False
print(result)
# 1302 只要有一个布尔值为真，or操作符就将表达式求值为True。如果都是False，所求值为False。

result = not True
print(result)
result = not False
print(result)
# 1303 和and和or不同，not操作符只作用于一个布尔值（或表达式）。not操作符求值为相反的布尔值。

