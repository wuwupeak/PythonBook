#2.4 pyecharts使用字典转换成有序列表
from pyecharts import Bar
import wordsAnalysisFunction as wordsProcess
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  #当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + '/wordsAnalysis.txt'
wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsCount = wordsProcess.analyzeWordsCount(wordsCleaned,5)

bar = Bar('分词统计的范例','英文分词')
bar.use_theme("dark") #使用黑色主题。dark,chalk....等等
bar.add('文章词频',list(wordsCount.keys()),list(wordsCount.values()),mark_line = ['average'],mark_point = ['max','min']) #使用字典转换为列表
bar.render( './PythonStudy/020进阶部分/060dataVisualization/240pyechartsBarMore.html')    # 生成本地 HTML 文件