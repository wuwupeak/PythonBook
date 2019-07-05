import wordsProcess
import os
import csv
    
fileName = "\\wordsAnalysis.txt"
wordsCountDict = wordsProcess.fileWordsCountAll(fileName)

fileNameToWrite = '\\wordsResult.csv'
fileFolderDir = os.path.dirname(__file__) #使用os模块的函数拿到正在当前文件所在文件夹的绝对路径
fileFullPath = fileFolderDir + fileNameToWrite #使用字符串拼接，得到需要写入文件的绝对路径
with open(fileFullPath,'w',newline = '',encoding = 'utf-8') as csvObject:
    csvWriter = csv.writer(csvObject)
    for wordCount in wordsCountDict.items():
        csvWriter.writerow(wordCount)
