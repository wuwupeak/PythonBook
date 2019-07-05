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
wordsValue = """When the aerials are down, and your spirit is covered with snows of cynicism and 
the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials 
are up, to catch the waves of optimism, there is hope you may die young at eighty."""
WordsValue = wordsValue.lower()  # 将所有字符串改成小写字母
StringCleaned = WordsValue.replace(',','').replace('.','')  # 将 ","和"." 替换空格
WordsList = StringCleaned.split()  # 将每段的距离设置成等大的
WordsCount = len(WordsList)
WordsUniqueList = []
for word in WordsList:
    if word not in WordsUniqueList:
        WordsUniqueList.append(word)  # 将同种字符串添加到列表中
WordsUniqueCount = len(WordsUniqueList)  # 计算列表中元素出现的个数
WordsCountDict = {}
for WordsUnique in WordsUniqueList:
    WordCount = 0
    for word in WordsList:
        if word == WordsUnique:
            WordCount = WordCount + 1
    WordsCountDict[WordsUnique] = WordCount  # 用字典开始输出
print(WordsCountDict)
# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
WordCountFive = {}
for key, value in WordsCountDict.items():  # 用字典将其遍历
        if len(key) > 5:  # 通过键值来计算单词中字母的个数
                WordCountFive[key] = value
print(WordCountFive)

# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
Words = input('请输入单词：')  # 进行交互式
word = Words
value = WordsCountDict.get(word)  # 利用键值对来查找单词
print("在文章中" + Words + "出现的次数是：" + str(value))


"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
