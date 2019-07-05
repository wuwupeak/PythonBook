# 1.1for循环语句和range()函数实现指定次数的循环
# for关键字；
# 一个变量名；
# in关键字；
# 调用range()方法，最多传入3个参数；
# 冒号；
# 从下一行开始，缩退的代码块（称为for子句）。
for value in range(5):
        print("value的值是：" + str(value))

# 等价的while循环
value = 0
while value < 5:
        print("value的值是：" + str(value))
        value = value + 1

# 1.2 range()函数可以有三个参数.
# 前两个参数分别是起始值和终止值，第三个参数是“步长”。
# 步长是每次迭代后循环变量增加的值。
for value in range(2, 5):
        print("value的值是：" + str(value))

for value in range(100, 200, 2):
        print("value的值是：" + str(value))

for value in range(200, 100, -2):
        print("value的值是：" + str(value))
