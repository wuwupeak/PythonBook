# 1.1 异常的发生
numerator = float(input('请输入分子：')) #输入非数字型值会引发异常
denumerator = float(input('请输入分母：'))  #输入非数字型值会引发异常，0也会引发异常
result = numerator/denumerator
print('分子' + str(numerator) + '分母' + str(denumerator) +  '的结果为：' + str(result) )

# 1.2 异常的基本处理
try:
        numerator = float(input('请输入分子：')) #输入非数字型值会引发异常
        denumerator = float(input('请输入分母：'))  #输入非数字型值会引发异常，0也会引发异常
        result = numerator/denumerator
except ValueError: #输入非数字型值会引发异常
        print('输入的数据不是数字型引发异常！！！')
except ZeroDivisionError: #分母输入0引发异常
        print('分母为零引发异常！！！')
else:
        print('分子' + str(numerator) + '分母' + str(denumerator) +  '的结果为：' + str(result) )


