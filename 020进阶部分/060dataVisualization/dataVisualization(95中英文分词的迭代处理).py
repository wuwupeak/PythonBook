#绝对路径
#转义符'\\'和读取中文的编码'UTF-8',linux系统使用斜杠'/'
with open('D:\\PythonStudy-V1.0\\PythonStudy\\020进阶部分\\060dataVisualization\\fileRead.txt',encoding='UTF-8') as fileObject: 
        contents = fileObject.read()
        print(contents)
        
# #相对路径
# #转义符'\\'和读取中文的编码'UTF-8',linux系统使用斜杠'/'
# with open('./fileRead.txt',encoding='UTF-8') as fileObject: 
#         contents = fileObject.read()
#         print(contents)

# 使用os模块获取当前文件和文件夹的绝对路径
import os
filePath = os.path.abspath(__file__) #当前文件的绝对路径
print(filePath)

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
print(fileFolderPath) 

#使用os模块使用绝对路径读取文件
import os
fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileName = "fileRead.txt"
fileFullPath = fileFolderPath + "\\" + fileName
with open(fileFullPath,encoding='UTF-8') as fileObject: 
        contents = fileObject.read()
        print(contents)

#使用封装的函数进行文件读取
import fileReadFunc
with open(fileReadFunc.fileOpen("fileRead.txt"),encoding='UTF-8') as fileObject: 
        contents = fileObject.read()
        print(contents)


# 1.3 文件的逐行读取和内容预处理
import fileReadFunc
lineNumber = 1
lineLength = 0 
with open(fileReadFunc.fileOpen("fileRead.txt"),encoding='UTF-8') as fileObject:
        for line in fileObject:
                lineProcessed = line.strip() #删除首尾的空格，预处理
                if (len(lineProcessed) != 0): #将空行处理掉
                        print('第'+str(lineNumber)+'行，' + '长度为：'+str(len(lineProcessed)))
                        print(lineProcessed)
                        lineNumber += 1

# 1.5 基本的文件内容查找
import fileReadFunc
lineNumber = 1
lineLength = 0 
lines = []
with open(fileReadFunc.fileOpen("fileRead.txt"),encoding='UTF-8') as fileObject:
        for line in fileObject:
                lineProcessed = line.strip() #删除首尾的空格，预处理
                if (len(lineProcessed) != 0): #将空行处理掉
                        lines.append(lineProcessed)
                        print('第'+str(lineNumber)+'行，' + '长度为：'+str(len(lineProcessed)))
                        print(lineProcessed)
                        lineNumber += 1
charFind = input('请输入你要查找的字符：')
lineNumber = 0
for line in lines:
        charCount = line.count(charFind)
        lineNumber +=1 
        print('第' + str(lineNumber) + '段找到' + "'" + charFind + "'" + '共计' + str(charCount) + '个')



# 1.5 基本的文件内容查找，结合while的改进版本
import fileReadFunc
lineNumber = 1
lineLength = 0 
lines = []
with open(fileReadFunc.fileOpen("wordsAnalysis.txt"),encoding='UTF-8') as fileObject:
        for line in fileObject:
                lineProcessed = line.strip() #删除首尾的空格，预处理
                if (len(lineProcessed) != 0): #将空行处理掉
                        lines.append(lineProcessed)
                        print('第'+str(lineNumber)+'行，' + '长度为：'+str(len(lineProcessed)))
                        print(lineProcessed)
                        lineNumber += 1
while True:
        charFind = input('请输入你要查找的字符(输入"quit"结束分析)：')
        if charFind != 'quit':
                lineNumber = 0
                charCountSum = 0
                for line in lines:
                        charCount = line.count(charFind) #计算每一行找到的字符个数
                        charCountSum = charCountSum + charCount #计算找到字符的合计数
                        lineNumber = lineNumber + 1 
                        print('第' + str(lineNumber) + '行找到' + "'" + charFind + "'" + '共计' + str(charCount) + '个')
                print('找到' + "'" + charFind + "'" + '共计' + str(charCountSum) + '个') 
        else:
                break

#英文分词的基础
contents = "I’m coming back tomorrow to see how you are getting along,You are the good man."
words = contents.split()
print(words)
contents = contents.replace("'",' ')
contents = contents.replace(",",' ')
contents = contents.replace(".",' ')
words = contents.split()
print(words)

contents = "I’m coming back tomorrow to see how you are getting along,You are the good man."
words = contents.replace("'",' ').replace(",",' ').replace(".",' ').split()
print(words)
                
import fileReadFunc
with open(fileReadFunc.fileOpen("wordsAnalysis.txt"),encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        contents = contents.replace("'",' ')
        contents = contents.replace(",",' ')
        contents = contents.replace(".",' ')
        contents = contents.replace("?",' ')
        contents = contents.replace("!",' ')
        words = contents.split()
print(words)

wordsCleaned = []
for word in words:
        if (len(word) != 1):
                wordsCleaned.append(word.lower())
print(wordsCleaned)

print(len(words))
print(len(wordsCleaned))

wordsUniqueSet = set(wordsCleaned)
wordsUnique = list(wordsUniqueSet)
print(len(wordsUnique))


wordsCount = {}
for word in wordsUnique:
        if wordsCleaned.count(word) > 1:
                wordsCount[word] = wordsCleaned.count(word)
print(wordsCount)

wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #使用该排序将字典变成有序的元组
wordsCountDict = dict(wordsCountOrder) 
print(wordsCountDict)

#写入CSV文件
import csv
with open(fileReadFunc.fileOpen("fileAnalysisUpper.csv"),'w',newline = '',encoding='UTF-8') as csvFile:
        csvWrite = csv.writer(csvFile)
        for row in wordsCountDict.items():
                csvWrite.writerow(row)


from pyecharts import Bar #引入数据可视化模块pyechart中的Bar直方图
bar_x = []
bar_y = []
for x,y in wordsCountDict.items():#遍历已排序的字典wordsCountDict的键、值
        if y > 4: #将词频出现5次及以上的单词进行显示
                bar_x.append(x)
                bar_y.append(y)
bar = Bar('words count','English words count')
bar.use_theme('dark')
bar.add('文章词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
bar.render('wordsCount.html')

from pyecharts import WordCloud
bar_x = list(wordsCountDict.keys())
bar_y = list(wordsCountDict.values())
wordCloud = WordCloud(width = 900,height = 600)
wordCloud.add('英文单词词频',bar_x,bar_y,word_size_range = [60,180])
wordCloud.render('wordsCloud.html')

#使用函数封装的分词可视化
import wordsProcess
wordsCleaned = []
with open(wordsProcess.fileOpen("wordsAnalysis.txt"),encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        wordsCleaned = wordsProcess.wordsClean(contents)
wordsCountDict = wordsProcess.wordsStatic(wordsCleaned,9)
wordsProcess.resultShow('bar',wordsCountDict,'英文词频','英文词频统计范例','word and count')
wordsProcess.resultShow('wordcloud',wordsCountDict,'英文词频')


#中文分词的基本处理
import jieba
words = '我们今天早点去学校上课，因为要打扫卫生，今天上课内容是python程序设计。'
words_list = jieba.cut(words, cut_all=False)
print(list(words_list))
words_list = jieba.cut(words, cut_all=True)
print(list(words_list))

#中文分词对文件的处理
import jieba
import wordsProcess
with open(wordsProcess.fileOpen("wordCHAnalysis.txt"),encoding='UTF-8') as fileObject:
        contents = fileObject.read()
jieba.add_word('大数据') #添加用户自己定义的字典
jieba.add_word('云计算')
jieba.add_word('区块链')
jieba.add_word('新技术')
jieba.add_word('C端')
jieba.add_word('B端')
wordslist = list(jieba.cut(contents, cut_all=False))

wordsSet = set(wordslist)
wordsUniquelist = list(wordsSet)
print(wordsUniquelist)
print(len(wordslist))
print(len(wordsUniquelist))

for word in wordsUniquelist:
        if len(word.strip()) == 1:
                wordsUniquelist.remove(word)
print(len(wordsUniquelist))
print(wordsUniquelist)

wordsCountDict = {}
for word in wordsUniquelist:
        if wordslist.count(word) > 2:
                wordsCountDict[word] = wordslist.count(word)

wordsCountOrderDict = dict(sorted(wordsCountDict.items(),key = lambda item:item[1]))
print(wordsCountOrderDict)

wordsProcess.resultShow('bar',wordsCountOrderDict,'中文词频','中文词频统计范例','单词和词频')
wordsProcess.resultShow('wordcloud',wordsCountOrderDict,'中文词频')


#函数封装的中文词频处理程序
import wordsProcess
wordsCuted = []
with open(wordsProcess.fileOpen("wordCHAnalysis.txt"),encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        wordsCuted = wordsProcess.chWordsCut(contents)
wordsUniquelist = wordsProcess.chWordsUniqueClean(wordsCuted)
wordsCountOrderDict = wordsProcess.chWordsStatic(wordsUniquelist,wordsCuted,3)

wordsProcess.resultShow('bar',wordsCountOrderDict,'中文词频','中文词频统计范例','单词和词频')
wordsProcess.resultShow('wordcloud',wordsCountOrderDict,'中文词频')





















