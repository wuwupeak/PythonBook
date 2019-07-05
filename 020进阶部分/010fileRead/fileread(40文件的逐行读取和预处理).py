# 1.3 文件的逐行读取和内容预处理
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileRead.txt"  # 读取文件的全路径
lineNumber = 1
lineLength = 0 
with open(fileFullPath, encoding='UTF-8') as fileObject:
        for line in fileObject:
                lineProcessed = line.strip()  # 删除首尾的空格，预处理
                if (len(lineProcessed) != 0):  # 将空行处理掉
                        print('第'+str(lineNumber)+'行，' + '长度为：'+str(len(lineProcessed)))
                        print(lineProcessed)
                        lineNumber += 1