import os
from pyecharts import Bar
from pyecharts import WordCloud
import jieba

def fileOpen(fileName):
    fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
    fileFullPath = fileFolderPath + "\\" + fileName
    return fileFullPath

def wordsClean(contents):
    contents = contents.replace("'",' ')
    contents = contents.replace(",",' ')
    contents = contents.replace(".",' ')
    contents = contents.replace("?",' ')
    contents = contents.replace("!",' ')
    words = contents.split()
    wordsCleaned = []
    for word in words:
            if (len(word) != 1):
                    wordsCleaned.append(word.lower())
    return wordsCleaned

def wordsStatic(wordsCleaned,number):
    wordsUniqueSet = set(wordsCleaned)
    wordsUnique = list(wordsUniqueSet)
    wordsCount = {}
    for word in wordsUnique:
            if wordsCleaned.count(word) > number:
                    wordsCount[word] = wordsCleaned.count(word)
    wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #使用该排序将字典变成有序的元组
    wordsCountDict = dict(wordsCountOrder) 
    return wordsCountDict

def chWordsCut(contents):
    jieba.add_word('大数据') #添加用户自己定义的字典
    jieba.add_word('云计算')
    jieba.add_word('区块链')
    jieba.add_word('新技术')
    jieba.add_word('C端')
    jieba.add_word('B端')
    return list(jieba.cut(contents, cut_all=False))

def chWordsUniqueClean(wordsCuted):
    wordsSet = set(wordsCuted)
    wordsUniquelist = list(wordsSet)
    wordsUniqueCleanlist = []
    for word in wordsUniquelist:
        if len(word.strip()) != 1 and len(word.strip()) != 0:
                wordsUniqueCleanlist.append(word)
    return wordsUniqueCleanlist

def chWordsStatic(wordsUniquelist,wordslist,number):
    wordsCountDict = {}
    for word in wordsUniquelist:
            if wordslist.count(word) > number:
                    wordsCountDict[word] = wordslist.count(word)
    wordsCountOrderDict = dict(sorted(wordsCountDict.items(),key = lambda item:item[1]))
    return wordsCountOrderDict

def resultShow(typeShow,wordsCountDict,name,mainName = '',subName = ''):
    '''typeShow目前支持bar和wordcloud两种类型，wordsCountDict参数为处理好的词频字典'''
    bar_x = list(wordsCountDict.keys())
    bar_y = list(wordsCountDict.values())
    if typeShow == 'bar':
        bar = Bar(mainName,subName)
        bar.use_theme('dark')
        bar.add(name,bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
        bar.render('wordsBar.html')
    if typeShow == 'wordcloud':
        wordCloud = WordCloud(width = 1024,height = 768)
        wordCloud.add(name,bar_x,bar_y,word_size_range = [20,120])
        wordCloud.render('wordsCloud.html')
