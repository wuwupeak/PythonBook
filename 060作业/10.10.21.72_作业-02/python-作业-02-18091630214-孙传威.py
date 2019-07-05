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

# 把，替换为空格
stringCleaned = stringValue.replace(",","").replace(".","")
# 以空格为分割符
wordsList = stringCleaned.split()
# 新建列表，存放该段文字中独一无二单词
wordsUniqueList = []
for word in wordsList:
    if word not in wordsUniqueList:
        wordsUniqueList.append(word)
# 新建空字典
wordsCountDist= {}
# 该段文字每个单词出现的次数
wordsCountList = []
for wordUnique in wordsUniqueList:
    wordcount = 0
    for word in wordsList:
        if word == wordUnique:
            wordcount = wordcount + 1
    wordsCountDist[wordUnique] = wordcount
print(wordsCountDist)






# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"

# 新建空字典用来存放单词长度超过5个字母的单词出现次数
wordcountFive = {}
# 字符键值对的遍历
for key,value in wordsCountDist.items():
    if len(key) >5:
        wordcountFive[key]= value
print(wordcountFive)






# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"

# 用户输入的单词
word = input('请输入文章中的单词:')
# 获取用户输入的单词在文章中出现的次数
word_count = wordsCountDist.get(word,0)
print("{}在文章中出现的次数是:{}".format(word,word_count))




"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
