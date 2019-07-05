# 1.1 写入文件
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileWrite.txt"  # 写入文件的全路径
#（'w' ）告诉Python，我们要以写入模式 打开这个文件。
# 打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。
# 写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
# 如果你要写入的文件不存在，函数open() 将自动创建它
with open(fileFullPath, 'w', encoding='UTF-8') as fileObject: 
        fileObject.write('我写入了一行数据')
