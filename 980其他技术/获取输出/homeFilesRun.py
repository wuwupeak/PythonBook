import os
import sys
import csv
import pysnooper


def getWorkPath():
        workFilesDirName = "homeWorkFiles"
        processFileFullPath = os.path.abspath(__file__)  # 当前文件全路径
        fileName = os.path.basename(__file__)  # 当前文件名名称
        filePathDir = processFileFullPath.replace(fileName, "")  # 当前文件文件夹
        workFilesPathDir = filePathDir + workFilesDirName + os.path.sep  # 作业所在文件夹
        return workFilesPathDir

@pysnooper.snoop()
def processWorkFiles(workFilesPathDir):
        csvFileName = "result.csv"
        csvFilePath = workFilesPathDir + csvFileName  # 处理不存在的CSV文件
        if not os.path.exists(csvFilePath):
                csvFile = open(csvFilePath, 'w')
                csvFile.close()
        filesList = os.listdir(workFilesPathDir)  # 处理已经存在的输出脚本文件
        filesNameList = []
        for fileName in filesList:
                if fileName.endswith(".txt"):
                        os.remove(fileName)
                if fileName.endswith(".py"):
                        filesNameList.append(fileName.replace(".py", ""))
        return filesNameList, csvFilePath


def comToText(filesNameList):
        for fileName in filesNameList:
                pyFileName = fileName + ".py"
                textFileName = fileName + ".txt"
                runCMD = 'python ' + pyFileName + '> ' + textFileName
                os.system(runCMD)


def textToCSV(filesNameList, csvWrite):
        for fileName in filesNameList:
                textFileName = fileName + ".txt"
                with open(textFileName, encoding='UTF-8') as textObject:  # 转义符'\\'和读取中文的编码'UTF-8',linux系统使用斜杠'/'
                        textLine = textObject.readline()
                        resultCount = 1
                        while textLine:
                                csvWrite. writerow([fileName, resultCount, textLine])
                                textLine = textObject.readline()
                                resultCount = resultCount + 1    


def writeToCSV():
        workFilesPathDir = getWorkPath()
        os.chdir(workFilesPathDir)  # 切换当前工作目录
        filesNameList, csvFilePath = processWorkFiles(workFilesPathDir)
        comToText(filesNameList)
        with open(csvFilePath, 'w', newline='', encoding='utf-8-sig') as csvObject:  # 转义符'\\'和读取中文的编码'UTF-8',linux系统使用斜杠'/'
                csvWrite = csv.writer(csvObject, delimiter=',')
                csvWrite. writerow(["文件名", "结果序号", "输出结果"])
                textToCSV(filesNameList, csvWrite)
        processWorkFiles(workFilesPathDir)
        
if __name__=='__main__':
    writeToCSV()