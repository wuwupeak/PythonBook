# 1.2 写入多行数据
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileWrite.txt"  # 写入文件的全路径
with open(fileFullPath, 'w', encoding='UTF-8') as fileObject:  #（'w' ）告诉Python，我们要以写入模式 打开这个文件。
        fileObject.write('我写入了一行数据。\n') #使用换行转义符'\n'
        fileObject.write('我又写入了一行数据。\n') #使用换行转义符'\n'
        fileObject.write('我又又写入了一行数据。\n') #使用换行转义符'\n'