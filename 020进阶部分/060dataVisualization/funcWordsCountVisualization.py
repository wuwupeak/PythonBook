from pyecharts import Bar
from pyecharts import WordCloud
import os

def getFilePathFolder():
        fileFolderDir = os.path.dirname(__file__) #使用os模块的函数拿到正在当前文件所在文件夹的绝对路径
        filePathFolder= fileFolderDir+"\\"
        return(filePathFolder)

def getValueXY(wordsCountDict):
        bar_x = []
        bar_y = []
        for x,y in wordsCountDict.items():#遍历已排序的字典wordsCountDict的键、值
                if y > 4: #将词频出现5次及以上的单词进行显示
                        bar_x.append(x)
                        bar_y.append(y)
        return([bar_x,bar_y])

def drawWordsCountBar(wordsCountDict):
        bar_x = getValueXY(wordsCountDict)[0]
        bar_y = getValueXY(wordsCountDict)[1]

        bar = Bar('词频统计','英文词频统计')
        bar.use_theme('dark')
        bar.add('文章词频',bar_x,bar_y,mark_line = ['average'],mark_point = ['max','min'])
        filePathFolder = getFilePathFolder()
        bar.render(filePathFolder + 'wordsCount.html')

def drawWordsCountCloud(wordsCountDict):
        bar_x = getValueXY(wordsCountDict)[0]
        bar_y = getValueXY(wordsCountDict)[1]

        wordCloud = WordCloud(width = 900,height = 600)
        wordCloud.add('英文单词词频',bar_x,bar_y,word_size_range = [60,180])
        filePathFolder = getFilePathFolder()
        wordCloud.render(filePathFolder + 'wordsCloud.html')




