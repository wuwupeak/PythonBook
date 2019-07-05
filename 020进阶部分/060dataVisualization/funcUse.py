#使用函数封装对文件的读取、分词、清理及统计词频的功能
import funcWordsProcess
fileName = "\\wordsAnalysis.txt"
fileContent = funcWordsProcess.fileRead(fileName)
wordsCleaned = funcWordsProcess.fileClean(fileContent)
wordsUnique = funcWordsProcess.fileWordsUnique(wordsCleaned)
wordsCountDict = funcWordsProcess.fileWordsCount(wordsCleaned,wordsUnique)

help(funcWordsProcess.fileRead) #该代码查看函数的文档内容

#使用模块中函数封装后的函数
wordsCountDict = funcWordsProcess.fileWordsCountForEN(fileName)
print(wordsCountDict)
print(len(wordsCountDict))

#使用封装的函数完成直方图和词云的可视化表达
import funcWordsProcess
import funcWordsCountVisualization
fileName = "\\wordsAnalysis.txt"
wordsCountDict = funcWordsProcess.fileWordsCountForEN(fileName)
funcWordsCountVisualization.drawWordsCountBar(wordsCountDict)
funcWordsCountVisualization.drawWordsCountCloud(wordsCountDict)
