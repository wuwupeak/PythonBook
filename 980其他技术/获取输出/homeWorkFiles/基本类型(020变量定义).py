# 1.1 在变量(varible)中保存值
var = 'Hello world!'
print(var)

VAR = 'Hello china!'
print(VAR)
# 1101 “变量”就像计算机内存中的一个盒子，其中可以存放一个值。
# 用“赋值语句”将值保存在变量中。赋值语句包含一个变量名、一个等号（称为赋值操作符），以及要存储的值。

# 变量名只能包含字母、数字和下划线。
# 变量名不能以数字开头。
# 变量名是区分大小写的

# 1.2 变量的类型由存储的值来决定
var = 'Hello world!'
print(type(var))  # 使用type内置函数查看变量的类型，str是string的缩写，代表字符串类型
var = 4
print(type(var))  # 使用type内置函数查看变量的类型，int是integer的缩写，代表整数类型
var = 4.1
print(type(var))  # 使用type内置函数查看变量的类型，float代表浮点类型
# 1201 第一次存入一个值，变量就被“初始化”（或创建)
# 如果变量被赋了一个新值，老值就会在新值中被替代

# 1.3 变量存储计算的结果
varOne = 100
varTwo = 5
varResult = varOne / varTwo
print(varResult)
print(type(varResult))

varOne = "Hello"
varTwo = "World!"
varResult = varOne + " " + varTwo
print(varResult)
print(type(varResult))
# 1301 如果你的程序稍后将用到一个已求值的表达式的结果，就可以将它保存在一个变量中。