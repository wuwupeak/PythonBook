#该函数封装了使用名字查找学号的功能
def findKey(keyNameDict,nameInput):
    for key,name in keyNameDict.items():
        if name == nameInput:
            return key
    return 0

#该函数封装了使用学号找到成绩的功能
def findScore(keyScoreDict,keyFind):
    if keyFind == 0:
        return -1
    else:
        return keyScoreDict[keyFind]

#该函数使用用户输入的名字和查找到的成绩形成输出的功能
def findResult(nameInput,result):
    if result == -1:
        print('no find')
    else:
        print("find "+ nameInput +"'s " +"score is "+str(result))