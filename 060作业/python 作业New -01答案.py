"""
Python-作业（第一次）
有一段文字需要处理，文字内容如下：
"When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."

"""
# 请根据上述文字，编写程序，输出以下问题的结果。

#  问题一：该段文字总共有多少个单词？【4分】
stringValue = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
stringCleaned = stringValue.replace(",","").replace(".","")
wordsList = stringCleaned.split()
wordsCount = len(wordsList)
print("这段话总共有" + str(wordsCount) + "个单词。")

# 问题二：该段文字总共出现了多少个独一无二的单词？【2分】
wordsUniqueList = []
for word in wordsList:
    if word not in wordsUniqueList:
        wordsUniqueList.append(word)
wordsUniqueCount = len(wordsUniqueList)
print("这段话总共有" + str(wordsUniqueCount) + "个独一无二的单词。")

# 问题三：该段文字每个单词出现的次数是多少？【3分】
wordsCountList = []
for wordUnique in wordsUniqueList:
    wordcount = 0
    for word in wordsList:
        if word == wordUnique:
            wordcount = wordcount + 1
    wordsCountList.append(wordcount)
for index in range(len(wordsUniqueList)):
    print("单词:" + wordsUniqueList[index] + "在文章中出现的次数是:" + str(wordsCountList[index]))







"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-01-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
