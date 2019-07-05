"""
使用方式说明：
1.pip安装openpyxl模块
2.在本脚本同级目录下新建班级名文件夹，将一次学生作业的所有程序放入其中
3.运行程序，输入“班级文件夹”的名字
4.在脚本统计目录下查看文件：程序运行结果.xlsx
"""

import os
import openpyxl

"""创建结果excel,初始化表头和sheet业名字"""
def createTable(classDirName):
    wb=openpyxl.Workbook()
    sheet=wb.get_active_sheet()
    sheet.title=classDirName
    sheet['A1'] ='文件名'
    sheet['B1'] ='执行结果'
    sheet['C1'] ='程序输出'
    wb.save('程序运行结果.xlsx')

"""将一次运行结果写入excel"""
def writeOneRowToExcel(classDirName,rowNum,*args):
    wb=openpyxl.load_workbook('程序运行结果.xlsx')
    sheet=wb.get_sheet_by_name(classDirName)
    start='A'
    index=0
    for argv in args:
        dest=str(chr(ord(start)+index))+str(rowNum)
        sheet[dest]=argv
        index+=1
    wb.save('程序运行结果.xlsx')

"""获取缓存的结果"""
def getFileContent(path_to_file):
    file = open(path_to_file,'r',encoding='UTF-8')
    out_str=''
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        out_str=out_str+line
    return out_str

"""主程序，运行班级文件夹中的所有程序，调用函数，将执行结果状态和程序输出写入excel"""
def runHomeworkCheckTask():
    #classDirName=input('请输入班级名称：')
    classDirName='homeFileRun'
    #获取当前工作目录
    currentDir = os.path.curdir
    #获取作业存放目录
    workDir=currentDir+os.path.sep+classDirName+os.path.sep
    #指定单次运行结果写入位置，方便后面读出
    logfile=currentDir+os.path.sep+'cmdrst.txt'
    createTable(classDirName)
    files=os.listdir(workDir)
    row=2
    for file in files:
        cmdStr='python '+workDir+file+' > ' +logfile
        cmdState='Success' if not os.system(cmdStr) else 'Failed'
        cmdRst=getFileContent(logfile)
        writeOneRowToExcel(classDirName,row,file,cmdState,cmdRst)
        row+=1

if __name__=='__main__':
    runHomeworkCheckTask()