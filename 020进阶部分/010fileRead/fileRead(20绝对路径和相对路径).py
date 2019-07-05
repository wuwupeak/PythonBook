# 1.1 相对路径
with open('./PythonStudy/PythonStudy V1.0/020进阶部分/010fileRead/fileRead.txt', encoding='UTF-8') as fileObject: #./代表相对路径中的工作目录
        contents = fileObject.read()
        print(contents)

# 1.2 父文件夹表达
with open('../PythonStudy/PythonStudy/PythonStudy V1.0/020进阶部分/010fileRead/fileRead.txt', encoding='UTF-8') as fileObject: #../代表相对路径中的工作目录的上一级目录
        contents = fileObject.read()
        print(contents)


# 1.3 使用os模块获取当前文件所在路径
import os
filePath = os.path.abspath(__file__)  # 当前文件的绝对路径
print(filePath)

fileFolderPath = os.path.dirname(os.path.abspath(__file__))  # 当前文件所在文件夹的绝对路径
print(fileFolderPath) 