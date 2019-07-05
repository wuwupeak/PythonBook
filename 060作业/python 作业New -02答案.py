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
stringCleaned = stringValue.replace(",","").replace(".","")
wordsList = stringCleaned.split()
wordsCount = len(wordsList)
print("这段话总共有" + str(wordsCount) + "个单词。")
wordsUniqueList = []
for word in wordsList:
    if word not in wordsUniqueList:
        wordsUniqueList.append(word)
wordsUniqueCount = len(wordsUniqueList)
print("这段话总共有" + str(wordsUniqueCount) + "个独一无二的单词。")
wordsCountDict = {}
for wordUnique in wordsUniqueList:
    wordCount = wordsList.count(wordUnique)
    wordsCountDict[wordUnique] = wordCount
print(wordsCountDict)


# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【3分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
wordsCountOverFiveDict = {}
for wordUnique in wordsUniqueList:
    if len(wordUnique) > 5:
        wordCount = wordsList.count(wordUnique)
        wordsCountOverFiveDict[wordUnique] = wordCount
print(wordsCountOverFiveDict)




# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【2分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
word = input("请输入要查找的单词：")
print(word + "在文章中出现的次数是:" + str(wordsCountDict[word]))







"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
