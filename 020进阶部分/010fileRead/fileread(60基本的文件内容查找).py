# 1.5 基本的文件内容查找
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileRead.txt"  # 读取文件的全路径
lineNumber = 1
lineLength = 0 
lines = []
with open(fileFullPath, encoding='UTF-8') as fileObject:
        for line in fileObject:
                lineProcessed = line.strip()  # 删除首尾的空格，预处理
                if (len(lineProcessed) != 0):  # 将空行处理掉
                        lines.append(lineProcessed)
                        print('第'+str(lineNumber)+'行，' + '长度为：'+str(len(lineProcessed)))
                        print(lineProcessed)
                        lineNumber += 1
charFind = input('请输入你要查找的字符：')
lineNumber = 0
for line in lines:
        charCount = line.count(charFind)
        lineNumber +=1 
        print('第' + str(lineNumber) + '段找到' + "'" + charFind + "'" + '共计' + str(charCount) + '个')