# 1.5 基本的文件内容查找，结合while的改进版本
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

active = True
while active:
        charFind = input('请输入你要查找的字符(输入"quit"结束分析)：')
        if charFind != 'quit':
                lineNumber = 0
                charCountSum = 0
                for line in lines:
                        charCount = line.count(charFind)  # 计算每一行找到的字符个数
                        charCountSum += charCount  # 计算找到字符的合计数
                        lineNumber += 1 
                        print('第' + str(lineNumber) + '行找到' + "'" + charFind + "'" + '共计' + str(charCount) + '个')
                print('找到' + "'" + charFind + "'" + '共计' + str(charCountSum) + '个') 
        else:
                active = False