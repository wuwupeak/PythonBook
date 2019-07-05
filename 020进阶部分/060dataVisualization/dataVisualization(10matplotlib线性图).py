# 1.1 使用matplotlib绘制可视化图形,线性
import matplotlib.pyplot as plt
import wordsAnalysisFunction as wordsProcess

fileFullPath = './PythonStudy/020进阶部分/060dataVisualization/wordsAnalysis.txt'

wordsCleaned = wordsProcess.textDivide(fileFullPath)
wordsCount = wordsProcess.analyzeWordsCount(wordsCleaned,5)

input_X = []
input_Y = []
input_labels = []

number = 1

for word,count in sorted(wordsCount.items(),key = lambda item:item[1]):
        if count > 1:
                input_Y.append(count)
                input_X.append(number)
                input_labels.append(word)
                number += 1

plt.plot(input_X, input_Y, linewidth=1) #plt.plot(x,y,format_string,**kwargs)
plt.show()