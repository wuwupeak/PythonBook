# 1.1 一个完整的除法计算器
while True:
        print('-----除法计算器，输入"q"就会停止计算。-----')
        numeratorInput = input('请输入分子：')
        if numeratorInput == 'q':
                break #使用break跳出循环体
        denumeratorInput = input('请输入分母：')
        if denumeratorInput == 'q':
                break
        try:
                numerator = float(numeratorInput) #输入非数字型值会引发异常
                denumerator = float(denumeratorInput)  #输入非数字型值会引发异常，0也会引发异常
                result = numerator/denumerator
        except ValueError: #输入非数字型值会引发异常
                print('输入的数据不是数字型引发异常！！！')
        except ZeroDivisionError: #分母输入0引发异常
                print('分母为零引发异常！！！')
        else:
                print('分子' + str(numerator) + '分母' + str(denumerator) +  '的结果为：' + str(result) )
                # print('分子{0}分母{1}的结果为：{2}'.format(str(numerator),str(denumerator),str(result))) #使用format函数占位显示
                # print('分子' + '{:g}'.format(numerator) + '分母' + '{:g}'.format(denumerator) +  '的结果为：' + '{:g}'.format(result))  #使用format函数去除小数点后面的0和不必要的.


# 1.2 一个完整的除法计算器[抓取所有异常]
while True:
        print('-----除法计算器，输入"q"就会停止计算。-----')
        numeratorInput = input('请输入分子：')
        if numeratorInput == 'q':
                break #使用break跳出循环体
        denumeratorInput = input('请输入分母：')
        if denumeratorInput == 'q':
                break
        try:
                numerator = float(numeratorInput) #输入非数字型值会引发异常
                denumerator = float(denumeratorInput)  #输入非数字型值会引发异常，0也会引发异常
                result = numerator/denumerator
        except Exception:
                print('请检查输入的是否是数字或分母是否为零！')
        else:
                print('分子' + str(numerator) + '分母' + str(denumerator) +  '的结果为：' + str(result) )