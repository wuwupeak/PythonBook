#1.5 pyecharts使用词云显示词频
from pyecharts import WordCloud
import wordsAnalysisFunction as wordsProcess
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/wordsAnalysis.txt'
wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsCount = wordsProcess.analyzeWordsCount(wordsCleaned,5)

words = list(wordsCount.keys())
counts = list(wordsCount.values())
wordCloud = WordCloud(width = 1300, height = 600)
wordCloud.add('词云可视化',words,counts,word_size_range = [20,300]) #word_size_range 最少的频次和最大的频次的图像比例区间
wordCloud.show_config()
wordCloud.render('./PythonStudy/020进阶部分/060dataVisualization/250pyechartsWordCloud.html')