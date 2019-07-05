# 1.2 文件读取去除最后一个空行
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileRead.txt"  # 读取文件的全路径
with open(fileFullPath, encoding='UTF-8') as fileObject:  # 读取中文的编码'UTF-8'
        contents = fileObject.read()
        print(contents.rstrip())  # 因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.