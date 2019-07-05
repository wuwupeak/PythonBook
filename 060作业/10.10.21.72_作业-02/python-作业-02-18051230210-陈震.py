"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
# 请根据上述文字，编写程序，输出以下问题的结果。

# 问题一：该段文字每个单词出现的次数是多少？【3分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
stringValue = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
stringCleaned = stringValue.replace(",","")
stringCleaned = stringCleaned.replace(".","")
wordsList = stringCleaned.split()
wordsCount = len(wordsList)                #此步输出为该段文字总共有多少个单词
wordsUniqueList = []
for word in wordsList:
    if word not in wordsUniqueList:
        wordsUniqueList.append(word)
wordsUniqueCount = len(wordsUniqueList)    #此步输出为该段文字总共出现了多少个独一无二的单词
wordsCountDict = {}
wordsCountList = []
for wordUnique in wordsUniqueList:
    wordcount = 0
    for word in wordsList:
        if word == wordUnique:
            wordcount = wordcount + 1
    wordsCountDict[wordUnique] = wordcount
print(wordsCountDict)                      #此步输出为该段文字每个单词出现的次数是多少

# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
# 变value
# wordCountFive = {}
# for key, value in wordsCountDict.items():
#     if value > 2:                             #对值
#         wordCountFive[key] = value
# print(wordCountFive)
# 变key
wordCountFive = {}
for key, value in wordsCountDict.items():       #字典遍历
    if len(key) > 5:                            #对键
        wordCountFive[key] = value              #添加元素
print(wordCountFive)                            #此步输出为单词长度超过5个字母的单词出现的次数是多少




# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
times = input("请输入单词: ")                        #接受用户输入
wordUnique = times
value = wordsCountDict.get(wordUnique)              #查找
print(times + "在文章中出现的次数是:" +str(value))    #此步输出为***在文章中出现的次数是:*
      







"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
