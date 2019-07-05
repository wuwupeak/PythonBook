#一个原始的除法器
numberOne = input('请输入分子：')
numberTwo = float(input('请输入分母：'))
result = numberOne/numberTwo
print('分子 ' + str(numberOne) + '除以分母 '+ str(numberTwo) + '的结果为:' + str(result))

#带异常检测的除法器
try:
    numberOne = float(input('请输入分子：'))
    numberTwo = float(input('请输入分母：')) 
    result = numberOne/numberTwo
except:
    print('用户输入错误!')
else:
    print('分子 ' + str(numberOne) + '除以分母 '+ str(numberTwo) + '的结果为:' + str(result))

#可以连续输入带异常检测的除法器
active = True
while active:
    try:
        numberOne = input('请输入分子：')
        if numberOne == 'exit':
            break
        else:
            numberOneFloat = float(numberOne)
        numberTwo = input('请输入分母：')
        if numberTwo == 'exit':
            break
        else:
            numberTwoFloat = float(numberTwo)
        result = numberOneFloat/numberTwoFloat
    except:
        print('用户输入错误!')
    else:
        print('分子 ' + str(numberOne) + '除以分母 '+ str(numberTwo) + '的结果为:' + str(result))


#可以连续输入带异常检测的除法器
active = True
numberOne = ''
numberTwo = ''
exitSig = 'exit'
while active:
    if numberOne == exitSig or numberTwo == exitSig:
        break
    else:
        while True:
            numberOne = input('请输入分子：')
            if numberOne == exitSig:
                break
            else:
                try:
                    numberOneFloat = float(numberOne)
                except ValueError:
                    print('输入数据类型不是数字')
                else:                
                    break 
        while True and numberOne != exitSig:
            numberTwo = input('请输入分母：')
            if numberTwo == exitSig:
                break
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
        

#可以连续输入带异常检测的除法器,改进的代码,去掉了一个if判断和一个循环
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


    


