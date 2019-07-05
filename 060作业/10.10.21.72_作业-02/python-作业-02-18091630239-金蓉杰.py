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
stringValue = """
When the aerials are down, and your spirit is covered with snows of cynicism and the ice of pessimism, then you are grown old, even at twenty, but as long as your aerials are up, to catch the waves of optimism, there is hope you may die young at eighty.
"""
stringValue = stringValue.replace(",","").replace(".","")
list1 = stringValue.split()

wordUniqueList = []
wordCountDict = {}
for word in list1:                    #遍历liat1的列表
    if word not in wordUniqueList:
        wordUniqueList.append(word)   #向wordUniqueList中添加元素
for word in wordUniqueList:
    wordCount = list1.count(word)     #计算单词出现的次数
    wordCountDict[word] = wordCount   
print(wordCountDict)



# 问题二：其中单词长度超过5个字母的单词出现的次数是多少？【2分，其中注释清晰1分,必须用字典输出】
# 输出格式为"{***:***,***:***}"
wordLengthDict = {}
for word in wordUniqueList:  #遍历wordUniqueList
    wordLength = len(word)  #计算单词长度
    if wordLength > 5:      #单词长度设计值
        wordLengthCount = list1.count(word)     #计算单词长度超过5字母单词的次数
        wordLengthDict[word] = wordLengthCount  #在字典wordLengthDict中添加wordLengthcount的元素
print(wordLengthDict)




# 问题三：设计一个交互式程序，能够根据用户输入的单词将单词出现的次数打印在屏幕上？【3分，其中注释清晰1分】
# 输出格式为"***在文章中出现的次数是:*"
word = input("请输入你想要搜索的单词：")   #交互输入提示
wordSearch = word
wordSearchCount = list1.count(word)      #计算次数
print(wordSearch+ "在文章中出现的次数是：" + str(wordSearchCount))





"""
注：
提交的文件名称请使用原文件名加学号姓名的方式。【1分】
如同学的学号为“00001”，姓名为“张三”
提交的文件名为“python-作业-02-00001-张三.py”（注意中间的横杠为英文且没有空格）
"""
