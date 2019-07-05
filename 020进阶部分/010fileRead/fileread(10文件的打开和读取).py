# 1.1 文件的打开和读取
# -*- coding:utf-8 -*-
with open('D:\\PythonStudy\\PythonStudy\\PythonStudy V1.0\\020进阶部分\\010fileRead\\fileRead.txt', encoding='UTF-8') as fileObject: #转义符'\\'和读取中文的编码'UTF-8',linux系统使用斜杠'/'
        contents = fileObject.read()
        print(contents)
