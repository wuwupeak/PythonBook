# 1.4 文件的内容存入列表
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileRead.txt"  # 读取文件的全路径
lineNumber = 1
lineLength = 0 
with open(fileFullPath, encoding='UTF-8') as fileObject:
        lines = fileObject.readlines()
for line in lines:
        print(line.strip())
print(lines)