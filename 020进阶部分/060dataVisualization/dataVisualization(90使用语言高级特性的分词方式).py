import os
import wordsAnalysisFunction as wordsProcess
fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/wordsAnalysis.txt'
print(fileFolderPath)

wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsUniqueSet = set(wordsCleaned) #利用set中元素唯一性的特点，保留了列表中唯一的单词
wordsUniqueList = list(wordsUniqueSet)
# words = nltk.text.Text(cotent)
print(len(wordsCleaned))
print(len(wordsUniqueSet))
print(len(wordsUniqueList))

wordsFrequencyDic = {word : wordsCleaned.count(word) for word in wordsUniqueList} #此处使用了字典推导式
print(wordsFrequencyDic)
print(len(wordsFrequencyDic))