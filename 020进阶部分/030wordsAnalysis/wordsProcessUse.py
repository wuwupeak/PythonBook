import wordsProcess
fileName = "\\wordsAnalysis.txt"
# fileContent = wordsProcess.fileRead(fileName)
# wordsCleaned = wordsProcess.fileClean(fileContent)
# wordsUnique = wordsProcess.fileWordsUnique(wordsCleaned)
# wordsCountDict = wordsProcess.fileWordsCount(wordsCleaned,wordsUnique)
wordsCountDict = wordsProcess.fileWordsCountAll(fileName)
print(wordsCountDict)

# help(wordsProcess.fileRead)

# from pyecharts import Bar #引入数据可视化模块pyechart中的Bar直方图
# bar_x = []
# bar_y = []
# for x,y in wordsCountDict.items():#遍历已排序的字典wordsCountDict的键、值
#         if y > 4: #将词频出现5次及以上的单词进行显示
#                 bar_x.append(x)
#                 bar_y.append(y)
# bar = Bar('words count','English words count')
# bar.use_theme('dark')
# bar.add('文章1词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
# bar.add('文章2词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
# bar.add('文章3词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
# bar.render('wordsCount.html')

# from pyecharts import WordCloud
# wordCloud = WordCloud(width = 900,height = 600)
# wordCloud.add('英文单词词频',bar_x,bar_y,word_size_range = [60,180])
# wordCloud.render('wordsCloud.html')