# 1.1 将内容拆分成单词列表的程序
fileFullPath = './pythonStudy/020进阶部分/030wordsAnalysis/wordsAnalysis.txt'
with open(fileFullPath,'r',encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        words = contents.split()
print(words)
print(len(words))