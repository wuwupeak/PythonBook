#2.3 pyecharts使用主题(pip install echarts-themes-pypkg)
from pyecharts import Bar
import wordsAnalysisFunction as wordsProcess
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/wordsAnalysis.txt'
wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsCount = wordsProcess.analyzeWordsCount(wordsCleaned,5)
input_X = []
input_Y = []
for word, count in wordsCount.items():
        if count > 5:
                input_Y.append(count)
                input_X.append(word)

bar = Bar('分词统计的范例','英文分词')
bar.use_theme("dark") #使用黑色主题。dark,chalk....等等
bar.add('文章词频',input_X,input_Y)
# bar.add('文章词频',input_X,input_Y,is_more_utils=True) #更加强大的工具选项，支持局部缩放和折线图
bar.render( './PythonStudy/020进阶部分/060dataVisualization/230pyechartsTheme.html')    # 生成本地 HTML 文件