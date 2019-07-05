keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}

active =True
while active:
    nameInput = input('please input name:')
    if nameInput == 'exit':
        active = False
    else:
        keyFind = 0
        for key,name in keyNameDict.items():
            if name == nameInput: #用户输入的名字与keyNameDict中的值相等则执行下面的代码
                keyFind = key
        if keyFind == 0:
            print('no find!')
        else:
            print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind])) #将keyNameDict的键直接用作keyScoreDict的键来获取对应的值

















# keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
# keyScoreDict = {10001:71,10002:77,10003:99}

# keyFind = 0 #使用该标志位来代表是否根据name找到key
# nameInput = input('please input name:')
# for key,name in keyNameDict.items():
#     if name == nameInput:
#         keyFind = key #找到key则使用key来替换标志位
# if keyFind == 0: #根据标志位的变化来决定输出
#     print('no find')
# else:
#     print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind]))
