# #可以连续输入带异常检测的除法器
# exitSig = 'exit'
# while True:
#     try:
#         #-----------------------------------
#         numberOne = input('请输入分子：')
#         if numberOne == exitSig:
#             break
#         else:
#             numberOneFloat = float(numberOne)
#         #------------------------------------
#         numberTwo = input('请输入分母：')
#         if numberTwo == exitSig:
#             break
#         else:
#             numberTwoFloat = float(numberTwo)
#         #------------------------------------
#         result = numberOneFloat/numberTwoFloat
#     except:
#         print('用户输入错误!')
#     else:
#         print('分子 ' + str(numberOne) + '除以分母 '+ str(numberTwo) + '的结果为:' + str(result))




active = True
numberOne = ''
numberTwo = ''
exitSig = 'exit'
while active:   
    numberOne = input('请输入分子：')
    if numberOne == exitSig:
        break
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