# 1.4 重新看分词的匹配
import re
fileFullPath = './pythonStudy/020进阶部分/030wordsAnalysis/wordsAnalysis.txt'
wordRE = re.compile(r"([^a-z,^A-Z]{1,3})") #将分词后的特殊字符拿出来建立列表
wordsAbnomal = []
with open(fileFullPath,'r',encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        words = contents.split()
        for word in words:
                matchObject = re.match(wordRE,word)
                if matchObject:
                        if matchObject.group(1) not in wordsAbnomal:
                                wordsAbnomal.append(matchObject.group(1))
print(wordsAbnomal)

# 改进的re分词处理
import re
fileFullPath = './pythonStudy/020进阶部分/030wordsAnalysis/wordsAnalysis.txt'
wordRE = re.compile(r"[^a-z]*([a-z]{1,20})") 
wordsCleaned = []
with open(fileFullPath,'r',encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        words = contents.split()
        for word in words:
                matchObject = re.match(wordRE,word)
                if matchObject:
                        if matchObject.group(1) not in wordsCleaned:
                                wordsCleaned.append(matchObject.group(1))
print(wordsCleaned)