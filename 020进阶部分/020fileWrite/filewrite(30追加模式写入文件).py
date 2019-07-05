# 1.3 附加模式写入文件，不清空
import os

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
fileFullPath = fileFolderPath + "/fileWrite.txt"  # 写入文件的全路径
with open(fileFullPath, 'a', encoding='UTF-8') as fileObject:  # （'a' ）告诉Python，我们要以附加模式 打开这个文件。
        fileObject.write('附加：我写入了一行数据。\n')  # 使用换行转义符'\n'
        fileObject.write('附加：我又写入了一行数据。\n')  # 使用换行转义符'\n'
        fileObject.write('附加：我又又写入了一行数据。\n')  # 使用换行转义符'\n'

with open(fileFullPath, 'r', encoding='UTF-8') as fileObject:  # （'r' ）告诉Python，我们要以只读模式 打开这个文件。
        print(fileObject.read())