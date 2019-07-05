import re #导入正则表达式处理模块re
def wordMatch(wordForClean): #定义单个分词的清洗
        # wordRE = re.compile(r"[‘,“,(]*([a-z]{1,20})")
        wordRE = re.compile(r"[^a-z]*([a-z]{1,20})")
        matchObject = re.match(wordRE,wordForClean)
        return matchObject

def wordsClean(textForDivide): #定义单词列表的清洗
        wordsForClean = textForDivide.split()
        wordsCleaned = []
        for wordForClean in wordsForClean:
                matchObject = wordMatch(wordForClean.lower()) #全部转成小写的处理
                if matchObject:
                        wordsCleaned.append(matchObject.group(1))
        return wordsCleaned

def textDivide(fileFullPath): #定义拆分单词的函数
        wordsCleaned = []
        with open(fileFullPath,'r',encoding='UTF-8') as fileObject:
                contents = fileObject.read()
                wordsCleaned = wordsClean(contents)
        return wordsCleaned
                
def analyzeWordsCount (wordsCleaned,minCount): #定义基本的统计函数
        wordsUnique = []
        wordsCount = {}
        for word in wordsCleaned:
                if word not in wordsUnique:
                        wordsUnique.append(word)
        for wordUnique in wordsUnique:
                wordCount = wordsCleaned.count(wordUnique)
                if wordCount >= minCount: #此处利用参数来选择最小的词频
                        wordsCount[wordUnique] = wordCount
        wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #使用该排序将字典变成有序的元组
        wordsCountDict = dict(wordsCountOrder) #将有序的元组转换为字典
        return wordsCountDict #返回字典