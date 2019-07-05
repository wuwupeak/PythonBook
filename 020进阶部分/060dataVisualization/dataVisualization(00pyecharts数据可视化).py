#字符串的处理
sentence = "What are you doing? I am working."
print(sentence)
sentence = sentence.replace('?',' ') #使用replace将？替换成空格
print(sentence)
sentence = sentence.replace('.',' ') #使用replace将.替换成空格
print(sentence)
words = sentence.split() #split方法以空格作为分隔符将字符串拆分成单词列表
print(words)

#对英文文本文件的分词处理
import os
fileFolderDir = os.path.dirname(__file__) #使用os模块的函数拿到正在当前文件所在文件夹的绝对路径
fileFullPath = fileFolderDir + "\\wordsAnalysis.txt" #使用字符串拼接，得到需要打开文件的绝对路径
with open(fileFullPath,encoding = 'utf-8') as fileObject: #使用绝对路径打开文件，并将文件作为一个对象fileObject
    fileContent = fileObject.read() #读取文件对象的内容，并赋值给变量fileContent


#     print(type(fileContent))
#将标点符号替换为空格
fileContent = fileContent.replace('?',' ')
fileContent = fileContent.replace(';',' ')
fileContent = fileContent.replace('.',' ')
fileContent = fileContent.replace(',',' ')
fileContent = fileContent.replace(':',' ')
fileContent = fileContent.replace('"',' ')
fileContent = fileContent.replace("'",' ')
fileContent = fileContent.replace('(',' ')
fileContent = fileContent.replace(')',' ')
fileContent = fileContent.replace("’",' ')
fileContent = fileContent.replace("“",' ')
fileContent = fileContent.replace("”",' ')
words = fileContent.lower().split() #split方法使用空格作为分隔符将字符串fileContent拆分成列表
# print(words)
# print(type(words))
# print(len(words))

for word in words:
    if len(word) == 1 and word != "i": #去除单词长度为1，且不是大写I的单词
        words.remove(word)
# print(words)
# print(type(words))
# print(len(words))

wordsUnique = [] #初始化空列表wordsUnique，用于存储words列表中出现的不重复单词
for word in words:
    if wordsUnique.count(word) == 0: #如果在wordsUnique列表中找不到单词word就加入该列表
        wordsUnique.append(word)
# print(wordsUnique)
# print(len(wordsUnique))

wordsCount = {}
for word in wordsUnique:
    wordsCount[word] = words.count(word) #将words列表中出现word的次数作为值，word作为键加入字典wordsCount
print(len(wordsCount))
wordsCount = {wordUnique:words.count(wordUnique) for wordUnique in wordsUnique} #使用生成器模式生成词频字典
print(len(wordsCount))


wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #对字典的value进行排序
wordsCountDict = dict(wordsCountOrder) #将元祖转换为字典
# print(wordsCountDict)

from pyecharts import Bar #引入数据可视化模块pyechart中的Bar直方图
bar_x = []
bar_y = []
for x,y in wordsCountDict.items():#遍历已排序的字典wordsCountDict的键、值
        if y > 4: #将词频出现5次及以上的单词进行显示
                bar_x.append(x)
                bar_y.append(y)
bar = Bar('words count','English words count')
bar.use_theme('dark')
bar.add('文章1词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
bar.add('文章2词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
bar.add('文章3词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
bar.render('wordsCount.html')

from pyecharts import WordCloud
# words = list(wordsCountDict.keys())
# counts = list(wordsCountDict.values())
wordCloud = WordCloud(width = 900,height = 600)
wordCloud.add('英文单词词频',bar_x,bar_y,word_size_range = [60,180])
wordCloud.render('wordsCloud.html')
