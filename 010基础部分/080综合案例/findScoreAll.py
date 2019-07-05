import findScore

def findScoreAll(keyNameDict,keyScoreDict,nameInput):
         keyFind = findScore.findKey(keyNameDict,nameInput)
         result = findScore.findScore(keyScoreDict,keyFind)
         findScore.findResult(nameInput,result)

def findScoreSame(keyNameDict,keyScoreDict,nameInput):
        findScore.findResult(nameInput,findScore.findScore(keyScoreDict,findScore.findKey(keyNameDict,nameInput)))