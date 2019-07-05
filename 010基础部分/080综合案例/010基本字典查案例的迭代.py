#本案例主要目标为根据输入的名字，通过主键关联来找到对应的成绩

#查找的基本算法
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
nameInput = input('please input name:')
for key,name in keyNameDict.items():
    if name == nameInput: #用户输入的名字与keyNameDict中的值相等则执行下面的代码
        print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[key ])) #将keyNameDict的键直接用作keyScoreDict的键来获取对应的值

#增加针对查找不到数据的处理
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
keyFind = 0 #使用该标志位来代表是否根据name找到key
nameInput = input('please input name:')
for key,name in keyNameDict.items():
    if name == nameInput:
        keyFind = key #找到key则使用key来替换标志位
if keyFind == 0: #根据标志位的变化来决定输出
    print('no find')
else:
    print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind]))

#增加用户连续输入提高易用性的处理
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
Active = True #使用该标志位来进行程序的循环
while Active:
    keyFind = 0
    nameInput = input('please input name:')
    for key,name in keyNameDict.items():
        if name == nameInput:
            keyFind = key 
    if keyFind == 0:
        print('no find')
    else:
        print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind]))


#根据输入条件结束程序
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
Active = True
while Active:
    keyFind = 0
    nameInput = input('please input name:')
    if nameInput == 'exit': #使用特定的输入来改变循环的执行条件
        Active = False
    else:
        for key,name in keyNameDict.items():
            if name == nameInput:
                keyFind = key 
        if keyFind == 0:
            print('no find')
        else:
            print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind]))

#一旦查找到姓名对应的键值，处理后就跳出循环
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
Active = True
while Active:
    keyFind = 0
    nameInput = input('please input name:')
    if nameInput == 'exit': #使用特定的输入来改变循环的执行条件
        Active = False
    else:
        for key,name in keyNameDict.items():
            if name == nameInput:
                keyFind = key 
                break #一旦查找到主键，处理后使用break跳出循环
        if keyFind == 0:
            print('no find')
        else:
            print("find "+ nameInput +"'s " +"score is "+str(keyScoreDict[keyFind]))

