# 1.5 使用封装函数进行处理
import wordsAnalysisFunction as wordsProcess
fileFullPath = './pythonStudy/020进阶部分/030wordsAnalysis/wordsAnalysis.txt'

wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsCount = wordsProcess.analyzeWordsCount(wordsCleaned,1)
print(wordsCount)

for word,count in wordsCount.items():
        print('单词"{0}"出现在文章中的次数为{1}次。'.format(word,str(count)))


import os
import csv
fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/fileAnalysisUpper.csv' #按照csv格式进行写入，csv是标准数据处理格式
with open(fileFullPath,'w',newline = '') as csvFile:
        csvWrite = csv.writer(csvFile)
        for row in wordsCount.items():
                csvWrite.writerow(row)
                csvWrite.writerow(row)