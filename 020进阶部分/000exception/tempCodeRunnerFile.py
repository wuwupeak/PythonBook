#可以连续输入带异常检测的除法器,改进的代码
active = True
numberOne = ''
numberTwo = ''
exitSig = 'exit'
while active:   
    numberOne = input('请输入分子：')
    if numberOne == exitSig:
        active = False
    else:
        try:
            numberOneFloat = float(numberOne)
        except ValueError:
            print('输入数据类型不是数字')
            continue
        else:                
            while active :
                numberTwo = input('请输入分母：')
                if numberTwo == exitSig:
                    active = False
                else:
                    try:
                        numberTwoFloat = float(numberTwo)
                        result = numberOneFloat/numberTwoFloat
                        print('分子 ' + str(numberOne) + '除以分母 '+ str(numberTwo) + '的结果为:' + str(result))
                    except ValueError:
                        print('输入数据类型不是数字')
                    except ZeroDivisionError:
                        print('分母不能为零！')
                    else:
                        break