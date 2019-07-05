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
strValue = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
strClean = strValue.replace(",","").replace(".","")
wordslist = strClean.split()
wordsCount = len(wordslist)
wordUniquelist = []
for word in wordslist:
    if word not in wordUniquelist:
        wordUniquelist.append(word)
wordUniquecount = len(wordUniquelist)
wordsCountlist = []
wordsCountdict = {}
for wordUnique in wordUniquelist:
    wordcount = 0
    for word in wordslist:
        if word == wordUnique:
            wordcount = wordcount + 1
    wordsCountdict[wordUnique] = wordcount
print(wordsCountdict)



# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
wordCountfive = {}
for key, value in wordsCountdict.items():
    if len(key) > 5:
            wordCountfive[key] = value
print(wordCountfive)



# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
word = input("请输入您要搜索的单词: ")
wordseach = word
wordseachcount = wordslist.count(word)
print(wordseach + "在文章中出现的次数: " + str(wordseachcount))





"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
