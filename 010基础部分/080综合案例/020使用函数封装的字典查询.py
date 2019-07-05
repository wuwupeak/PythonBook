#使用函数封装相应的查找和输出功能
import findScore
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}

Active = True
while Active:
    nameInput = input('please input name:')
    if nameInput == 'exit':
        Active = False
    else:
        keyFind = findScore.findKey(keyNameDict,nameInput)
        result = findScore.findScore(keyScoreDict,keyFind)
        findScore.findResult(nameInput,result)

#使用对函数再次进行封装的函数
import findScoreAll
keyNameDict = {10001:'zhangsan',10002:'lisi',10003:'wangwu'}
keyScoreDict = {10001:71,10002:77,10003:99}
Active = True
while Active:
    nameInput = input('please input name:')
    if nameInput == 'exit':
        Active = False
    else:
        findScoreAll.findScoreAll(keyNameDict,keyScoreDict,nameInput)
        findScoreAll.findScoreSame(keyNameDict,keyScoreDict,nameInput)
