# 1.1 hello world程序，字符串类型
# Python会忽略注释，你可以用它们来写程序注解，或提醒自己代码试图完成的事。
# 这一行中，#标志之后的所有文本都是注释。
print('Hello world!') 
print("Hello world!")
# 1101 这是一个字符串类型str
# 所有用单引号（'）、双引号（"）或成组的3个引号（单引号或双引号）包围且没有前缀的值都表示str数据类型：
# 1102 print是python的内置输出函数。
# 1103代码行print('Hello world!')表示“打印出字符串'Hello world!'的文本”。
# Python执行到这行时，你告诉Python调用print()函数，并将字符串“传递”给函数。
# 传递给函数的值称为“参数”。
# 请注意，引号没有打印在屏幕上。它们只是表示字符串的起止，不是字符串的一部分。

# 1.2 数值计算，整数型和浮点类型
print(2+2)  # 整数相加
print(-2+2)  # 整数相加
print(4-2)  # 整数相减
print(4*2)  # 整数相乘
print(4/2)  # 整数相除，结果出现了不一样，因为整数相除的结果是一个浮点类型的结果
# 1201 整型（或int）数据类型表明值是正负整数
# 1202 带有小数点的数据类型，如3.14，称为“浮点型”（或float）
print(12.51 + 11.37)
print(12.5 + 11.37)
# 1203 浮点数的计算精度问题
# 这是因为小数以二进制形式表示时的有穷性导致的。
# 我们知道，将一个小数转化为二进制表示的方式是，不断的乘2，取其中的整数部分。例如：
# (1) 0.625*2 = 1.25, 整数部分为1，小数部分为0.25 
# (2) 0.25 * 2 = 0.5 , 整数部分为0，小数部分为0.5 
# (3) 0.5 * 2 = 1 , 整数部分为1，小数部分为0 
# 所以0.625的二进制表示就是0.101。
# 然而有些小数，例如0.4，并不能够精确的转化为二进制表示，用上面的这种方法计算：
# (1) 0.4*2=0.8 整数部分为0，小数部分为0.8 
# (2) 0.8*2=1.6 整数部分为1，小数部分为0.6 
# (3) 0.6*2=1.2 整数部分为1，小数部分为0.2 
# (4) 0.2*2=0.4 整数部分为0，小数部分为0.4 
# (5) 0.4*2=0.8 整数部分为0，小数部分为0.8
# (6) 0.8*2=1.6 整数部分为1，小数部分为0.6 
# (7) 0.6*2=1.2 整数部分为1，小数部分为0.2 
# 所以0.4转化为二进制，应该是0.0110... 这样一个无限循环小数。
# 计算机的内存、cpu寄存器等等这些硬件单元都是有限的，只能表示有限位数的二进制位，因此存储的二进制小数就会和实际转换而成的二进制数有一定的误差。
# 这个不是python 的问题，所有基于二进制的浮点数都会有这个问题
# 原因在于大部分浮点数转换为二进制后都是无限循环小数，而浮点数不可能用无限大的内存来储存，所以会有舍入的误差。
# 所以在python中不建议直接将两个浮点数进行大小比较，或者做精确的计算，往往会得到意想不到的结果。

# 1.3 字符串计算 仅支持加法和乘法运算
print('Hello' + 'world')  # 输出会很难看，因为字会连在一起
print('Hello' + ' ' + 'world')  # 输出会很难看，因为字会连在一起
print('Hello ' * 3)  # 使用字符串乘法将字符串复制三次

# 1.4 字符串类型与整数和浮点型不能做运算
print('Hello world!' + 12)
# 1401 引发 发生异常: TypeError，异常是程序书写不符合运算或者语法导致的