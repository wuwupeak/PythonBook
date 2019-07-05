# 使用循环构建数值列表1-100
numbers = []
for value in range(1, 101):
        numbers.append(value)
print(numbers)

# 列表推导式构建数值列表1-100
numbers = [number for number in range(1, 101)]  # 列表的构造器，切记使用[]一旦使用()就成了生成器
print(numbers)

# 使用循环构建偶数数值列表1-100
evenNumbers = []
for value in range(1, 101):
        if value % 2 == 0:
                evenNumbers.append(value)
print(evenNumbers)

# 带条件的列表推导式构建偶数数值列表1-100
evenNumbers = [number for number in range(1, 101) if number % 2 == 0]  # 带条件的列表的构造器，输出1-100内的偶数
print(evenNumbers)
# 表达式 for 变量 in 列表 if 条件

# 带条件的列表推导式案例
oddNumbers = [number for number in range(1, 101) if number % 2 != 0]  # 带条件的列表的构造器，输出1-100内的偶数
print(oddNumbers)
evenNumbers = [number for number in range(1, 101) if number % 2 == 0 if number > 49]  # 带多个条件的列表推导式
print(evenNumbers)

# 使用循环对列表值进行计算
numbers = []
for value in range(1,6):
        numbers.append(value)
numberCal = []
for number in numbers:
        numberCal.append(number**2)
print(numberCal)

# 带计算的列表推导式对列表值进行计算
numbers = [value**2 for value in range(1, 6)]  
# 使用值计算建立列表,更精简的方法,6行代码缩减为一行
# 这种写法除了更加高效之外，也更加简短，涉及的语法元素也更少。
# 在大型程序中，这意味着更少的错误，代码也更容易阅读和理解。
print(numbers)
# 表达式 for 变量 in 列表

# 使用多个列表的推导式
names = ['高等数学', '计算机网络基础', '大学英语', 'Python编程基础', 'Linux操作系统基础']
scores = ['一班', '二班',  '三班']
nameScores = [(name, score) for name in names for score in scores]
print(nameScores)