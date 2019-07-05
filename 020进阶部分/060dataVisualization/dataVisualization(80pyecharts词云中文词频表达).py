# 1.1 中文分词模块jieba
import os
import jieba
words = '我们今天早点去学校上课，因为要打扫卫生，今天上课内容是python程序设计。'
words_list = jieba.cut(words, cut_all=True)
print("-".join(words_list))
words_list = jieba.cut(words, cut_all=False)
print(" ".join(words_list))
words_list = jieba.cut_for_search(words)
print("/".join(words_list))

# 1.2 对文本的分词
import jieba
from pyecharts import WordCloud
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/wordsAnalysis.txt'
with open(os.path.join('./PythonStudy/020进阶部分/060dataVisualization/','wordCHAnalysis.txt'),'r',encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        jieba.add_word('大数据') #添加用户自己定义的字典
        jieba.add_word('云计算')
        jieba.add_word('区块链')
        words_cut = jieba.cut(contents, cut_all=True)

words_list = list(words_cut)
print(list(words_list))

wordsUnique = []
wordsCount = {}
minCount = 4
for word in words_list:
        if word not in wordsUnique:
                wordsUnique.append(word)
for wordUnique in wordsUnique:
        wordCount = words_list.count(wordUnique)
        if wordCount >= minCount: #此处利用参数来选择最小的词频
                wordsCount[wordUnique] = wordCount
wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #使用该排序将字典变成有序的元组
wordsCountDict = dict(wordsCountOrder) #将有序的元组转换为字典
del wordsCountDict['的'] #去除一些无意义的统计词频
del wordsCountDict['与']
del wordsCountDict['和']
del wordsCountDict['了']
del wordsCountDict['年']
del wordsCountDict['个']
del wordsCountDict['从']
del wordsCountDict['将']
del wordsCountDict['在']
del wordsCountDict['等']
del wordsCountDict['是']
del wordsCountDict['']
print(wordsCountDict)


words = list(wordsCountDict.keys())
counts = list(wordsCountDict.values())
wordCloud = WordCloud(width = 1300, height = 600)
wordCloud.add('词云可视化',words,counts,word_size_range = [20,100]) #word_size_range 最少的频次和最大的频次的图像比例区间
wordCloud.render(os.path.join('./PythonStudy/020进阶部分/060dataVisualization/','260pyechartsWordCloud.html'))